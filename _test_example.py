from pymurtree import lib
import pymurtree as mrt
import numpy as np
import pandas

def read_data(path: str, pass_arr: bool=True) -> np.ndarray:
        """
        Reads data from a space-separated text file with the following format:
        The first column contains the target variable (y), and the remaining columns 
        contain the features (x).

        Args:
            path (str): The path to the text file.

        Returns:
            tuple: A tuple containing x (a pandas DataFrame with all columns except the first) 
            and y (a pandas Series representing the first column).
        """
        data = pandas.read_csv(path, sep=' ', header=None)
        # drop the first index column
        # How can I convert the pandas dataframe to numpy?
        # https://stackoverflow.com/questions/13187778/convert-pandas-dataframe-to-numpy-array
        data = data.iloc[:, 1:].to_numpy().astype(np.int32)

        if pass_arr:
            return data
        
        else:
            x = data[:, 1:]
            y = data[:, 0]
        return x, y

x, y = read_data("_no_anneal.txt", pass_arr=False)
my_first_array = np.concatenate((y.reshape(-1,1), x), axis=1)
my_second_array = read_data("_no_anneal.txt", pass_arr=True)

print(type(my_first_array) == type(my_second_array))
print(np.shape(my_first_array) == np.shape(my_second_array))
print(my_first_array == my_second_array)

# data = read_data("_no_anneal.txt")

model = mrt.OptimalDecisionTreeClassifier()
# model.fit(data, duplicate_factor=2)
model.fit(x, y, duplicate_factor=2)

# v = lib.read_data(data.astype(np.int32),2)
# # v = lib.numpy_to_vector(data.astype(np.int32))
# print(v)

