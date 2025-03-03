import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from msdbook.utils import fit_logit, plot_contour_map
from statsmodels.base.wrapper import ResultsWrapper

# Define column names as variables for easy reference
predictor1 = 'Predictor1'
predictor2 = 'Predictor2'
interaction = 'Interaction'
intercept = 'Intercept'
success = 'Success'

@pytest.fixture
def sample_data():
    """Fixture to provide sample data for testing."""
    np.random.seed(0)  # For reproducibility
    
    # Number of samples
    n = 100

    # Generate some random data
    df = pd.DataFrame({
        success: np.random.randint(0, 2, size=n),  # Binary outcome variable (0 or 1)
        predictor1: np.random.randn(n),  # Random values for Predictor1
        predictor2: np.random.randn(n),  # Random values for Predictor2
        interaction: np.random.randn(n)  # Random values for Interaction term
    })

    return df

@pytest.mark.parametrize("sample_data, df_resid, df_model, llf", [
    (pd.DataFrame({
        predictor1: [1.0, 2.0, 3.0],
        predictor2: [3.0, 4.0, 5.0],
        interaction: [2.0, 4.0, 6.0],
        intercept: [1.0, 1.0, 1.0],
        success: [1.0, 1.0, 0.0],
    }), 0.0, 2.0, -6.691275315650184e-06),

    (pd.DataFrame({
        predictor1: [5.0, 6.0, 7.0],
        predictor2: [7.0, 8.0, 9.0],
        interaction: [3.0, 6.0, 9.0],
        intercept: [1.0, 1.0, 1.0],
        success: [1.0, 0.0, 1.0],
    }), 0.0, 2.0, -2.4002923915238235e-06),

    (pd.DataFrame({
        predictor1: [0.5, 1.5, 2.5],
        predictor2: [1.0, 2.0, 3.0],
        interaction: [0.2, 0.4, 0.6],
        intercept: [1.0, 1.0, 1.0],
        success: [0.0, 1.0, 1.0],
    }), 0.0, 2.0, -1.7925479970021486e-05)
])
def test_fit_logit(sample_data, df_resid, df_model, llf):
    """Test the fit_logit function and ensure it works with the provided sample data."""
    predictors = [predictor1, predictor2]
    result = fit_logit(sample_data, predictors)
    assert result.df_resid == df_resid
    assert result.df_model == df_model
    assert result.llf == llf


def test_plot_contour_map(sample_data):
    """Test the plot_contour_map function."""
    fig, ax = plt.subplots()

    # Fit a logit model for the purpose of plotting
    result = fit_logit(sample_data, [predictor1, predictor2])

    # Dynamically generate grid and levels based on input data to reflect the data range
    xgrid_min, xgrid_max = sample_data[predictor1].min(), sample_data[predictor1].max()
    ygrid_min, ygrid_max = sample_data[predictor2].min(), sample_data[predictor2].max()
    xgrid = np.linspace(xgrid_min - 1, xgrid_max + 1, 50)
    ygrid = np.linspace(ygrid_min - 1, ygrid_max + 1, 50)
    levels = np.linspace(0, 1, 10)
    
    contour_cmap = 'viridis'
    dot_cmap = 'coolwarm'
    
    # Call the plot function
    contourset = plot_contour_map(
        ax,
        result,
        sample_data,
        contour_cmap,
        dot_cmap,
        levels,
        xgrid,
        ygrid,
        predictor1,
        predictor2,
        base=0,
    )

    # Verify the plot and axis limits/labels are correct
    assert contourset is not None
    assert ax.get_xlim() == (xgrid.min(), xgrid.max())
    assert ax.get_ylim() == (ygrid.min(), ygrid.max())
    assert ax.get_xlabel() == predictor1
    assert ax.get_ylabel() == predictor2

    # Verify that scatter plot is present by checking the number of points
    assert len(ax.collections) > 0  
    plt.close(fig)


def test_fit_logit_empty_data():
    """Test the fit_logit function with empty data to ensure no errors."""
    empty_df = pd.DataFrame({
        success: [],
        predictor1: [],
        predictor2: [],
        interaction: []
    })

    # Test if fitting with empty data raises an error
    with pytest.raises(ValueError):
        fit_logit(empty_df, [predictor1, predictor2])

    plt.close()


def test_fit_logit_invalid_predictors(sample_data):
    """Test the fit_logit function with invalid predictors."""
    invalid_predictors = ['InvalidPredictor1', 'InvalidPredictor2']
    
    with pytest.raises(KeyError):
        fit_logit(sample_data, invalid_predictors)


def test_fit_logit_comprehensive(sample_data):
    """Comprehensive test for fit_logit checking various aspects."""
    # Check valid predictors
    result = fit_logit(sample_data, [predictor1, predictor2])  # There are variables for predictor1 and predictor2
    
    # Validate coefficients are reasonable
    assert np.all(np.abs(result.params) > 1e-5)  # Coefficients should not be too close to zero

    # Check if specific expected values are close (if known from actual model output)
    EXPECTED_PARAMS = np.array([0.34060709, -0.26968773, 0.31551482, 0.45824332])  # Update with actual expected values
    assert np.allclose(result.params.values, EXPECTED_PARAMS, atol=0.1)  # Increased tolerance to 0.1

    # Check p-values are valid
    assert np.all(np.isfinite(result.pvalues))  # P-values should be finite numbers
    # Check if any coefficient has a p-value less than 0.1 (10% significance level)
    assert np.any(result.pvalues < 0.1)

