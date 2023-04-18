# Issues to address
## Psuedo code reference
```python
import murtree

(X, Y) = murtree.ReadData("anneal.txt")
model = murtree.OptimalDecisionTreeClassifier(max_depth=4) #this would call the constructor "Solver(ParameterHandle&)" in C++ https://bitbucket.org/EmirD/murtree/src/163364e8c50e5f2505524de917a59ebf38bdac65/code/MurTree/Engine/solver.h#lines-24.
model.fit(X, Y) # this would call the C++ "Solve" https://bitbucket.org/EmirD/murtree/src/163364e8c50e5f2505524de917a59ebf38bdac65/main.cpp#lines-362
Y_pred = model.predict(Y)

and later on the user could write

model.fit(X, Y, num_nodes=13) #notice the parameter being passed that was not there before
Y_pred2 = model.predict(Y) #this call should be shorter given that .predict was called above already

```
- The python model wrapps the pybind methods into a sklearn like interface
- `src/main.cpp` Convert data from python to cpp in wrapper code.
- When calling `optimal_decision_tree_classifier` the pybinded Solver constructor must not be called, instead we just hold the paramters, this is patch or mock to deal with current limitations
- In cpp when calling the solver constructor we need the option to not read data from file. Instead we add an optional argument to the constructor that takes in the data. Inside the constructor, we check if the data was passed (ie data not nullopt), if so we do not read the data from file.
- How do we hold features data when we call the model again like so in python: `Y_pred2 = model.predict(Y)`
    - Check if Solver::Solve can operate with just the features and not labels

- If authors intend to reuse sklean predict function the we would have to pass a tree model from cpp to python and translate so that they are interoperable. Is this is the case?

- Ask researchers if they have a script that serealized the tree that is the output of MurTree.