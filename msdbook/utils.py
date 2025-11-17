import warnings

import numpy as np
import statsmodels.api as sm

def fit_logit(dta, predictors):
    """Logistic regression with optional interaction term.
    
    Parameters
    ----------
    dta : pandas.DataFrame
        Input data containing the 'Success' column and predictor columns.
        If an 'Interaction' column is present, it will be included in the model.
    predictors : list of str
        List of predictor column names to include in the model.
    
    Returns
    -------
    statsmodels.discrete.discrete_model.BinaryResultsWrapper
        Fitted logistic regression model.
    
    Notes
    -----
    The function automatically adds an intercept column. If the data contains
    an 'Interaction' column, it will be included in the model alongside the
    specified predictors.
    """

    # Add intercept column of 1s
    dta["Intercept"] = np.ones(np.shape(dta)[0])
    
    # Get columns of predictors, starting with intercept
    cols = dta.columns.tolist()[-1:] + predictors
    
    # Add interaction term if present in the data
    if "Interaction" in dta.columns:
        cols = cols + ["Interaction"]
    
    # Fit logistic regression without the deprecated 'disp' argument
    logit = sm.Logit(dta["Success"], dta[cols])
    result = logit.fit(method='bfgs')  # Use method='bfgs' or another supported method
    
    return result

def plot_contour_map(
    ax, result, dta, contour_cmap, dot_cmap, levels, xgrid, ygrid, xvar, yvar, base
):
    """Plot the contour map"""

    # Ignore tight layout warnings
    warnings.filterwarnings("ignore")

    # Generate probability of success for x=xgrid, y=ygrid
    X, Y = np.meshgrid(xgrid, ygrid)
    x = X.flatten()
    y = Y.flatten()
    grid = np.column_stack([np.ones(len(x)), x, y, x * y])

    z = result.predict(grid)
    Z = np.reshape(z, np.shape(X))

    contourset = ax.contourf(X, Y, Z, levels, cmap=contour_cmap, aspect="auto")
    
    # Plot scatter points based on the data
    xpoints = np.mean(dta[xvar].values.reshape(-1, 10), axis=1)
    ypoints = np.mean(dta[yvar].values.reshape(-1, 10), axis=1)
    colors = np.round(np.mean(dta["Success"].values.reshape(-1, 10), axis=1), 0)
    
    ax.scatter(xpoints, ypoints, s=10, c=colors, edgecolor="none", cmap=dot_cmap)
    ax.set_xlim(np.min(xgrid), np.max(xgrid))
    ax.set_ylim(np.min(ygrid), np.max(ygrid))
    ax.set_xlabel(xvar, fontsize=14)
    ax.set_ylabel(yvar, fontsize=14)
    ax.tick_params(axis="both", labelsize=12)

    return contourset
