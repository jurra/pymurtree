#include "parameters.h"
#include "parameter_handler.h"
#include "solver.h"

#include <pybind11/pybind11.h>

namespace py = pybind11;
using namespace MurTree;

PYBIND11_MODULE(lib, m) {

    // Bindings for the MurTree::Solver class
    py::class_<Solver> solver(m, "Solver");
    
    // Binding for the MurTree::Solver constructor
    solver.def(py::init([](unsigned int time, unsigned int max_depth,
    unsigned int max_num_nodes, float sparse_coefficient, bool verbose,
    bool all_trees, bool incremental_frequency, bool similarity_lower_bound,
    unsigned int node_selection, unsigned int feature_ordering,
    int random_seed, unsigned int cache_type, int duplicate_factor) 
    {
        ParameterHandler ph = DefineParameters();
        ph.SetStringParameter("file", "_no_anneal.txt");
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

        // Carry-out actions from murtree function main in main.cpp
        CheckParameters(ph);

        if (verbose) { 
            ph.PrintParameterValues();
        }

        // Construct the Solver object
        return new Solver(ph); 

    }), py::keep_alive<0, 1>());


    // Bindings for the Solver::solve metod
    solver.def("solve", []( const Solver &solver, unsigned int time, 
    unsigned int max_depth, unsigned int max_num_nodes, 
    float sparse_coefficient, bool verbose, bool all_trees, 
    bool incremental_frequency, bool similarity_lower_bound,
    unsigned int node_selection, unsigned int feature_ordering,
    int random_seed, unsigned int cache_type, int duplicate_factor)
    {
        ParameterHandler ph = DefineParameters();
        ph.SetStringParameter("file", "anneal.txt");
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

        // Call Solver::solve
        //solver.solve(ph)
    });
    
    // Bindings for the MurTree::SolverResult class
    py::class_<SolverResult> solver_result(m, "SolverResult");          
}

