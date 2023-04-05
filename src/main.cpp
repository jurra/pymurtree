#include <pybind11/pybind11.h>

#include "../murtree/code/MurTree/Engine/solver.h"
#include "../murtree/code/MurTree/Engine/dataset_cache.h"
#include "../murtree/code/MurTree/Engine/hyper_parameter_tuner.h"
#include "../murtree/code/MurTree/Utilities/parameter_handler.h"
#include "../murtree/code/MurTree/Utilities/stopwatch.h"
#include "../murtree/murtree.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <time.h>
#include <algorithm>

namespace py = pybind11;
// using namespace murtree;

PYBIND11_MODULE(python_example, m) {

    // py::class_<Solver> solver(m, "Solver");

    // solver.def(py::init<std::string>())
    //       .def("solve", &Solver::solve);

    // py::class_<DatasetCache> dataset_cache(m, "DatasetCache");

    // dataset_cache.def(py::init<Matrix2D, std::vector<size_t>>())
    //              .def("get_subtable", &DatasetCache::get_subtable);

    // py::class_<HyperParameterTuner> hyper_parameter_tuner(m, "HyperParameterTuner");

    // hyper_parameter_tuner.def(py::init<const ParameterHandler&>())
    //                       .def("get_best_parameters", &HyperParameterTuner::get_best_parameters);

    py::class_<ParameterHandler> parameter_handler(m, "ParameterHandler");

    parameter_handler.def(py::init<>())
                     .def("define_new_category", &ParameterHandler::DefineNewCategory)
                     .def("define_string_parameter", &ParameterHandler::DefineStringParameter)
                     .def("define_integer_parameter", &ParameterHandler::DefineIntegerParameter)
                     .def("define_float_parameter", &ParameterHandler::DefineFloatParameter)
                     .def("define_boolean_parameter", &ParameterHandler::DefineBooleanParameter);

}

// #define STRINGIFY(x) #x
// #define MACRO_STRINGIFY(x) STRINGIFY(x)

// int add(int i, int j) {
//     return i + j;
// }

// namespace py = pybind11;

// PYBIND11_MODULE(python_example, m) {
//     m.doc() = R"pbdoc(
//         Pybind11 example plugin
//         -----------------------

//         .. currentmodule:: python_example

//         .. autosummary::
//            :toctree: _generate

//            add
//            subtract
//     )pbdoc";

//     m.def("add", &add, R"pbdoc(
//         Add two numbers

//         Some other explanation about the add function.
//     )pbdoc");

//     m.def("subtract", [](int i, int j) { return i - j; }, R"pbdoc(
//         Subtract two numbers

//         Some other explanation about the subtract function.
//     )pbdoc");

// #ifdef VERSION_INFO
//     m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
// #else
//     m.attr("__version__") = "dev";
// #endif
// }


