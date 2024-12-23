import pytest
from unittest import mock
import numpy as np
import pandas as pd
from msdbook import package_data

# Mock data for testing
mock_robustness_data = np.array([1.0, 2.0, 3.0])
mock_profit_maximization_data = np.array([4.0, 5.0, 6.0])
mock_param_values = np.array([[1, 2], [3, 4], [5, 6]])
mock_collapse_data = np.array([[1, 100], [2, 200], [3, 300]])
mock_lhs_basin_sample = np.array([0.1, 0.2, 0.3])
mock_basin_param_bounds = np.array([[1, 10], [2, 20], [3, 30]])
mock_user_heatmap_array = np.array([[1, 2], [3, 4]])
mock_user_pseudo_scores = pd.DataFrame({'user_id': [1, 2], 'score': [0.5, 0.7]})
mock_hymod_input_file = pd.DataFrame({'time': [0, 1], 'value': [10, 20]})
mock_hymod_params = np.array([0.01, 0.02, 0.03])
mock_hymod_metric_simulation = pd.DataFrame({'Kq': [1.0], 'Ks': [2.0], 'Alp': [3.0], 'Huz': [4.0], 'B': [5.0]})
mock_hymod_simulation = pd.DataFrame({'time': [1, 2], 'value': [0.1, 0.2]})
mock_hymod_monthly_simulations = (np.array([0.1, 0.2]), np.array([0.3, 0.4]))
mock_hymod_annual_simulations = (np.array([0.5, 0.6]), np.array([0.7, 0.8]))
mock_hymod_varying_simulations = (np.array([0.9, 1.0]), np.array([1.1, 1.2]))

# Test for the function get_data_directory
@mock.patch("importlib.resources.files")
def test_get_data_directory(mock_files):
    mock_files.return_value.joinpath.return_value = "mocked/data/directory"
    result = package_data.get_data_directory()
    assert result == "mocked/data/directory"


# Test for load_robustness_data
@mock.patch("msdbook.package_data.np.loadtxt")
def test_load_robustness_data(mock_loadtxt):
    mock_loadtxt.return_value = mock_robustness_data
    result = package_data.load_robustness_data()
    assert isinstance(result, np.ndarray)
    np.testing.assert_array_equal(result, mock_robustness_data)


# Test for load_profit_maximization_data
@mock.patch("msdbook.package_data.np.loadtxt")
def test_load_profit_maximization_data(mock_loadtxt):
    mock_loadtxt.return_value = mock_profit_maximization_data
    result = package_data.load_profit_maximization_data()
    assert isinstance(result, np.ndarray)
    np.testing.assert_array_equal(result, mock_profit_maximization_data)


# Test for load_saltelli_param_values
@mock.patch("msdbook.package_data.np.loadtxt")
def test_load_saltelli_param_values(mock_loadtxt):
    mock_loadtxt.return_value = mock_param_values
    result = package_data.load_saltelli_param_values()
    assert isinstance(result, np.ndarray)
    np.testing.assert_array_equal(result, mock_param_values)


# Test for load_collapse_data
@mock.patch("msdbook.package_data.np.loadtxt")
def test_load_collapse_data(mock_loadtxt):
    mock_loadtxt.return_value = mock_collapse_data
    result = package_data.load_collapse_data()
    assert isinstance(result, np.ndarray)
    np.testing.assert_array_equal(result, mock_collapse_data)


# Test for load_lhs_basin_sample
@mock.patch("msdbook.package_data.np.loadtxt")
def test_load_lhs_basin_sample(mock_loadtxt):
    mock_loadtxt.return_value = mock_lhs_basin_sample
    result = package_data.load_lhs_basin_sample()
    assert isinstance(result, np.ndarray)
    np.testing.assert_array_equal(result, mock_lhs_basin_sample)


# Test for load_basin_param_bounds
@mock.patch("msdbook.package_data.np.loadtxt")
def test_load_basin_param_bounds(mock_loadtxt):
    mock_loadtxt.return_value = mock_basin_param_bounds
    result = package_data.load_basin_param_bounds()
    assert isinstance(result, np.ndarray)
    np.testing.assert_array_equal(result, mock_basin_param_bounds)


