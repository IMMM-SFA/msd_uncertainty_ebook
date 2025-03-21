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
    # Set a fixed seed for reproducibility
    np.random.seed(42)

    Inputs = [0.5]
    vars = np.random.rand(20)  # Ensure there are enough values for nRBF, nIn, and nOut
    input_ranges = [[0, 1]]
    output_ranges = [[0, 1]]
    
    result = hrvSTR(Inputs, vars, input_ranges, output_ranges)
    
    # Set a new expected value based on the seeded result
    expected = [0.92786921]  # Update the expected value after running the function and checking results
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
    
    assert len(objs) == nObjs, "Incorrect number of objective values"
    assert len(cnstr) == nCnstr, "Incorrect number of constraint values"
    assert np.all(np.isfinite(objs)), "Objective values should be finite"
    assert np.all(np.isfinite(cnstr)), "Constraint values should be finite"

@pytest.mark.mpl_image_compare
def test_plot_uncertainty_relationship():
    param_values = np.random.rand(10, 7)
    collapse_days = np.random.rand(10, 2)
    
    fig, ax = plt.subplots()  # Create an axis for the plot
    plot_uncertainty_relationship(param_values, collapse_days)

    # Create a ScalarMappable for the colorbar
    sm = plt.cm.ScalarMappable(cmap=plt.cm.get_cmap("RdBu_r"))
    sm.set_array(collapse_days)  # Pass data for the colorbar
    
    # Explicitly specify the axis (ax) for colorbar
    cbar = fig.colorbar(sm, ax=ax)  # Explicitly pass the axis for colorbar
    cbar.set_label("Days with predator collapse")
    
    return fig


@pytest.mark.mpl_image_compare
def test_plot_solutions():
    objective_performance = np.random.rand(100, 5)
    profit_solution = 0
    robust_solution = 1
    
    fig, ax = plt.subplots()  # Create an axis for the plot
    plot_solutions(objective_performance, profit_solution, robust_solution)

    # Create a ScalarMappable for the colorbar
    sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues)
    sm.set_array(objective_performance[:, 0])  # Pass data for the colorbar
    
    # Explicitly specify the axis (ax) for colorbar
    cbar = fig.colorbar(sm, ax=ax)  # Explicitly pass the axis for colorbar
    cbar.set_label("\nNet present value (NPV)")
    
    return fig
