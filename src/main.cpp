#include <pybind11/pybind11.h>

// #include "code/MurTree/Engine/solver.h"
// #include "code/MurTree/Engine/dataset_cache.h"
// #include "code/MurTree/Engine/hyper_parameter_tuner.h"
// #include "code/MurTree/Utilities/parameter_handler.h"
// #include "code/MurTree/Utilities/stopwatch.h"

// #include <iostream>
// #include <fstream>
// #include <vector>
// #include <string>
// #include <time.h>
// #include <algorithm>


#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

int add(int i, int j) {
    return i + j;
}

namespace py = pybind11;

PYBIND11_MODULE(python_example, m) {
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------

        .. currentmodule:: python_example

        .. autosummary::
           :toctree: _generate

           add
           subtract
    )pbdoc";

    m.def("add", &add, R"pbdoc(
        Add two numbers

        Some other explanation about the add function.
    )pbdoc");

    m.def("subtract", [](int i, int j) { return i - j; }, R"pbdoc(
        Subtract two numbers

        Some other explanation about the subtract function.
    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}