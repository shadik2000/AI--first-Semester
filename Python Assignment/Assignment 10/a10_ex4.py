import numpy as np

def moving_average_2D(arr: np.ndarray, size: int) -> np.ndarray:
    # Check if arr is 2D
    if arr.ndim != 2:
        raise ValueError(f"apply for 2D array, not {arr.ndim}D")

    if not np.issubdtype(arr.dtype, np.number):
        raise TypeError("Invalid data type")

    if size < 1 or size > min(arr.shape):
        raise ValueError("Invalid window size")

    result_shape = (arr.shape[0] - size + 1, arr.shape[1] - size + 1)

    result = np.empty(result_shape, dtype=float)

    for i in range(result_shape[0]):
        for j in range(result_shape[1]):
            window = arr[i:i+size, j:j+size]
            result[i, j] = np.mean(window)

    return result


