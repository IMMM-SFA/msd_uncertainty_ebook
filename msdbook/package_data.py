import pkg_resources

import numpy as np
import pandas as pd


def load_robustness_data():
    """Load data from file."""

    f = pkg_resources.resource_filename('msdbook', 'data/Robustness.txt')

    return np.loadtxt(f, delimiter=' ')


def load_result_data():
    """Load data from file."""

    f = pkg_resources.resource_filename('msdbook', 'data/solutions.resultfile')

    return np.loadtxt(f)


def load_hymod_input_file():
    """Load data from file."""

    f = pkg_resources.resource_filename('msdbook', 'data/LeafCatch.csv')

    return pd.read_csv(f, sep=',')
