'''
Decription of test cases for readdata.py as user stories and acceptance criteria

Story: As a user I want to read data from a file so that I can use it for training and testing
AC: The file is written in DL format see the readme for details
AC: The file is read and converted to a numpy array  (x, y) where x is the feature vectors and y is the labels
AC: Features are binary values and labels are integers
'''
import pytest
import pandas as pd
import numpy as np
from pymurtree.readdata import read_from_file
import pymurtree.lib as lib
import pprint

TRAIN_DATA = "./tests/fixtures/test_dataset.txt"

@pytest.fixture
def dl_from_file() -> np.ndarray:
    ''' Read data from DL formatted file and return as numpy array'''
    x, y = read_from_file(TRAIN_DATA)
    x = x.to_numpy()
    y = y.to_numpy()
    return np.concatenate((y.reshape(-1,1), x), axis=1).astype(np.int32)

@pytest.fixture
def dl_x_y() -> tuple:
    ''' Read data from DL formatted file and return as tuple with two numpy arrays 
    (x, y) where x is the feature vectors and y is the labels'''
    x, y = read_from_file(TRAIN_DATA)
    return x, y

@pytest.fixture
def dl_data_sample() -> np.ndarray:

    return np.array([[1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
                    ]).astype(np.int32)
                    

# test that data read is correct
def test_read_from_file():
    x, y = read_from_file(TRAIN_DATA)
    assert x is not None
    assert y is not None
    assert type(x) == pd.core.frame.DataFrame
    assert type(y) == pd.core.series.Series
    
def test_compare_feature_vectors(dl_from_file):
    ''' Test that we get exactly the same feature vectors from the file and from the numpy array'''
    feature_vectors_from_file = lib._read_data_dl(TRAIN_DATA, 1)
    assert feature_vectors_from_file is not None
    assert type(feature_vectors_from_file) == list
    assert type(feature_vectors_from_file[0]== lib.FeatureVectorBinary)

    feature_vectors = lib._nparray_to_feature_vectors(dl_from_file, 1)
    assert len(feature_vectors[0]) == len(feature_vectors_from_file[0])
    assert len(feature_vectors) == len(feature_vectors_from_file)