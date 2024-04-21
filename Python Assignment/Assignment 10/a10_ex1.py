import numpy as np
import numbers

def extend(arr: np.ndarray, rows: int, cols: int, fill=None) -> np.ndarray:
    if arr.ndim != 2:
        raise ValueError(f"can only extend 2D arrays, not {arr.ndim}D")

    if rows < arr.shape[0]:
        raise ValueError("invalid rows")

    if cols < arr.shape[1]:
        raise ValueError("invalid cols")

    if fill is not None and not isinstance(fill, numbers.Number):
        raise ValueError("invalid fill")

    extended_arr = np.empty_like(arr)

    extended_arr[:arr.shape[0], :arr.shape[1]] = arr

    if rows > arr.shape[0]:
        if fill is None:
            row_means = np.mean(arr, axis=1)
            extended_arr[arr.shape[0]:rows, :] = row_means[:, None]
        else:
            extended_arr[arr.shape[0]:rows, :] = fill

    if cols > arr.shape[1]:
        if fill is None:
            col_means = np.mean(arr, axis=0)
            extended_arr[:, arr.shape[1]:cols] = col_means[None, :]
        else:
            extended_arr[:, arr.shape[1]:cols] = fill

    if rows > arr.shape[0] and cols > arr.shape[1]:
        if fill is None:
            overall_mean = np.mean(arr)
            extended_arr[arr.shape[0]:rows, arr.shape[1]:cols] = overall_mean
        else:
            extended_arr[arr.shape[0]:rows, arr.shape[1]:cols] = fill

    return extended_arr
