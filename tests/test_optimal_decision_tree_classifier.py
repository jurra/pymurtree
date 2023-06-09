'''
For predict we use only 10 samples of iris_categorical_bin.txt which can be found
and downloaded here: https://github.com/MurTree/murtree-data/blob/main/NL/iris_categorical_bin.txt
'''

import pytest
import numpy as np
from src.pymurtree import read_from_file
import pymurtree

# Define a fixture for input data with known output values
@pytest.fixture
def input_data():
    # Define input data with known output values
    # ...
    # anneal text imported from readdata.py
    x, y = read_from_file("_no_iris_categorical.txt")
    x = x.to_numpy()
    y = y.to_numpy()
    return x, y

@pytest.fixture
def x_train_data():
    x, y = read_from_file("_no_iris_categorical.txt")
    x = x.to_numpy()
    return x

@pytest.fixture
def y_train_data():
    x, y = read_from_file("_no_iris_categorical.txt")
    y = y.to_numpy()
    return y

# Define a fixture for the decision tree
@pytest.fixture
def decision_tree(x_train_data, y_train_data):
    # Define the structure of your decision tree
    # ...
    # Define the data used by your decision tree
    # ...
    decision_tree = pymurtree.OptimalDecisionTreeClassifier(max_depth=4, duplicate_factor=1, max_num_nodes=15)
    decision_tree.fit(x_train_data, y_train_data)
    return decision_tree

@pytest.fixture
def x_test_data():
    ''' These are the first 10 samples of iris_categorical_bin.txt
    '''
    # The code bellow must be a numpy array
    return np.array([[1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 1, 0, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 1, 0, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 1, 0, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 1, 0, 0, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 1, 0, 1, 0, 0 , 1, 0, 0 ]
                    ]).astype(np.int32)
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
    '''This is the expected classification of the first 10 samples of iris_categorical_bin.txt
    We get this from the cpp library and use it to test our python library'''
    return np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def _test_predict_all_correct(decision_tree, x_test_data, y_test_data, expected_fit_output):
    # Ensure that the decision tree predicts the correct output values for all input data
    # ...
    # predicted_output = decision_tree.predict(x_test_data)
    # assert predicted_output == expected_fit_output
    pass

# Define the test functions
def test_predict_all_correct(decision_tree, x_test_data, expected_predict_output):
    # Ensure that the decision tree predicts the correct output values for all input data
    # ...
    predict_output = decision_tree.predict(x_test_data[0:10]) # We do this because our train data is only 10 samples
    assert (predict_output == expected_predict_output).all()

def test_predict_some_incorrect(decision_tree, input_data):
    # Ensure that the decision tree predicts the correct output values for some input data,
    # but incorrect output values for others
    # ...
    # assert predicted_output == expected_output
    pass

def test_predict_empty_input(decision_tree):
    # Ensure that an error or exception is raised when no input data is provided
    # ...
    # with pytest.raises(Exception):
    #     decision_tree.predict([])
    pass

def test_predict_invalid_input(decision_tree):
    # Ensure that an error or exception is raised when invalid input data is provided
    # ...
    # with pytest.raises(Exception):
    #     decision_tree.predict(invalid_input)
    pass

def test_predict_missing_features(decision_tree):
    # Ensure that an error or exception is raised when input data is missing features that
    # are required by the decision tree
    # ...
    # with pytest.raises(Exception):
    #     decision_tree.predict(missing_features)
    pass
