import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from msdbook.utils import fit_logit, plot_contour_map
from statsmodels.base.wrapper import ResultsWrapper


# Define commonly used column names as constants
PREDICTOR_1 = "Predictor1"
PREDICTOR_2 = "Predictor2"
INTERACTION = "Interaction"


@pytest.fixture
def sample_data():
    """Fixture to provide sample data for testing."""
    np.random.seed(0)  # For reproducibility
    
    # Number of samples
    n = 100

    # Generate some random data
    df = pd.DataFrame({
        'Success': np.random.randint(0, 2, size=n),  # Binary outcome variable (0 or 1)
        PREDICTOR_1: np.random.randn(n),  # Random values for Predictor1
        PREDICTOR_2: np.random.randn(n),  # Random values for Predictor2
        INTERACTION: np.random.randn(n)  # Random values for Interaction term
    })

    return df 


def test_fit_logit(sample_data):
    """Test the fit_logit function."""
    predictors = [PREDICTOR_1, PREDICTOR_2]
    result = fit_logit(sample_data, predictors)

    # Check if result is a statsmodels LogitResultsWrapper object
    assert isinstance(result, ResultsWrapper)
    
    # Check if the result object has the expected attributes
    assert hasattr(result, "params")
    assert hasattr(result, "pvalues")
    assert hasattr(result, "predict")

    # Check that parameters (coefficients) are not empty
    assert result.params is not None
    assert result.pvalues is not None

    # Check that the parameters (coefficients) are reasonable (e.g., non-zero)
    assert np.all(np.abs(result.params) > 0)  # Coefficients should not be zero

    # Check that the p-values are reasonable (not NaN, not infinity)
    assert np.all(np.isfinite(result.pvalues))  # P-values should be finite numbers
    assert np.any(result.pvalues < 0.05)  # At least one coefficient should be statistically significant (p-value < 0.05)


def test_plot_contour_map(sample_data):
    """Test the plot_contour_map function."""
    fig, ax = plt.subplots()

    # Fit a logit model for the purpose of plotting
    predictors = [PREDICTOR_1, PREDICTOR_2]
    result = fit_logit(sample_data, predictors)

    # Dynamically generate grid and levels
    xgrid = np.linspace(sample_data[PREDICTOR_1].min() - 1, sample_data[PREDICTOR_1].max() + 1, 50)
    ygrid = np.linspace(sample_data[PREDICTOR_2].min() - 1, sample_data[PREDICTOR_2].max() + 1, 50)
    levels = np.linspace(0, 1, 10)
    
    contour_cmap = 'viridis'
    dot_cmap = 'coolwarm'

    # Call the plot function
    contourset = plot_contour_map (
        ax,
        result,
        sample_data,
        contour_cmap,
        dot_cmap,
        levels,
        xgrid,
        ygrid,
        PREDICTOR_1,
        PREDICTOR_2,
        base=0,
    )

    # Check if the contour plot is created
    assert contourset is not None

    # Check if the axis limits and labels are set correctly
    assert ax.get_xlim() == (np.min(xgrid), np.max(xgrid))
    assert ax.get_ylim() == (np.min(ygrid), np.max(ygrid))
    assert ax.get_xlabel() == PREDICTOR_1
    assert ax.get_ylabel() == PREDICTOR_2

    # Verify that scatter plot is present by checking number of points
    assert len(ax.collections) > 0  
    plt.close(fig)


def test_empty_data():
    """Test with empty data to ensure no errors."""
    empty_df = pd.DataFrame({
        'Success': [],
        PREDICTOR_1: [],
        PREDICTOR_2: [],
        INTERACTION: []
    })
    
    predictors = [PREDICTOR_1, PREDICTOR_2]
    
    # Check if fitting with empty data raises an error
    with pytest.raises(ValueError):
        fit_logit(empty_df, predictors)

    # Skip plotting test if the dataframe is empty
    fig, ax = plt.subplots()

    # Ensure we don't try plotting with empty data
    if not empty_df.empty:
        result = fit_logit(empty_df, predictors)
        contourset = plot_contour_map(
            ax, result, empty_df,
            'viridis', 'coolwarm', np.linspace(0, 1, 10), np.linspace(-2, 2, 50),
            np.linspace(-2, 2, 50), PREDICTOR_1, PREDICTOR_2, base=0
        )
        assert contourset is not None
    else:
        # Skip if no result is generated (empty DataFrame)
        pass
    plt.close(fig)


def test_invalid_predictors(sample_data):
    """Test with invalid predictors."""
    invalid_predictors = ['InvalidPredictor1', 'InvalidPredictor2']
    
    with pytest.raises(KeyError):
        fit_logit(sample_data, invalid_predictors)


def test_logit_with_interaction(sample_data):
    """Test logistic regression with interaction term."""
    sample_data[INTERACTION] = sample_data[PREDICTOR_1] * sample_data[PREDICTOR_2]
    predictors = [PREDICTOR_1, PREDICTOR_2]
    
    result = fit_logit(sample_data, predictors)
    
    # Ensure the interaction term is included in the result
    assert INTERACTION in result.params.index
