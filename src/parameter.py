from dataclasses import dataclass

@dataclass
class Parameter:
    name: str
    description: str
    value: any
    category: str
    min_value: any
    max_value: any
    type: any

    # These below should be dynamically generated.....
    # Or they should be easy to mutate
    string_params = ["file", "node_selection"] 
    float_params = ["time", "sparse_coefficient"]
    int_params = ["max_depth", "max_num_nodes", "feature_ordering", "random_seed", "cache_type", "duplicate_factor"]

    def __init__(self, 
                 name: str, 
                 **kwargs):
        
        self.name = name

        if 'description' in kwargs:
            self.description = kwargs["description"]
        if 'value' in kwargs:
            self.value = kwargs["value"]
        if 'category' in kwargs:
            self.category = kwargs["category"]
        if 'min_value' in kwargs:
            self.min_value = kwargs["min_value"]
        else:
            self.min_value = None
        if 'max_value' in kwargs:
            self.max_value = kwargs["max_value"]
        else:
            self.max_value = None
        
        if self.name in self.string_params:
            self.type = str
        elif self.name in self.float_params:
            self.type = float
        elif self.name in self.int_params:
            self.type = int
        else:
             raise ValueError(f"Parameter {name} not found in string_params, float_params, or int_params")


    