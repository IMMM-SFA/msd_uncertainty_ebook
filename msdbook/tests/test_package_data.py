import pytest
import numpy as np
import pandas as pd
import importlib.resources
from package_data import (
    get_data_directory,
    load_robustness_data,
    load_profit_maximization_data,
    load_saltelli_param_values,
    load_collapse_data,
    load_lhs_basin_sample,
    load_basin_param_bounds,
    load_user_heatmap_array,
    load_user_pseudo_scores,
    load_hymod_input_file,
    load_hymod_params,
    load_hymod_metric_simulation,
    load_hymod_simulation,
    load_hymod_monthly_simulations,
    load_hymod_annual_simulations,
    load_hymod_varying_simulations
)

@pytest.fixture
def test_data_dir(tmp_path):
    # Create test data directory
    data_dir = tmp_path / "msdbook" / "data"
    data_dir.mkdir(parents=True)

    # Create example data files
    np.savetxt(data_dir / "Robustness.txt", np.array([[1, 2], [3, 4]]), delimiter=" ")
    np.savetxt(data_dir / "solutions.resultfile", np.array([[5, 6], [7, 8]]))
    np.savetxt(data_dir / "param_values.csv", np.array([[9, 10], [11, 12]]), delimiter=",")
    np.savetxt(data_dir / "collapse_days.csv", np.array([[13, 14], [15, 16]]), delimiter=",")
    np.savetxt(data_dir / "LHsamples_original_1000.txt", np.array([[17, 18], [19, 20]]))
    np.savetxt(data_dir / "uncertain_params_bounds.txt", np.array([[21, 22], [23, 24]]))
    np.save(data_dir / "user123_heatmap.npy", np.array([[25, 26], [27, 28]]))
    pd.DataFrame([[29, 30], [31, 32]], columns=['A', 'B']).to_csv(data_dir / "user123_pseudo_r_scores.csv", index=False)
    pd.DataFrame([[33, 34], [35, 36]], columns=['C', 'D']).to_csv(data_dir / "LeafCatch.csv", index=False)
    np.save(data_dir / "hymod_params_256samples.npy", np.array([[37, 38], [39, 40]]))
    np.save(data_dir / "sa_metric_s1.npy", np.array([[41, 42, 43, 44, 45]]))
    pd.DataFrame([[46, 47], [48, 49]], columns=['E', 'F']).to_csv(data_dir / "hymod_simulations_256samples.csv", index=False)
    np.save(data_dir / "sa_by_mth_delta.npy", np.array([[50, 51], [52, 53]]))
    np.save(data_dir / "sa_by_mth_s1.npy", np.array([[54, 55], [56, 57]]))
    np.save(data_dir / "sa_by_yr_delta.npy", np.array([[58, 59], [60, 61]]))
    np.save(data_dir / "sa_by_yr_s1.npy", np.array([[62, 63], [64, 65]]))
    np.save(data_dir / "sa_vary_delta.npy", np.array([[66, 67], [68, 69]]))
    np.save(data_dir / "sa_vary_s1.npy", np.array([[70, 71], [72, 73]]))

    return data_dir

# Helper function to set the resource path for importlib
def set_resource_path(path):
    importlib.resources.files = lambda package: path

def test_get_data_directory(test_data_dir):
    set_resource_path(test_data_dir)
    assert get_data_directory() == str(test_data_dir)


def test_load_robustness_data(test_data_dir):
    set_resource_path(test_data_dir)
    data = load_robustness_data()
    expected = np.array([[1, 2], [3, 4]])
    assert np.array_equal(data, expected)


def test_load_profit_maximization_data(test_data_dir):
    set_resource_path(test_data_dir)
    data = load_profit_maximization_data()
    expected = np.array([[5, 6], [7, 8]])
    assert np.array_equal(data, expected)


def test_load_saltelli_param_values(test_data_dir):
    set_resource_path(test_data_dir)
    data = load_saltelli_param_values()
    expected = np.array([[9, 10], [11, 12]])
    assert np.array_equal(data, expected)


def test_load_collapse_data(test_data_dir):
    set_resource_path(test_data_dir)
    data = load_collapse_data()
    expected = np.array([[13, 14], [15, 16]])
    assert np.array_equal(data, expected)


def test_load_lhs_basin_sample(test_data_dir):
    set_resource_path(test_data_dir)
    data = load_lhs_basin_sample()
    expected = np.array([[17, 18], [19, 20]])
    assert np.array_equal(data, expected)


def test_load_basin_param_bounds(test_data_dir):
    set_resource_path(test_data_dir)
    data = load_basin_param_bounds()
    expected = np.array([[21, 22], [23, 24]])
    assert np.array_equal(data, expected)


def test_load_user_heatmap_array(test_data_dir):
    set_resource_path(test_data_dir)
    data = load_user_heatmap_array("user123")
    expected = np.array([[25, 26], [27, 28]])
    assert np.array_equal(data, expected)


def test_load_user_pseudo_scores(test_data_dir):
    set_resource_path(test_data_dir)
    data = load_user_pseudo_scores("user123")
    expected = pd.DataFrame([[29, 30], [31, 32]], columns=['A', 'B'])
    pd.testing.assert_frame_equal(data, expected)


def test_load_hymod_input_file(test_data_dir):
    set_resource_path(test_data_dir)
    data = load_hymod_input_file()
    expected = pd.DataFrame([[33, 34], [35, 36]], columns=['C', 'D'])
    pd.testing.assert_frame_equal(data, expected)


def test_load_hymod_params(test_data_dir):
    set_resource_path(test_data_dir)
    data = load_hymod_params()
    expected = np.array([[37, 38], [39, 40]])
    assert np.array_equal(data, expected)


def test_load_hymod_metric_simulation(test_data_dir):
    set_resource_path(test_data_dir)
    data = load_hymod_metric_simulation()
    expected = pd.DataFrame([[41, 42, 43, 44, 45]], columns=["Kq", "Ks", "Alp", "Huz", "B"])
    pd.testing.assert_frame_equal(data, expected)


def test_load_hymod_simulation(test_data_dir):
    set_resource_path(test_data_dir)
    data = load_hymod_simulation()
    expected = pd.DataFrame([[46, 47], [48, 49]], columns=['E', 'F'])
    pd.testing.assert_frame_equal(data, expected)


def test_load_hymod_monthly_simulations(test_data_dir):
    set_resource_path(test_data_dir)
    delta, s1 = load_hymod_monthly_simulations()
    expected_delta = np.array([[50, 51], [52, 53]])
    expected_s1 = np.array([[54, 55], [56, 57]])
    assert np.array_equal(delta, expected_delta)
    assert np.array_equal(s1, expected_s1)


def test_load_hymod_annual_simulations(test_data_dir):
    set_resource_path(test_data_dir)
    delta, s1 = load_hymod_annual_simulations()
    expected_delta = np.array([[58, 59], [60, 61]])
    expected_s1 = np.array([[62, 63], [64, 65]])
    assert np.array_equal(delta, expected_delta)
    assert np.array_equal(s1, expected_s1)


def test_load_hymod_varying_simulations(test_data_dir):
    set_resource_path(test_data_dir)
    delta, s1 = load_hymod_varying_simulations()
    expected_delta = np.array([[66, 67], [68, 69]])
    expected_s1 = np.array([[70, 71], [72, 73]])
    assert np.array_equal(delta, expected_delta)
    assert np.array_equal(s1, expected_s1)
