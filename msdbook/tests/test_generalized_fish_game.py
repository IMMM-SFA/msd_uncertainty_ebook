import pytest
import numpy as np
from generalized_fish_game import (
    inequality,
    plot_uncertainty_relationship,
    plot_solutions,
    fish_game,
    hrvSTR
)

def test_inequality():
    # Test with some example values
    b = 0.5
    m = 0.9
    h = 0.1
    K = 1000
    result = inequality(b, m, h, K)
    expected = (b**m) / (h * K) ** (1 - m)
    assert np.isclose(result, expected), f"Expected {expected}, but got {result}"

def test_hrvSTR():
    Inputs = [0.5]
    vars = [0.1, 0.2, 0.3, 0.4]
    input_ranges = [[0, 1]]
    output_ranges = [[0, 1]]
    
    result = hrvSTR(Inputs, vars, input_ranges, output_ranges)
    expected = [0.5]  # This should be replaced with the actual expected value
    assert np.allclose(result, expected), f"Expected {expected}, but got {result}"

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
    
    assert len(objs) == nObjs, "Incorrect number of objective values"
    assert len(cnstr) == nCnstr, "Incorrect number of constraint values"
    assert np.all(np.isfinite(objs)), "Objective values should be finite"
    assert np.all(np.isfinite(cnstr)), "Constraint values should be finite"

@pytest.mark.mpl_image_compare
def test_plot_uncertainty_relationship():
    param_values = np.random.rand(10, 7)
    collapse_days = np.random.rand(10, 2)
    
    fig = plt.figure()
    plot_uncertainty_relationship(param_values, collapse_days)
    return fig

@pytest.mark.mpl_image_compare
def test_plot_solutions():
    objective_performance = np.random.rand(100, 5)
    profit_solution = 0
    robust_solution = 1
    
    fig = plt.figure()
    plot_solutions(objective_performance, profit_solution, robust_solution)
    return fig
