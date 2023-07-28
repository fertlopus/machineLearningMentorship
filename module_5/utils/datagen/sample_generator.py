import numpy as np
import warnings


def generate_xy(n=500):
    """
    Generates random sample of X and y for linear regression problem.
    Used to quickly explore the in-depth work of linreg algo in terms
    of PyTorch using
    :param n: number of observations per X and y. Dtype: int
    :return: (X, Y) numpy arrays
    """
    warnings.filterwarnings("ignore")
    try:
        X = (np.random.random(n)*10 - 5) / 0.22
        y = 0.31 * X - 1.031002 + np.random.randn(n)
    except (RuntimeWarning, RuntimeError) as E:
        pass
    return X.reshape(n, 1), y.reshape(n, 1)


def generate_time_series(batch_size, n_steps):
    freq1, freq2, offsets1, offsets2 = np.random.rand(4, batch_size, 1)
    time = np.linspace(0, 1, n_steps)
    series = 0.5 * np.sin((time - offsets1) * (freq1 * 10 + 10)) # wave 1
    series += 0.2 * np.sin((time - offsets2) * (freq2 * 20 + 20)) # wave 2
    series += 0.1 * (np.random.rand(batch_size, n_steps) - 0.5) # + noise
    return series[..., np.newaxis].astype(np.float32)

