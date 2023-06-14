
# Here we test the parameter handler using pytest
# Path: tests\test_murtree.py
import sys
import pytest
# from pymurtree.lib import ParameterHandler
from pymurtree.lib import  _create_parameters

# Instantiate the parameter handler
# this is a fixture
@pytest.fixture
def handler():
    return _create_parameters(
    time=600,
    max_depth=10,
    max_num_nodes=100,
    sparse_coefficient=0.1,
    verbose=False,
    all_trees=0,
    incremental_frequency=0,
    similarity_lower_bound=0,
    node_selection=3,
    feature_ordering=2,
    random_seed=0,
    cache_type=0,
    duplicate_factor=1)

# Assert that handler is instance of pymurtree.lib.ParameterHandler
def test_handler_instantiation(handler):
    assert isinstance(handler, object)
