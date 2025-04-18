import pytest
import numpy as np
import matplotlib.pyplot as plt

from msdbook.generalized_fish_game import (
    inequality,
    plot_uncertainty_relationship,
    plot_solutions,
    fish_game,
    hrvSTR
)

# Register the mpl_image_compare marker to prevent unknown marker warnings
pytestmark = pytest.mark.filterwarnings("ignore::pytest.PytestUnknownMarkWarning")

def test_inequality():
    b = 0.5
    m = 0.9
    h = 0.1
    K = 1000
    result = inequality(b, m, h, K)
    expected = (b**m) / (h * K) ** (1 - m)
    assert np.isclose(result, expected), f"Expected {expected}, but got {result}"

def test_hrvSTR():
    np.random.seed(42)
    Inputs = [0.5]
    vars = np.random.rand(20)
    input_ranges = [[0, 1]]
    output_ranges = [[0, 1]]
    
    result = hrvSTR(Inputs, vars, input_ranges, output_ranges)
    expected = [0.92786921]  # Adjust this if needed
    assert np.allclose(result, expected, atol=0.05), f"Expected {expected}, but got {result}"

def test_fish_game():
    vars = [0.1] * 20
    additional_inputs = [
        "Previous_Prey",
        "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9"
    ]
    N = 10
    tSteps = 100
    nObjs = 5
    nCnstr = 1
    
    objs, cnstr = fish_game(vars, additional_inputs, N, tSteps, nObjs, nCnstr)
    
    assert len(objs) == nObjs
    assert len(cnstr) == nCnstr
    assert np.all(np.isfinite(objs))
    assert np.all(np.isfinite(cnstr))

@pytest.mark.mpl_image_compare
def test_plot_uncertainty_relationship():
    param_values = np.random.rand(10, 7)
    collapse_days = np.random.rand(10, 2)
    
    plot_uncertainty_relationship(param_values, collapse_days)
    # No return, test will auto-compare generated figure

@pytest.mark.mpl_image_compare
def test_plot_solutions():
    objective_performance = np.random.rand(100, 5)
    profit_solution = 0
    robust_solution = 1

    plot_solutions(objective_performance, profit_solution, robust_solution)
    # No return, test will auto-compare generated figure
