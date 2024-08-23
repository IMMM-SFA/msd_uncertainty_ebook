import pytest
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from msdbook.utils import fit_logit, plot_contour_map

@pytest.fixture
def sample_data():
    """Fix to provide sample data for testing."""
    np.random.seed(0)
    # Generate some random data
    n = 100
    df = pd.DataFrame({
        'Success': np.random.randint(0, 2, size=n),
        'Predictor1': np.random.randn(n),
        'Predictor2': np.random.randn(n),
        'Interaction': np.random.randn(n)
    })
    return df

def test_fit_logit(sample_data):
    """Test the fit_logit function."""
    predictors = ['Predictor1', 'Predictor2']
    result = fit_logit(sample_data, predictors)
    
    # Check if result is a statsmodels regression results object
    assert isinstance(result, sm.LogitResults)
    
    # Check if the result object has the expected attributes
    assert hasattr(result, 'params')
    assert hasattr(result, 'pvalues')
    assert hasattr(result, 'predict')

def test_plot_contour_map(sample_data):
    """Test the plot_contour_map function."""
    fig, ax = plt.subplots()
    
    # Fit a logit model for the purpose of plotting
    predictors = ['Predictor1', 'Predictor2']
    result = fit_logit(sample_data, predictors)
    
    xgrid = np.linspace(-2, 2, 50)
    ygrid = np.linspace(-2, 2, 50)
    
    contour_cmap = 'viridis'
    dot_cmap = 'coolwarm'
    levels = np.linspace(0, 1, 10)
    
    # Call the plot function
    contourset = plot_contour_map(
        ax, result, sample_data, contour_cmap, dot_cmap, levels, xgrid, ygrid, 'Predictor1', 'Predictor2', base=0
    )
    
    # Check if the contour plot is created
    assert contourset is not None
    
    # Check if the axis limits and labels are set correctly
    assert ax.get_xlim() == (np.min(xgrid), np.max(xgrid))
    assert ax.get_ylim() == (np.min(ygrid), np.max(ygrid))
    assert ax.get_xlabel() == 'Predictor1'
    assert ax.get_ylabel() == 'Predictor2'
    
    # Verify that scatter plot is present by checking number of points
    assert len(ax.collections) > 0  # Scatter plot should create collections

    plt.close(fig)
