import pandas as pd
import numpy as np
import os

from . import lib
from pymurtree.parameters import Parameters

class OptimalDecisionTreeClassifier:
    def __init__(self,
                 time: int = 600,
                 max_depth: int = 3,
                 max_num_nodes: int = 7,
                 sparse_coefficient: float = 0.0,
                 verbose: bool = True,
                 all_trees: bool = True,
                 incremental_frequency: bool = True,
                 similarity_lower_bound: bool = True,
                 node_selection: int = 0,
                 feature_ordering: int = 0,
                 random_seed: int = 3,
                 cache_type: int = 0,
                 duplicate_factor: int = 1
                ) -> None:

        self.__solver = None
        self.__tree = None

        self.__params = Parameters(time, max_depth, max_num_nodes,
                                   sparse_coefficient, verbose,
                                   all_trees, incremental_frequency, 
                                   similarity_lower_bound, node_selection,
                                   feature_ordering, random_seed,
                                   cache_type, duplicate_factor)
    
    def write_data_to_file(X, Y, output_file):
        '''Write data to txt file.
        Parameters
        ----------
        X : pandas.DataFrame
            The features of the dataset.
        Y : pandas.Series
            The labels of the dataset.
        output_file : str
            The path to the output file.
        '''
        X = X.astype(np.uint8)

        # binarize non-binary features
        # you can use your own binarization script here
        X_bin = pd.DataFrame(np.unpackbits(X.to_numpy(), axis=1), columns=[f'feature_{i}' for i in range(X.shape[1]*8)])

        # concatenate the binarized features and the label into a single dataframe
        df = pd.concat([Y.reset_index(drop=True), X_bin.reset_index(drop=True)], axis=1)

        # write the dataframe to a csv file
        df.to_csv(output_file, index=False, header=False, sep=" ")

    def fit(self,
            x, y,
            time: int = None,
            max_depth: int = None,
            max_num_nodes: int = None,
            sparse_coefficient: float = None,
            verbose: bool = None,
            all_trees: bool = None,
            incremental_frequency: bool = None,
            similarity_lower_bound: bool = None,
            node_selection: int = None,
            feature_ordering: int = None,
            random_seed: int = None,
            cache_type: int = None,
            duplicate_factor: int = None) -> None:
        
        if time is not None:
            self.__params.time = time
        if max_depth is not None:
            self.__params.max_depth = max_depth
        if max_num_nodes is not None:
            self.__params.max_num_nodes = max_num_nodes
        if sparse_coefficient is not None:
            self.__params.sparse_coefficient = sparse_coefficient
        if verbose is not None:
            self.__params.verbose = verbose
        if all_trees is not None:
            self.__params.all_trees = all_trees
        if incremental_frequency is not None:
            self.__params.incremental_frequency = incremental_frequency
        if similarity_lower_bound is not None:
            self.__params.similarity_lower_bound = similarity_lower_bound
        if node_selection is not None:
            self.__params.node_selection = node_selection
        if feature_ordering is not None:
            self.__params.feature_ordering = feature_ordering
        if random_seed is not None:
            self.__params.random_seed = random_seed
        if cache_type is not None:
            self.__params.cache_type = cache_type
        if duplicate_factor is not None:
            self.__params.duplicate_factor = duplicate_factor

        # If ./pymurtree_data directory does not exist, create it
        if not os.path.exists('./pymurtree_data'):
            os.makedirs('./pymurtree_data')
        
        # Write data to txt file before calling the constructor
        self.write_data_to_file(x, y, './pymurtree_data/data.txt')

        # Initialize solver (call cpp Solver class constructor)
        if self.__solver is None:
            self.__solver = lib.Solver(self.__params.time,
                                       self.__params.max_depth,
                                       self.__params.max_num_nodes,
                                       self.__params.sparse_coefficient,
                                       self.__params.verbose,
                                       self.__params.all_trees,
                                       self.__params.incremental_frequency,
                                       self.__params.similarity_lower_bound,
                                       self.__params.node_selection,
                                       self.__params.feature_ordering,
                                       self.__params.random_seed,
                                       self.__params.cache_type,
                                       self.__params.duplicate_factor)
        
        # Create the tree that will be used for predictions
        # (call cpp Solver::Solve method)
        self.__tree = self.__solver.solve(self.__params.time,
                                          self.__params.max_depth,
                                          self.__params.max_num_nodes,
                                          self.__params.sparse_coefficient,
                                          self.__params.verbose,
                                          self.__params.all_trees,
                                          self.__params.incremental_frequency,
                                          self.__params.similarity_lower_bound,
                                          self.__params.node_selection,
                                          self.__params.feature_ordering,
                                          self.__params.random_seed,
                                          self.__params.cache_type,
                                          self.__params.duplicate_factor)

    def predict(self):
        pass


    def score(self) -> int:
        return self.__tree.misclassification_score()

    def depth(self) -> int:
        return self.__tree.tree_depth()

    def num_nodes(self) -> int:
        return self.__tree.tree_nodes()
