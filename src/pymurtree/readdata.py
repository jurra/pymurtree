import pandas
import numpy

def read_from_file(path: str) -> tuple:
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
        y = data.iloc[:, 0]
        x = data.iloc[:, 1:]
        return x, y


def load_data(path: str) -> tuple:
        """
        Reads data from a space-separated text file with the following format:
        The first column contains the target variable (y), and the remaining columns 
        contain the features (x).

        Args:
            path (str): The path to the text file.

        Returns:
            tuple: A tuple containing:
              x (numpy.ndarray): 2D array with all columns except the first 
              y (numpy.ndarray): 1D array with the first column
        """
        data = numpy.loadtxt(path, dtype=int, delimiter=' ')
        x = data[:, 1:]
        y = data[:, 0]
        return x, y