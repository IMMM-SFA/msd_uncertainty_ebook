import pkg_resources

import numpy as np


def load_robustness_data():
    """Load data from file."""

    f = pkg_resources.resource_filename('msdbook', 'data/Robustness.txt')

    return np.loadtxt(f, delimiter=' ')


def load_result_data():
    """Load data from file."""

    f = pkg_resources.resource_filename('msdbook', 'data/solutions.resultfile')

    return np.loadtxt(f)
