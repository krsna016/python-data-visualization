import pytest
import pandas as pd
import numpy as np

def test_pandas_dataframe_vectorization():
    # Demonstrating testing of fundamental data structures
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    
    # Assert vectorization mechanics
    df['C'] = df['A'] + df['B']
    assert df['C'].tolist() == [5, 7, 9]

def test_numpy_matrix_operations():
    # Demonstrating testing of mathematical assertions
    matrix = np.array([[1, 2], [3, 4]])
    transposed = matrix.T
    
    assert transposed[0][1] == 3
    assert transposed[1][0] == 2
