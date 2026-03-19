import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(lst).reshape(3, 3)

    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    }

    return calculations

"""
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
"""
