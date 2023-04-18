''' 
The wrapper class for the murtree solver

WARNING: This is a work in progress and is not yet ready for use, they are just
notes on how to implement the python interface


Here we defined all the methods the user can call to interact with the solver
Pybind python code will be private and not exposed to the user
'''
import pymurtree # This is the pybind11 module 
# it could be called _pymurtree since the code should be private

class PyMurTree:
    @property
    def parameters(self):
        '''
        Store parameters as a property in a dictionary
        how to declare properties in python
        https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters

        '''
        return self._parameters

    # OptimaDecisonTreeClassifier is a patch method that initializes the python object
    def optimal_decision_tree_classifier(self, max_depth=4, **kwargs): # This is in practice an init function to hold parameters to then call a constructor
        '''This function doesnt build the model, it just initializes the python object
        We pass and store parameters that the parameter handler handles
        When user calls fit, we pass the parameters to the solver constructor to then initialize the solver object binded with pybind11

        Parameters
        ----------
        max_depth : int, optional (default=4)
            The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.
        other parameters : dict, optional

        Returns
        -------
        self : object
            The object is a model instance...
        
        '''
        
        # Here we take all parameters that the parameter handler handles and store them in the python object
        if max_depth is not None:
            self.parameters['max_depth'] = max_depth

        return self
    
    def _solve():
        '''
        A private method that can be used for fit and predict
        Here we call the C++ function that does the heavy lifting
        Here we tell the solver to solve
        '''

        pass 


    def fit(self, X, Y, **kwargs):
        '''Fit the model to the data
        When user passes data supposed to be read with pandas or numpy, 
        we convert it to a C++ vector of vectors of FeatureVectorBinary 

        then we call the constructor of the solver class
        the model is modified 

        Parameters
        ----------
        X : array-like, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples and
            n_features is the number of features.
        Y : array-like, shape = [n_samples]

        kwargs : dict my contain parameters to be passed to the solver
        
        Returns
        -------
        self : object
        
        
        '''
        # If parameters in kwargs then update the parameters
        if 'parameters' in kwargs:
            # update parameters with new parameters
            pass
            self.parameters.update(kwargs['parameters']) # How do we update the parameters in the python object?

        # Call **new** c++ functions:
        #   1) Function that takes Python array/matrix and creates a std::vector<std::vector<FeatureVectorBinary>>

        # Here we call the C++ function that does the heavy lifting
         # instantiates the solver from pybind11 with the parameters

        # This can only be called once
        model = self.Solve(self.parameters)  # here we instantiate the solver, this is when the constructor is called...
        self._solve(model)

    def predict(self, X):
        # Here we call the C++ function that does the heavy lifting
        # instantiates the solver from pybind11 with the parameters
        self._solve()

    def get_score():
        '''Returns the score of the model '''
        pass

    def get_misclassification():
        '''Returns the misclassification of the model'''
        pass