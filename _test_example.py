from pymurtree import lib
import pymurtree as mrt
import numpy as np
import pandas
from pymurtree.readdata import read_from_file

x, y = read_from_file("_no_iris_categorical.txt")
x = x.to_numpy()
y = y.to_numpy()

# -max-depth 4 -max-num-nodes 15 -time 600
model = mrt.OptimalDecisionTreeClassifier(max_depth=4, max_num_nodes=15, time=600)
result = model.fit(x, y)
print(model.score())

predicted = model.predict_cpp(x)

# Turn the code from line 15 to 26 into a foor loop considering x as input
for i in range(0, len(x), 10):
    print("Next 10 samples of iris_categorical_bin.txt")
    print(model.predict_cpp(x[i:i+10]))
    print("--------------------")


print("Test that doesnt work in pytest")

data = np.array([   [1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 1, 0, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 1, 0, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 1, 0, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 0, 1, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 1, 0, 0, 1, 0, 0 , 1, 0, 0 ],
                    [1, 0, 0, 0, 1, 0, 1, 0, 0 , 1, 0, 0 ]
                    ]).astype(np.int32)

expected_prediction = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

prediction = model.predict_cpp(data)
# assert np.array_equal(prediction, expected_prediction)

assert (x[0:10] == data).all()
print("data is equal to x[0:10]")

assert (model.predict(x[0:10]) == model.predict_cpp(data)).all()
print("model.predict(x[0:10]) is equal to model.predict_cpp(data)")

assert (model.predict(x[0:10]) == expected_prediction).all()
print("model.predict(x[0:10]) is equal to expected_prediction")










