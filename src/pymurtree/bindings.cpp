#include <pybind11/pybind11.h>

int add(int a, int b) {
    return a+b;
};

PYBIND11_MODULE(lib, m){
    m.doc() = "Python wrapper for MurTree";
    m.def("py_add", &add);
}