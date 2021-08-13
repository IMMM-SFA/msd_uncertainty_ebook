import numpy as np
import statsmodels.api as sm


def load_performance(ID):
    """Need description"""

    allSOWs = np.load('./data/'+ ID + '_heatmap.npy')

    return allSOWs


def fitLogit(dta, predictors):
    """Need description"""

    # concatenate intercept column of 1s
    dta['Intercept'] = np.ones(np.shape(dta)[0])
    # get columns of predictors
    cols = dta.columns.tolist()[-1:] + predictors + ['Interaction']
    #fit logistic regression
    logit = sm.Logit(dta['Success'], dta[cols], disp=False)
    result = logit.fit()

    return result


def plotContourMap(ax, result, dta, contour_cmap, dot_cmap, levels, xgrid, ygrid, xvar, yvar, base):
    """Need description"""

    # find probability of success for x=xgrid, y=ygrid
    X, Y = np.meshgrid(xgrid, ygrid)
    x = X.flatten()
    y = Y.flatten()
    grid = np.column_stack([np.ones(len(x)), x, y, x * y])

    z = result.predict(grid)
    Z = np.reshape(z, np.shape(X))

    contourset = ax.contourf(X, Y, Z, levels, cmap=contour_cmap, aspect='auto')
    xpoints = np.mean(dta[xvar].values.reshape(-1, 10), axis=1)
    ypoints = np.mean(dta[yvar].values.reshape(-1, 10), axis=1)
    colors = np.round(np.mean(dta['Success'].values.reshape(-1, 10), axis=1), 0)
    ax.scatter(xpoints, ypoints, s=10, c=colors, edgecolor='none', cmap=dot_cmap)
    ax.set_xlim(np.min(xgrid), np.max(xgrid))
    ax.set_ylim(np.min(ygrid), np.max(ygrid))
    ax.set_xlabel(xvar, fontsize=14)
    ax.set_ylabel(yvar, fontsize=14)
    ax.tick_params(axis='both', labelsize=12)

    return contourset

