from dataclasses import dataclass

@dataclass
class Parameters:

    # Maximum runtime given in seconds
    time: int
    
    # Maximum allowed depth of the tree, where the depth is defined as the
    # largest number of *decision/feature nodes* from the root to any leaf.
    # Depth greater than four is usually time consuming."
    max_depth: int

    # Maximum number of *decision/feature nodes* allowed.
    # Note that a tree with k feature nodes has k+1 leaf nodes.
    max_num_nodes: int

    # Assigns the penalty for using decision/feature nodes.
    # Large sparse coefficients will result in smaller trees.
    sparse_coefficient: float

    # Determines if the solver should print logging information to the standard
    # output.
    verbose: bool

    # Instructs the algorithm to compute trees using all allowed combinations
    # of max-depth and max-num-nodes. Used to stress-test the algorithm.
    all_trees: bool

    # Activate incremental frequency computation, which takes into account
    # previously computed trees when recomputing the frequency.
    # In our experiments proved to be effective on all datasets.
    incremental_frequency: bool

    # Activate similarity-based lower bounding. Disabling this option may be 
    # better for some benchmarks, but on most of our tested datasets keeping
    # this on was beneficial.
    similarity_lower_bound: bool

    # Node selection strategy used to decide on whether the algorithm should
    # examine the left or right child node first.
    #   0 = dynamic
    #   1 = post-order
    node_selection: int

    # Feature ordering strategy used to determine the order in which features
    # will be inspected in each node.
    #   0 = in-order
    #   1 = random
    #   2 = gini
    feature_ordering: int

    # Random seed used only if the feature-ordering is set to random.
    # A seed of -1 assings the seed based on the current time.
    random_seed: int

    # Cache type used to store computed subtrees.
    # 'Dataset' is more powerful than 'branch' but may required more 
    # computational time. Needs to be determined experimentally.
    # 'Closure' is experimental and typically slower than other options.
    #   0 = dataset
    #   1 = branch
    #   2 = closure
    cache_type: int

    # Duplicates the instances the given amount of times.
    # Used for stress-testing the algorithm, not a practical parameter.
    duplicate_factor: int

    # Initial upper bound.
    # TO-DO
