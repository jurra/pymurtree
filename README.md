# PyMurTree 
> DISCLAIMER: This codebase is currently in alpha version, meaning that the main branch version is made available for testing mainly by project members. Please note that this codebase is still under development and may contain bugs or errors. Users are advised to exercise caution when using this codebase and to report any issues or feedback to the developers so they can be addressed in future releases.


PyMurTree is a Python wrapper for the [MurTree project](https://github.com/DCC/murtree). The MurTree algorithm constructs optimal classification trees that minimize the misclassification score of a given dataset while respecting constraints on depth and number of feature nodes. The sparse objective, which penalizes each node added in the tree, is also supported.

Details about the algorithm can be found in the paper:
"MurTree: Optimal Decision Trees via Dynamic Programming and Search" by Emir Demirović, Anna Lukina, Emmanuel Hebrard, Jeffrey Chan, James Bailey, Christopher Leckie, Kotagiri Ramamohanarao, and Peter J. Stuckey, Journal of Machine Learning Research (JMLR), 2022. Available online at https://jmlr.org/papers/v23/20-520.html


## Installation

Before attempting to install pymurtree, make sure your system has the following software available: Python version 3.7 or higher and pip.

### Install from source using `pip`

```bash
git clone https://github.com/MurTree/pymurtree.git
cd pymurtree

# Optional: build pymurtree within a virtual environment
# python3 --version # check your python version
# sudo apt install python<your_python_version>-venv
# python3 -m venv env
# . env/bin/activate
 
# Install
pip install . 

# To install the dev version:
# pip install .[dev] 
```

### Building and running the tests

For building and running the tests, you will need the following software: pytest, a C++ compiler, and CMake version 3.14 or higher.

```bash
# Run the Python tests
pytest

# Run the C++ tests
cd tests/cpptests
mkdir build
cd build
cmake ..
make
ctest
```

## Usage
After installing the package, you can use it in your Python code by importing pymurtree. Here's an example of how to load data, fit an optimal decision tree classifier, and predict on new data:

```python
import pymurtree

(X, Y) = pymurtree.load_data("./tests/fixtures/test_dataset.txt")
model = pymurtree.OptimalDecisionTreeClassifier(max_depth=4)
model.fit(X, Y) 
Y_pred = model.predict(X)
```
The fit method takes the training data X and Y as inputs, where X is the feature matrix and Y is the label vector. The predict method takes a new feature matrix as input and returns the predicted labels.

You can also pass additional parameters to the fit method, such as max_num_nodes, which constrains the maximum number of nodes in the tree:

```python	
model.fit(X, Y, max_num_nodes=13)
Y_pred2 = model.predict(X)

```

