import pymurtree
from parameter import Parameter

class MurTree:
    def __init__(self, **kwargs):
        '''
        example:
        >>> from pymurtree import MurTree
        >>> murtree = MurTree(time=600, max_depth=3, 
                            max_num_nodes=7, sparse_coefficient=0.0, 
                            verbose=True, all_trees=True, incremental_frequency=True, 
                            similarity_lower_bound=True, node_selection=0, feature_ordering=0, 
                            random_seed=3, cache_type=0, duplicate_factor=1)
        '''
        # DEFAULT PARAMETERS
        #FIXME: This is not working, we are supposed to set defualt parameters here,
        # So that we can then create a Parameter object for each of these defaults and then define them in the ParameterHandler
        self.parameters = {
            "time": kwargs.get("time", 600),
            "max_depth": kwargs.get("max_depth", 3),
            "max_num_nodes": kwargs.get("max_num_nodes", 7),
            "sparse_coefficient": kwargs.get("sparse_coefficient", 0.0),
            # "verbose": kwargs.get("verbose", True),
            "all_trees": kwargs.get("all_trees", True),
            "incremental_frequency": kwargs.get("incremental_frequency", True),
            "similarity_lower_bound": kwargs.get("similarity_lower_bound", True),
            "node_selection": kwargs.get("node_selection", 0),
            "feature_ordering": kwargs.get("feature_ordering", 0),
            "random_seed": kwargs.get("random_seed", 3),
            "cache_type": kwargs.get("cache_type", 0),
            "duplicate_factor": kwargs.get("duplicate_factor", 1)
        }

        self._parameters = pymurtree.ParameterHandler()
        self._parameters.define_new_category("Main Parameters", "Main Parameters")
        self._parameters.define_new_category("Algorithmic Parameters", "Algorithmic Parameters")
        self._parameters.define_new_category("Tuning Parameters", "Tuning Parameters")

        # We use our Parameter class to define types of parameters based on a list of parameters that have a certain type
        # Then with the type data extracted from the Parameter class, we can define the parameters in the ParameterHandler
        for key, value in kwargs.items():
            try: param = Parameter(name=key, value=value)
            except ValueError: raise 
            
            # FIXME: This is a hack, but it works for non, categories shouldn't be defined here
            if param.type == int:
                self._parameters.define_int_parameter(param.name, "", param.value, "Main Parameters") # FIXME: This is a hack, but it works for non, categories shouldn't be defined here
            
            elif param.type == float:
                self._parameters.define_float_parameter(param.name, "", param.value, "Main Parameters")
            
            elif param.type == str:
                self._parameters.define_string_parameter(param.name, "", param.value, "Main Parameters", [])


    def fit(self):
        # The right API should be fit(self, X, y)
        return pymurtree.Solver(self._parameters).solve()