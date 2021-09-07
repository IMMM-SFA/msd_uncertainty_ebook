import pkg_resources

import numpy as np
import pandas as pd


def get_data_directory():
    """Return the directory of where the cerf package data resides."""

    return pkg_resources.resource_filename('msdbook', 'data')


def load_robustness_data():
    """Load robustness solution data from file.  For use in 'fishery_dynamics.ipynb'"""

    f = pkg_resources.resource_filename('msdbook', 'data/Robustness.txt')

    return np.loadtxt(f, delimiter=' ')


def load_profit_maximization_data():
    """Load profit-maximizing solution data from file.  For use in 'fishery_dynamics.ipynb'"""

    f = pkg_resources.resource_filename('msdbook', 'data/solutions.resultfile')

    return np.loadtxt(f)


def load_saltelli_param_values():
    """Load Saltelli parameter values from file.  For use in 'fishery_dynamics.ipynb'"""

    f = pkg_resources.resource_filename('msdbook', 'data/param_values.csv')

    return np.loadtxt(f, delimiter=',')


def load_collapse_data():
    """Load the predator population collapse data from file.  For use in 'fishery_dynamics.ipynb'"""

    f = pkg_resources.resource_filename('msdbook', 'data/collapse_days.csv')

    return np.loadtxt(f, delimiter=',')


def load_lhs_basin_sample():
    """Load LHS sample data from file.  For use in 'basin_users_logistic_regression.ipynb'"""

    f = pkg_resources.resource_filename('msdbook', 'data/LHsamples_original_1000.txt')

    return np.loadtxt(f)


def load_basin_param_bounds():
    """Load parameter bounds data from file.  For use in 'basin_users_logistic_regression.ipynb'"""

    f = pkg_resources.resource_filename('msdbook', 'data/uncertain_params_bounds.txt')

    return np.loadtxt(f, usecols=(1, 2))


def load_user_heatmap_array(user_id):
    """Load the heatmap array associated with the target user ID.

    For use in 'basin_users_logistic_regression.ipynb'

    """

    f = pkg_resources.resource_filename('msdbook', f'data/{user_id}_heatmap.npy')

    return np.load(f)


def load_user_pseudo_scores(user_id):
    """Load the pseudo r scores associated with the target user ID.

    For use in 'basin_users_logistic_regression.ipynb'

    """

    f = pkg_resources.resource_filename('msdbook', f'data/{user_id}_pseudo_r_scores.csv')

    return pd.read_csv(f)


def load_hymod_input_file():
    """Load data from file."""

    f = pkg_resources.resource_filename('msdbook', 'data/LeafCatch.csv')

    return pd.read_csv(f, sep=',')


def load_hymod_params():
    """Load HYMOD parameters from the Saltelli sample.  For use in 'hymod.ipynb'"""

    f = pkg_resources.resource_filename('msdbook', 'data/hymod_params_256samples.npy')

    return np.load(f)


def load_hymod_metric_simulation():
    """Load HYMOD metric sensitivity S1 outputs.  For use in 'hymod.ipynb'"""

    col_names = ['Kq', 'Ks', 'Alp', 'Huz', 'B']

    f = pkg_resources.resource_filename('msdbook', 'data/sa_metric_s1.npy')

    # load the numpy array
    arr = np.load(f)

    # construct dataframe
    return pd.DataFrame(arr, columns=col_names)


def load_hymod_simulation():
    """Load HYMOD simulated outputs.  For use in 'hymod.ipynb'"""

    f = pkg_resources.resource_filename('msdbook', 'data/hymod_simulations_256samples.csv')

    return pd.read_csv(f)


def load_hymod_monthly_simulations():
    """Load HYMOD monthly simulation.  For use in 'hymod.ipynb'"""

    f_delta = pkg_resources.resource_filename('msdbook', 'data/sa_by_mth_delta.npy')
    f_s1 = pkg_resources.resource_filename('msdbook', 'data/sa_by_mth_s1.npy')

    return np.load(f_delta), np.load(f_s1)


def load_hymod_annual_simulations():
    """Load HYMOD annual simulation.  For use in 'hymod.ipynb'"""

    f_delta = pkg_resources.resource_filename('msdbook', 'data/sa_by_yr_delta.npy')
    f_s1 = pkg_resources.resource_filename('msdbook', 'data/sa_by_yr_s1.npy')

    return np.load(f_delta), np.load(f_s1)


def load_hymod_varying_simulations():
    """Load HYMOD time varying simulation.  For use in 'hymod.ipynb'"""

    f_delta = pkg_resources.resource_filename('msdbook', 'data/sa_vary_delta.npy')
    f_s1 = pkg_resources.resource_filename('msdbook', 'data/sa_vary_s1.npy')

    return np.load(f_delta), np.load(f_s1)

