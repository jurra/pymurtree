# Using the parameter handler as it is
import pymurtree as m

handler = m.ParameterHandler()

handler.define_new_category("Main Parameters", "Main Parameters")
handler.define_new_category("Algorithmic Parameters", "Algorithmic Parameters")
handler.define_new_category("Tuning Parameters", "Tuning Parameters")

handler.define_string_parameter("file", 
                                "Location to the dataset.", 
                                "_no_anneal.txt", # default value
                                "Main Parameters", [])

handler.define_float_parameter("time", 
                               "Maximum runtime given in seconds",
                                 600, # default value
                                "Main Parameters",
                                0, # min value
                                1000000) # max value

handler.define_integer_parameter("max-depth",
                                "Maximum allowed depth of the tree, where the depth is defined as the largest number of *decision/feature nodes* from the root to any leaf. Depth greater than four is usually time consuming.",
                                3, # default value
                                "Main Parameters",
                                0, # min value
                                20) # max value

handler.define_integer_parameter("max-num-nodes",
                                "Maximum number of *decision/feature nodes* allowed. Note that a tree with k feature nodes has k+1 leaf nodes.",
                                7, # default value
                                "Main Parameters",
                                0, # min value
                                20) # max value

handler.define_float_parameter("sparse-coefficient",
                               "Assigns the penalty for using decision/feature nodes. Large sparse coefficients will result in smaller trees.",
                                0.0, # default value
                                "Main Parameters",
                                0.0, # min value
                                1.0) # max value

handler.define_boolean_parameter("verbose",
                                    "Determines if the solver should print logging information to the standard output.",
                                    True, # default value
                                    "Main Parameters")

handler.define_boolean_parameter("all-trees",
                                    "Instructs the algorithm to compute trees using all allowed combinations of max-depth and max-num-nodes. Used to stress-test the algorithm.",
                                    False, # default value
                                    "Main Parameters")

handler.define_string_parameter("result-file",
                                "The results of the algorithm are printed in the provided file, using for simple benchmarking. The output file contains the runtime, misclassification score, and number of cache entries. Leave blank to avoid printing.",
                                "", # default value
                                "Main Parameters", [])


# 	Internal algorithmic parameters-----------

handler.define_boolean_parameter("incremental-frequency",
                                    "Activate incremental frequency computation, which takes into account previously computed trees when recomputing the frequency. In our experiments proved to be effective on all datasets.",
                                    True, # default value
                                    "Algorithmic Parameters")

handler.define_boolean_parameter("similarity-lower-bound",
                                    "Activate similarity-based lower bounding. Disabling this option may be better for some benchmarks, but on most of our tested datasets keeping this on was beneficial.",
                                    True, # default value
                                    "Algorithmic Parameters")

handler.define_string_parameter("node-selection",
                                "Node selection strategy used to decide on whether the algorithm should examine the left or right child node first.",
                                "dynamic", # default value
                                "Algorithmic Parameters", ["dynamic", "post-order"])

handler.define_string_parameter("feature-ordering",
                                "Feature ordering strategy used to determine the order in which features will be inspected in each node.",
                                "in-order", # default value
                                "Algorithmic Parameters", ["in-order", "random", "gini"])

handler.define_integer_parameter("random-seed",
                                 "Random seed used only if the feature-ordering is set to random. A seed of -1 assings the seed based on the current time.",
                                    3, # default value
                                "Algorithmic Parameters",
                                -1, # min value
                                1000000) # max value

handler.define_string_parameter("cache-type",
                                "Cache type used to store computed subtrees. \"Dataset\" is more powerful than \"branch\" but may required more computational time. Need to be determined experimentally. \"Closure\" is experimental and typically slower than other options.",
                                "dataset", # default value
                                "Algorithmic Parameters", ["branch", "dataset", "closure"])

   
handler.define_integer_parameter("duplicate-factor",
                                    "Duplicates the instances the given amount of times. Used for stress-testing the algorithm, not a practical parameter.",
                                    1, # default value
                                    "Algorithmic Parameters",
                                    1, # min value
                                    1000000) # max value

handler.define_integer_parameter("upper-bound",
                                    "Initial upper bound.",
                                    1000000000, # default value
                                    "Algorithmic Parameters",
                                    0, # min value
                                    1000000000) # max value


# 	//Tuning parameters
handler.define_boolean_parameter("hyper-parameter-tuning",
                                    "Activate hyper-parameter tuning using max-depth and max-num-nodes as the maximum values allowed. The splits need to be provided in the appropriate folder...see the code. todo",
                                    False, # default value
                                    "Tuning Parameters")

handler.define_string_parameter("hyper-parameter-stats-file",
                                "Location of the output file that contains information about the hyper-parameter procedure.",
                                "", # default value
                                "Tuning Parameters", [])

handler.define_string_parameter("hyper-parameter-splits-file",
                                "Location of the file that contains the splits used for hyper-parameter tuning.",
                                "", # default value
                                "Tuning Parameters", [])


