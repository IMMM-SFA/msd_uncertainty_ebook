import pytest
import numpy as np 
import matplotlib.pyplot as plt
from pytest_mock import MockerFixture
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib.testing.decorators import check_figures_equal
from msdbook.fishery_dynamics import plot_objective_performance, plot_factor_performance

@pytest.fixture
def sample_data():
    """Fixture to provide sample data for testing."""
    objective_performance = np.array([
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7]
    ])
    profit_solution = 1
    robust_solution = 2
    param_values = np.random.rand(100, 7)  
    collapse_days = np.random.rand(100, 2) * 10  
    b = np.linspace(0, 1, 10)
    m = np.linspace(0, 1, 10)
    a = np.linspace(0, 2, 10)
    return {
        'objective_performance': objective_performance,
        'profit_solution': profit_solution,
        'robust_solution': robust_solution,
        'param_values': param_values,
        'collapse_days': collapse_days,
        'b': b,
        'm': m,
        'a': a
    }


def test_plot_objective_performance(sample_data, mocker):
    """Test the plot_objective_performance function."""
    fig, ax = plt.subplots()
    mocker.patch('matplotlib.pyplot.figure', return_value=fig)
    
    plot_objective_performance(
        sample_data['objective_performance'],
        sample_data['profit_solution'],
        sample_data['robust_solution']
    )
    
    # Ensure figure and axes are created
    assert plt.gcf() == fig
    assert len(fig.axes) > 0
    
    # Check for colorbars in the figure
    colorbars = [c for a in fig.axes for c in a.collections if isinstance(c, plt.cm.ScalarMappable)]
    assert len(colorbars) > 0


def test_plot_factor_performance(sample_data, mocker):
    """Test the plot_factor_performance function."""
    fig, axs = plt.subplots(1, 2, subplot_kw={'projection': '3d'})
    mocker.patch('matplotlib.pyplot.figure', return_value=fig)
    
    # Reshape b, m, a to 2D arrays for plotting
    b, m = np.meshgrid(sample_data['b'], sample_data['m'])
    a = np.tile(sample_data['a'], (len(sample_data['m']), 1))  

    plot_factor_performance(
        sample_data['param_values'],
        sample_data['collapse_days'],
        b,
        m,
        a
    )
    
    # Ensure figure and axes are created
    assert plt.gcf() == fig
    assert len(fig.axes) >= 3  
    
    for ax in axs:
        assert isinstance(ax, Axes3D)  

    # Check for colorbars in the figure
    colorbars = [c for a in fig.axes for c in a.collections if isinstance(c, plt.cm.ScalarMappable)]
    assert len(colorbars) > 0

