import numpy as np

def eigen_finder(matrix):
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return []
    

    
    return list(np.linalg.eigvals(matrix))

def frobenious_norm_finder(matrix):
    return float(np.linalg.norm(matrix, 'fro'))

def infinity_norm_finder(matrix):
    return float(np.linalg.norm(matrix, np.inf))

def min_max_normalizer(matrix):
    min_val = np.min(matrix)
    max_val = np.max(matrix)
    if min_val == max_val:
        return np.full(matrix.shape, 0.5)
    return (matrix - min_val) / (max_val - min_val)