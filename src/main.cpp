//Distributed under the MIT license, see License.txt
//Copyright © 2022 Emir Demirović

//Code for the paper: 
// "MurTree: optimal classification trees via dynamic programming and search", JMLR, 2022.
//  Note that some of the comments directly refer to the paper:
// 
//Authors: Emir Demirović, Anna Lukina, Emmanuel Hebrard, Jeffrey Chan, James Bailey, Christopher Leckie, Kotagiri Ramamohanarao, Peter J. Stuckey
//For any issues related to the code, please feel free to contact Dr Emir Demirović, e.demirovic@tudelft.nl

#include "../murtree/code/MurTree/Engine/solver.h"
#include "../murtree/code/MurTree/Engine/dataset_cache.h"
#include "../murtree/code/MurTree/Engine/hyper_parameter_tuner.h"
#include "../murtree/code/MurTree/Utilities/parameter_handler.h"
#include "../murtree/code/MurTree/Utilities/stopwatch.h"
// #include "../murtree/code/murtree.h

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <time.h>
#include <algorithm>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <pybind11/chrono.h>
#include <pybind11/functional.h>

namespace py = pybind11;
using namespace MurTree;

PYBIND11_MODULE(pymurtree, m){
	py::class_<ParameterHandler> parameter_handler(m, "ParameterHandler");
    // parameter_handler.def(py::init<>())
    parameter_handler.def(py::init([](){ return new ParameterHandler(); })
    , py::keep_alive<0, 1>()
    )
                     .def("define_new_category", &ParameterHandler::DefineNewCategory)
                     .def("define_string_parameter", &ParameterHandler::DefineStringParameter)
                     .def("define_integer_parameter", &ParameterHandler::DefineIntegerParameter)
                     .def("define_float_parameter", &ParameterHandler::DefineFloatParameter)
                     .def("define_boolean_parameter", &ParameterHandler::DefineBooleanParameter);
}

