
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
    

def test_np_to_vectors(dl_x_y):
    ''' Test that the numpy array is converted to a list of vectors'''

    x = dl_x_y[0].to_numpy().astype(np.int32)
    cpp_vectors = lib._nparray_to_vectors(x)

    assert cpp_vectors is not None
    assert type(cpp_vectors) == list
    assert len(cpp_vectors) == x.shape[0]
    assert type(cpp_vectors[0][0] == int)

def test_nparray_to_feature_vectors(dl_data_sample):
    ''' Test that the numpy array is converted to a list of feature vectors'''

    feature_vectors = lib._nparray_to_feature_vectors(dl_data_sample, 1)

    assert feature_vectors is not None
    assert type(feature_vectors) == list
    assert type(feature_vectors[0]== lib.FeatureVectorBinary)
    assert len(feature_vectors) == dl_data_sample.shape[0] - 1

def test_compare_feature_vectors(dl_from_file):
    ''' Test that we get exactly the same feature vectors from the file and from the numpy array'''
    feature_vectors_from_file = lib._read_data_dl(TRAIN_DATA, 1)
    assert feature_vectors_from_file is not None
    assert type(feature_vectors_from_file) == list
    assert type(feature_vectors_from_file[0]== lib.FeatureVectorBinary)

    feature_vectors = lib._nparray_to_feature_vectors(dl_from_file, 1)
    assert len(feature_vectors[0]) == len(feature_vectors_from_file[0])
    assert len(feature_vectors) == len(feature_vectors_from_file)











