#include "parameters.h"
#include "parameter_handler.h"
#include "solver.h"
#include "solver_result.h"
#include "feature_vector_binary.h"



#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>


namespace py = pybind11;
using namespace MurTree;

// We need to convert the numpy array to a vector of vectors
// So that we can pass it to the solver
std::vector<std::vector<int>> NumpyToVectors(py::array_t<int, py::array::c_style>& arr) {
    auto buf = arr.request();
    int* ptr = (int*) buf.ptr;
    int nrows = buf.shape[0];
    int ncols = buf.shape[1];

    std::vector<std::vector<int>> result(nrows);
    for (int i = 0; i < nrows; i++) {
        result[i] = std::vector<int>(ptr + i * ncols, ptr + (i+1) * ncols);
    }
    return result;
}

std::vector<std::vector<FeatureVectorBinary>> ReadDataDL(const std::vector<std::vector<int>>& vec, int duplicate_instances_factor)
{
    std::vector<std::vector<FeatureVectorBinary>> feature_vectors;

    int nrows = vec.size();
    int ncols = vec[0].size();

    int id = 0;
    int num_features = ncols - 1;
    for (int i = 0; i < nrows; i++)
    {
        int label = vec[i][0];

        std::vector<bool> v(num_features);
        for (int j = 0; j < num_features; j++)
        {
            v[j] = (vec[i][j+1] == 1);
        }

        if (feature_vectors.size() <= label) { feature_vectors.resize(label+1); } //adjust the vector to take into account the new label (recall that labels are expected to be from 0..num_labels-1
        for (int i = 0; i < duplicate_instances_factor; i++)
        {
            feature_vectors[label].push_back(FeatureVectorBinary(v, id));
            id++;            
        }       
    }
    return feature_vectors;
}

// Utility function to construct a ParameterHandler object
ParameterHandler createParameters( unsigned int time, unsigned int max_depth,
unsigned int max_num_nodes, float sparse_coefficient, bool verbose,
bool all_trees, bool incremental_frequency, bool similarity_lower_bound,
unsigned int node_selection, unsigned int feature_ordering,
int random_seed, unsigned int cache_type, int duplicate_factor)
{
    ParameterHandler ph = DefineParameters();
    // ph.SetStringParameter("file", "./pymurtree_data/data.txt");
    ph.SetFloatParameter("time", time);
    ph.SetIntegerParameter("max-depth", max_depth);
    ph.SetIntegerParameter("max-num-nodes", max_num_nodes);
    ph.SetFloatParameter("sparse-coefficient", sparse_coefficient);
    ph.SetBooleanParameter("verbose", verbose);
    ph.SetBooleanParameter("all-trees", all_trees);
    ph.SetBooleanParameter("incremental-frequency", incremental_frequency);
    ph.SetBooleanParameter("similarity-lower-bound", similarity_lower_bound);
    ph.SetIntegerParameter("random-seed", random_seed);
    ph.SetIntegerParameter("duplicate-factor", duplicate_factor);
    // Node selection
    if (node_selection == 1) {
        ph.SetStringParameter("node-selection", "post-order");
    }
    else {
        ph.SetStringParameter("node-selection", "dynamic");
    }
    // Feature ordering
    if (feature_ordering == 1) {
        ph.SetStringParameter("feature-ordering", "random");
    } 
    else if (feature_ordering == 2) {
        ph.SetStringParameter("feature-ordering", "gini");
    }
    else {
        ph.SetStringParameter("feature-ordering", "in-order");
    }
    // Cache Type
    if (cache_type == 1) {
        ph.SetStringParameter("cache-type", "branch");
    }
    else if (cache_type == 2) {
        ph.SetStringParameter("cache-type", "closure");
    }
    else {
        ph.SetStringParameter("cache-type", "dataset");
    }
    return ph;
}

 
PYBIND11_MODULE(lib, m) {    
    // Read data coming as a numpy array that is then converted to a vector of vectors
    // To do that we need to use the numpy_to_vectors function and then
    // pass the result to the ReadDataDL function
    m.def("read_data", [](py::array_t<int, py::array::c_style>& arr, int duplicate_instances_factor) {
        // We don't return the result as this is only needed to pass the data to the solver
        // This function is meant to be private and will only be used to pass data to the solver like so:
        ReadDataDL(NumpyToVectors(arr), duplicate_instances_factor);
    }, py::arg("np_array"), py::arg("duplicate_instances_factor"), 
          "Reads file and returns feature vectors");

    // Bindings for the MurTree::Solver class
    py::class_<Solver> solver(m, "Solver");
    
    // Bindings for the MurTree::Solver constructor
    solver.def(py::init([](py::array_t<int, py::array::c_style>& arr, // The numpy array containing the data
    unsigned int time, unsigned int max_depth,
    unsigned int max_num_nodes, float sparse_coefficient, bool verbose,
    bool all_trees, bool incremental_frequency, bool similarity_lower_bound,
    unsigned int node_selection, unsigned int feature_ordering,
    int random_seed, unsigned int cache_type, int duplicate_factor) 
    {
        ParameterHandler ph = createParameters(time, max_depth, max_num_nodes,
        sparse_coefficient, verbose, all_trees, incremental_frequency,
        similarity_lower_bound, node_selection, feature_ordering, random_seed,
        cache_type, duplicate_factor);

        // Carry-out actions from murtree function main in main.cpp
        // CheckParameters(ph); // TODO: This should be uncommented later
        if (verbose) { 
            ph.PrintParameterValues();
        }
        
        // Add the data to the parameter handler
        ph.SetData(ReadDataDL(NumpyToVectors(arr), duplicate_factor));

        // Construct the Solver object
        return new Solver(ph); 

    }), py::keep_alive<0, 1>());


    // Bindings for the Solver::solve method
    solver.def("solve", [](Solver &solver, unsigned int time, 
    unsigned int max_depth, unsigned int max_num_nodes, 
    float sparse_coefficient, bool verbose, bool all_trees, 
    bool incremental_frequency, bool similarity_lower_bound,
    unsigned int node_selection, unsigned int feature_ordering,
    int random_seed, unsigned int cache_type, int duplicate_factor)
    {
        ParameterHandler ph = createParameters(time, max_depth, max_num_nodes,
        sparse_coefficient, verbose, all_trees, incremental_frequency,
        similarity_lower_bound, node_selection, feature_ordering, random_seed,
        cache_type, duplicate_factor);
        //CheckParameters(ph);
        return solver.Solve(ph);
    });
    
    // Bindings for the MurTree::SolverResult class
    py::class_<SolverResult> solver_result(m, "SolverResult");

    solver_result.def("misclassification_score", [](const SolverResult &solverresult) {
        return solverresult.misclassifications;
    });

    solver_result.def("tree_depth", [](const SolverResult &solverresult) {
        return solverresult.decision_tree_->Depth();
    });

    solver_result.def("tree_nodes", [](const SolverResult &solverresult) {
        return solverresult.decision_tree_->NumNodes();
    });

}

