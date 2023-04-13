
# Here we test the parameter handler using pytest
# Path: tests\test_murtree.py

import sys
from pymurtree import ParameterHandler


# TESTING THE PARAMETER HANDLER
def test_define_category():
    handler = ParameterHandler()
    try:
        handler.define_new_category("category1")
    except:
        pass

    handler.define_new_category("category1", "category1")

def test_define_float_parameter():
    handler = ParameterHandler()
    handler.define_new_category("Main Parameters", "Main Parameters")
    handler.define_float_parameter("time", 
                                   "Maximum runtime given in seconds",
                                   600, # default value
                                   "Main Parameters",
                                   0, # min value
                                   1000000) # max value

def test_define_string_parameter():
    handler = ParameterHandler()
    handler.define_new_category("Main Parameters", "Main Parameters")
    handler.define_string_parameter("file", "Location to the dataset.", "", "Main Parameters")

def test_define_integer_parameter():
    handler = ParameterHandler()
    handler.define_new_category("Algorithmic Parameters", "Algorithmic Parameters")
    handler.define_integer_parameter("upper-bound", 
                                     "Initial upper bound.", 
                                     1000000, 
                                     "Algorithmic Parameters", 
                                     0, 
                                     1000000)

def test_define_boolean_parameter():
    handler = ParameterHandler()
    handler.define_new_category("Main Parameters", "Main Parameters")
    handler.define_boolean_parameter("hyper-parameter-tuning", 
                                     "Activate hyper-parameter tuning using max-depth and max-num-nodes as the maximum values allowed. The splits need to be provided in the appropriate folder...see the code. todo", 
                                     False, 
                                     "Main Parameters")