#include "parameter_handler.h"
#include "solver.h"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <pybind11/chrono.h>
#include <pybind11/functional.h>

namespace py = pybind11;
using namespace MurTree;

// convert array of two dimensions to vector of vectors in cpp

// convert numpy array to vector of vectors of vectors in cpp

PYBIND11_MODULE(lib, m){
	py::class_<ParameterHandler> parameter_handler(m, "ParameterHandler");
    parameter_handler.def(py::init([](){ return new ParameterHandler(); }), py::keep_alive<0, 1>())
                     .def("define_new_category", &ParameterHandler::DefineNewCategory)
                     .def("define_string_parameter", &ParameterHandler::DefineStringParameter)
                     .def("define_integer_parameter", &ParameterHandler::DefineIntegerParameter)
                     .def("define_float_parameter", &ParameterHandler::DefineFloatParameter)
                     .def("define_boolean_parameter", &ParameterHandler::DefineBooleanParameter);
    py::class_<Solver> solver(m, "Solver");
    solver.def(py::init([](ParameterHandler& parameter_handler){ 
        return new Solver(parameter_handler); }), py::keep_alive<0, 1>())
          .def("solve", &Solver::Solve);
}

