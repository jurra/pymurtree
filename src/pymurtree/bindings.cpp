#include "parameters.h"
#include "parameter_handler.h"
#include "solver.h"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <pybind11/chrono.h>
#include <pybind11/functional.h>

namespace py = pybind11;
using namespace MurTree;

struct Pet {
    Pet(const std::string &name) : name(name) { }
    void setName(const std::string &name_) { name = name_; }
    const std::string &getName() const { return name; }

    std::string name;
};
// convert array of two dimensions to vector of vectors in cpp

// convert numpy array to vector of vectors of vectors in cpp

PYBIND11_MODULE(lib, m){
        py::class_<Pet>(m, "Pet")
        .def(py::init<const std::string &>())
        .def("setName", &Pet::setName)
        .def("getName", &Pet::getName);
	// py::class_<ParameterHandler> parameter_handler(m, "ParameterHandler");
  //   parameter_handler.def(py::init([](){ return new ParameterHandler(); }), py::keep_alive<0, 1>())
  //                    .def("define_new_category", &ParameterHandler::DefineNewCategory)
  //                    .def("define_string_parameter", &ParameterHandler::DefineStringParameter)
  //                    .def("define_integer_parameter", &ParameterHandler::DefineIntegerParameter)
  //                    .def("define_float_parameter", &ParameterHandler::DefineFloatParameter)
  //                    .def("define_boolean_parameter", &ParameterHandler::DefineBooleanParameter);
    
    py::class_<Solver> solver(m, "Solver");
    solver.def(py::init(
        [](unsigned int time,
           unsigned int max_depth,
           unsigned int max_num_nodes,
           float sparse_coefficient,
           bool verbose,
           bool all_trees,
           bool incremental_frequency,
           bool similarity_lower_bound,
           unsigned int node_selection,
           unsigned int feature_ordering,
           int random_seed,
           unsigned int cache_type,
           int duplicate_factor) {
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

                return new Solver(ph); 

                }), py::keep_alive<0, 1>())

          .def("solve", 
            []( const Solver &solver, 
                unsigned int time,
                unsigned int max_depth,
                unsigned int max_num_nodes,
                float sparse_coefficient,
                bool verbose,
                bool all_trees,
                bool incremental_frequency,
                bool similarity_lower_bound,
                unsigned int node_selection,
                unsigned int feature_ordering,
                int random_seed,
                unsigned int cache_type,
                int duplicate_factor) {
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
          });
    
    // This is needed to be able to return the tree after solving
    py::class_<SolverResult> solver_result(m, "SolverResult");          
}

