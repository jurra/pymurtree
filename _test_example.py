from pymurtree import lib
import pymurtree as mrt
import numpy as np
import pandas

def read_data(path: str) -> np.ndarray:
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
        data = data.iloc[:, 1:].to_numpy()
        return data

data = read_data("_no_anneal.txt")

print(data)

model = mrt.OptimalDecisionTreeClassifier()
model.fit(data.astype(np.int32))

# v = lib.read_data(data.astype(np.int32),2)
# # v = lib.numpy_to_vector(data.astype(np.int32))
# print(v)

