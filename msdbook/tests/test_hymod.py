import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from msdbook.hymod import (
    plot_observed_vs_simulated_streamflow,
    plot_observed_vs_sensitivity_streamflow,
    plot_monthly_heatmap,
    plot_annual_heatmap,
    plot_varying_heatmap,
    plot_precalibration_flow,
    plot_precalibration_glue,
    Pdm01,
    Nash,
    Hymod01,
    hymod
)

@pytest.fixture
def sample_data():
    """Fixture for sample input data."""
    dates = pd.date_range(start='2000-01-01', periods=10)
    df = pd.DataFrame({
        'Precip': np.random.rand(10),
        'Pot_ET': np.random.rand(10),
        'Strmflw': np.random.rand(10)
    }, index=dates)
    return df

@pytest.fixture
def sample_simulated():
    """Fixture for sample simulated data."""
    return pd.DataFrame(np.random.rand(10, 3), columns=['Sim1', 'Sim2', 'Sim3'])

@pytest.fixture
def sample_heatmap_data():
    """Fixture for sample heatmap data."""
    return np.random.rand(5, 12), pd.DataFrame(np.random.rand(12), columns=['Strmflw'])

def test_plot_observed_vs_simulated_streamflow(sample_data):
    """Test if the function for plotting observed vs simulated streamflow works without errors."""
    hymod_dict = {"Q": np.random.rand(len(sample_data))}
    ax = plot_observed_vs_simulated_streamflow(sample_data, hymod_dict)
    assert isinstance(ax, plt.Axes)
    plt.close()

def test_plot_observed_vs_sensitivity_streamflow(sample_data, sample_simulated):
    """Test if the function for plotting observed vs sensitivity streamflow works without errors."""
    ax = plot_observed_vs_sensitivity_streamflow(sample_data, sample_simulated)
    assert isinstance(ax, plt.Axes)
    plt.close()

def test_plot_monthly_heatmap(sample_heatmap_data):
    """Test if the function for plotting monthly heatmap works without errors."""
    arr_sim, df_obs = sample_heatmap_data
    ax, ax2 = plot_monthly_heatmap(arr_sim, df_obs)
    assert isinstance(ax, plt.Axes)
    assert isinstance(ax2, plt.Axes)
    plt.close()

def test_Pdm01():
    """Test Pdm01 function for correct output."""
    OV, ET, Hend, Cend = Pdm01(1.0, 0.5, 0.2, 0.1, 0.3)
    assert isinstance(OV, float)
    assert isinstance(ET, float)
    assert isinstance(Hend, float)
    assert isinstance(Cend, float)

def test_Nash():
    """Test Nash function for correct output."""
    out, Xend = Nash(0.5, 5, np.zeros(5), 1.0)
    assert isinstance(out, float)
    assert isinstance(Xend, np.ndarray)
    assert Xend.shape == (5,)

def test_Hymod01(sample_data):
    """Test Hymod01 function for correct output."""
    pars = {"Nq": 2, "Kq": 0.5, "Ks": 0.1, "Alp": 0.3, "Huz": 0.5, "B": 1.0}
    init = {"Xq": np.zeros(pars["Nq"]), "Xs": 0, "XHuz": 0}
    results = Hymod01(sample_data, pars, init)
    assert isinstance(results, dict)
    assert all(key in results for key in ["XHuz", "XCuz", "Xq", "Xs", "ET", "OV", "Qq", "Qs", "Q"])
    assert isinstance(results["XHuz"], np.ndarray)
    assert isinstance(results["Q"], np.ndarray)

def test_hymod(sample_data):
    """Test hymod function for correct output."""
    results = hymod(2, 0.5, 0.1, 0.3, 0.5, 1.0, sample_data, 10)
    assert isinstance(results, dict)
    assert all(key in results for key in ["XHuz", "XCuz", "Xq", "Xs", "ET", "OV", "Qq", "Qs", "Q"])
    assert isinstance(results["Q"], np.ndarray)
