import numpy as np

def one_hot_encoding(arr: np.ndarray) -> np.ndarray:
    if arr.ndim != 1:
        raise ValueError(f"The function can work for 1D matrices, not {arr.ndim}D")

    unique_values = np.unique(arr)

    encoding_result = np.zeros((arr.size, unique_values.size), dtype=float)

    for i, value in enumerate(arr):
        index = np.where(unique_values == value)[0][0]
        encoding_result[i, index] = 1.0

    return encoding_result


