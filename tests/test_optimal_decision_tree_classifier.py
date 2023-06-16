'''
For predict we use only 10 samples of iris_categorical_bin.txt which can be found
and downloaded here: https://github.com/MurTree/murtree-data/blob/main/NL/iris_categorical_bin.txt
'''

import pytest
import numpy as np
from src.pymurtree import read_from_file
import pymurtree

TRAIN_DATA = "./tests/fixtures/test_dataset.txt"
EXPECTED_PREDICT_OUTPUT = "./tests/fixtures/expected_predict_output.txt"

# Define a fixture for input data with known output values
@pytest.fixture
def train_data():
    x, y = read_from_file(TRAIN_DATA)
    x = x.to_numpy()
    y = y.to_numpy()
    return x, y

@pytest.fixture
def x_train_data(train_data):
    return train_data[0]

@pytest.fixture
def y_train_data(train_data):
    return train_data[1]

# Define a fixture for the decision tree
@pytest.fixture
def decision_tree(x_train_data, y_train_data):
    decision_tree = pymurtree.OptimalDecisionTreeClassifier(max_depth=4, duplicate_factor=1, max_num_nodes=15)
    decision_tree.fit(x_train_data, y_train_data)
    return decision_tree

@pytest.fixture
def invalid_input():
    # Define input data with invalid values
    # ...
    # make a numpy arrau where features are not 0 or 1
    return np.array([   [1, 0, 0, 0, 0, 1, 1, 0, 3 , 1, 0, 0 ],
                        [1, 0, 0, 0, 1, 0, 1, 0, 0 , 1, 0, 0 ],
                        [1, 0, 0, 0, 1, 0, 1, 0, 0 , 1, 0, 0 ],
                        [1, 0, 0, 0, 1, 0, 1, 4, 0 , 1, 0, 0 ],
                        [1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                        [1, 0, 0, 0, 0, 1, 1, 5, 0 , 1, 0, 0 ],
                        [1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                        [1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                        [1, 0, 0, 1, 0, 0, 1, 0, 0 , 1, 0, 0 ],
                        [1, 0, 0, 0, 1, 0, 1, 0, 0 , 1, 0, 0 ]
                        ])

# Define a fixture for output values that are expected to be predicted by the decision tree
@pytest.fixture
def expected_fit_output(decision_tree, expected_predict_output):
    # Define output values that are expected to be predicted by the decision tree
    # ...
    # make it a numpy array from anneal.txt
    # This we do from generating the model with cpp library
    # then classifying it and storing it in a 1d array
    pass

@pytest.fixture
def expected_predict_output():
    return np.loadtxt(EXPECTED_PREDICT_OUTPUT, dtype=np.int32)


def test_predict(decision_tree, x_train_data, expected_predict_output):
    predict_output = decision_tree.predict(x_train_data)
    # check that predict_output is a numpy array
    print(predict_output)
    print(type(predict_output))
    assert predict_output is not None
    assert isinstance(predict_output, np.ndarray)
    assert (predict_output == expected_predict_output).all()

def test_predict_empty_input(decision_tree):
    # Ensure that an error or exception is raised when no input data is provided
    with pytest.raises(Exception):
        decision_tree._predict([])

def test_predict_invalid_input(decision_tree):
    # Ensure that an error or exception is raised when invalid input data is provided
    # ...
    with pytest.raises(Exception):
        decision_tree._predict(invalid_input)