# Test for load_user_heatmap_array
@mock.patch("msdbook.package_data.np.load")
def test_load_user_heatmap_array(mock_load):
    mock_load.return_value = mock_user_heatmap_array
    result = package_data.load_user_heatmap_array(user_id="123")
    assert isinstance(result, np.ndarray)
    np.testing.assert_array_equal(result, mock_user_heatmap_array)


# Test for load_user_pseudo_scores
@mock.patch("msdbook.package_data.pd.read_csv")
def test_load_user_pseudo_scores(mock_read_csv):
    mock_read_csv.return_value = mock_user_pseudo_scores
    result = package_data.load_user_pseudo_scores(user_id="123")
    assert isinstance(result, pd.DataFrame)
    pd.testing.assert_frame_equal(result, mock_user_pseudo_scores)


# Test for load_hymod_input_file
@mock.patch("msdbook.package_data.pd.read_csv")
def test_load_hymod_input_file(mock_read_csv):
    mock_read_csv.return_value = mock_hymod_input_file
    result = package_data.load_hymod_input_file()
    assert isinstance(result, pd.DataFrame)
    pd.testing.assert_frame_equal(result, mock_hymod_input_file)


# Test for load_hymod_params
@mock.patch("msdbook.package_data.np.load")
def test_load_hymod_params(mock_load):
    mock_load.return_value = mock_hymod_params
    result = package_data.load_hymod_params()
    assert isinstance(result, np.ndarray)
    np.testing.assert_array_equal(result, mock_hymod_params)


# Test for load_hymod_metric_simulation
@mock.patch("msdbook.package_data.np.load")
def test_load_hymod_metric_simulation(mock_load):
    mock_load.return_value = mock_hymod_metric_simulation.values
    result = package_data.load_hymod_metric_simulation()
    assert isinstance(result, pd.DataFrame)
    pd.testing.assert_frame_equal(result, mock_hymod_metric_simulation)


# Test for load_hymod_simulation
@mock.patch("msdbook.package_data.pd.read_csv")
def test_load_hymod_simulation(mock_read_csv):
    mock_read_csv.return_value = mock_hymod_simulation
    result = package_data.load_hymod_simulation()
    assert isinstance(result, pd.DataFrame)
    pd.testing.assert_frame_equal(result, mock_hymod_simulation)


# Test for load_hymod_monthly_simulations
@mock.patch("msdbook.package_data.np.load")
def test_load_hymod_monthly_simulations(mock_load):
    mock_load.side_effect = [mock_hymod_monthly_simulations[0], mock_hymod_monthly_simulations[1]]
    result = package_data.load_hymod_monthly_simulations()
    assert isinstance(result, tuple)
    assert isinstance(result[0], np.ndarray)
    assert isinstance(result[1], np.ndarray)
    np.testing.assert_array_equal(result[0], mock_hymod_monthly_simulations[0])
    np.testing.assert_array_equal(result[1], mock_hymod_monthly_simulations[1])


# Test for load_hymod_annual_simulations
@mock.patch("msdbook.package_data.np.load")
def test_load_hymod_annual_simulations(mock_load):
    mock_load.side_effect = [mock_hymod_annual_simulations[0], mock_hymod_annual_simulations[1]]
    result = package_data.load_hymod_annual_simulations()
    assert isinstance(result, tuple)
    assert isinstance(result[0], np.ndarray)
    assert isinstance(result[1], np.ndarray)
    np.testing.assert_array_equal(result[0], mock_hymod_annual_simulations[0])
    np.testing.assert_array_equal(result[1], mock_hymod_annual_simulations[1])


# Test for load_hymod_varying_simulations
@mock.patch("msdbook.package_data.np.load")
def test_load_hymod_varying_simulations(mock_load):
    mock_load.side_effect = [mock_hymod_varying_simulations[0], mock_hymod_varying_simulations[1]]
    result = package_data.load_hymod_varying_simulations()
    assert isinstance(result, tuple)
    assert isinstance(result[0], np.ndarray)
    assert isinstance(result[1], np.ndarray)
    np.testing.assert_array_equal(result[0], mock_hymod_varying_simulations[0])
    np.testing.assert_array_equal(result[1], mock_hymod_varying_simulations[1])

