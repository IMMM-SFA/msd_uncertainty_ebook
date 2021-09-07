import numpy as np
import matplotlib.pyplot as plt

from matplotlib import patheffects as pe


def plot_objective_performance(objective_performance, profit_solution, robust_solution, figsize=(18, 9)):
    """Plot the identified solutions with regards to their objective performance
    in a parallel axis plot

    :param objective_performance:               Objective performance array
    :param profit_solution:                     Profitable solutions array
    :param robust_solution:                     Robust solutions array
    :param figsize:                             Figure size
    :type figsize:                              tuple

    """

    # create the figure object
    fig = plt.figure(figsize=figsize)

    # set up subplot axis object
    ax = fig.add_subplot(1, 1, 1)

    # labels where constraint is always 0
    objs_labels = ['Net present\nvalue (NPV)',
                   'Prey population deficit',
                   'Longest duration\nof low harvest',
                   'Worst harvest instance',
                   'Variance of harvest',
                   'Duration of predator\npopulation collapse']

    # normalization across objectives
    mins = objective_performance.min(axis=0)
    maxs = objective_performance.max(axis=0)
    norm_reference = objective_performance.copy()

    for i in range(5):
        mm = objective_performance[:, i].min()
        mx = objective_performance[:, i].max()
        if mm != mx:
            norm_reference[:, i] = (objective_performance[:, i] - mm) / (mx - mm)
        else:
            norm_reference[:, i] = 1

    # colormap from matplotlib
    cmap = plt.cm.get_cmap("Blues")

    # plot all solutions
    for i in range(len(norm_reference[:, 0])):
        ys = np.append(norm_reference[i, :], 1.0)
        xs = range(len(ys))
        ax.plot(xs, ys, c=cmap(ys[0]), linewidth=2)

    # to highlight robust solutions
    ys = np.append(norm_reference[profit_solution, :], 1.0)  # Most profitable
    xs = range(len(ys))
    l1 = ax.plot(xs[0:6],
                 ys[0:6],
                 c=cmap(ys[0]),
                 linewidth=3,
                 label='Most robust in NPV',
                 path_effects=[pe.Stroke(linewidth=6, foreground='darkgoldenrod'), pe.Normal()])

    ys = np.append(norm_reference[robust_solution, :], 1.0)  # Most robust in all criteria
    xs = range(len(ys))
    l2 = ax.plot(xs[0:6],
                 ys[0:6],
                 c=cmap(ys[0]),
                 linewidth=3,
                 label='Most robust across criteria',
                 path_effects=[pe.Stroke(linewidth=6, foreground='gold'), pe.Normal()])

    # build colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap)
    sm.set_array([objective_performance[:, 0].min(), objective_performance[:, 0].max()])
    cbar = fig.colorbar(sm)
    cbar.ax.set_ylabel("\nNet present value (NPV)")

    # tick values
    minvalues = ["{0:.3f}".format(mins[0]),
                 "{0:.3f}".format(-mins[1]),
                 str(-mins[2]),
                 "{0:.3f}".format(-mins[3]),
                 "{0:.2f}".format(-mins[4]),
                 str(0)]

    maxvalues = ["{0:.2f}".format(maxs[0]),
                 "{0:.3f}".format(-maxs[1]),
                 str(-maxs[2]),
                 "{0:.2f}".format(maxs[3]),
                 "{0:.2f}".format(-maxs[4]),
                 str(0)]

    ax.set_ylabel("Preference ->", size=12)
    ax.set_yticks([])
    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.set_xticklabels([minvalues[i] + '\n' + objs_labels[i] for i in range(len(objs_labels))])

    # make a twin axis for toplabels
    ax1 = ax.twiny()
    ax1.set_yticks([])
    ax1.set_xticks([0, 1, 2, 3, 4, 5])
    ax1.set_xticklabels([maxvalues[i] for i in range(len(maxs) + 1)])

    return ax, ax1


def plot_factor_performance(param_values, collapse_days, b, m, a):
    """Visualize the performance of our policies in three-dimensional
    parametric space.

    :param param_values:                Saltelli sample array
    :param collapse_days:               Simulation array
    :param b:                           b parameter boundary interval
    :param m:                           m parameter boundary interval
    :param a:                           a parameter boundary interval

    """

    # set colormap
    cmap = plt.cm.get_cmap("RdBu_r")

    # build figure object
    fig = plt.figure(figsize=plt.figaspect(0.5), dpi=600, constrained_layout=True)

    # set up scalable colormap
    sm = plt.cm.ScalarMappable(cmap=cmap)

    # set up subplot for profit maximizing policy
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')

    # add point data for profit plot
    sows = ax1.scatter(param_values[:,1],
                       param_values[:,6],
                       param_values[:,0],
                       c=collapse_days[:,0],
                       cmap=cmap,
                       s=0.5)

    # add surface data for boundary separating successful and failed states of the world
    pts_ineq = ax1.plot_surface(b, m, a, color='black', alpha=0.25, zorder=1)

    # add reference point to plot
    pt_ref = ax1.scatter(0.5, 0.7, 0.005, c='black', s=50, zorder=0)

    # set up plot aesthetics and labels
    ax1.set_xlabel("b")
    ax1.set_ylabel("m")
    ax1.set_zlabel("a")
    ax1.set_zlim([0.0, 2.0])
    ax1.set_xlim([0.0, 1.0])
    ax1.set_ylim([0.0, 1.5])
    ax1.xaxis.set_view_interval(0,  0.5)
    ax1.set_facecolor('white')
    ax1.view_init(12, -17)
    ax1.set_title('Profit maximizing policy')

    # set up subplot for robust policy
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')

    # add point data for robust plot
    sows = ax2.scatter(param_values[:,1],
                       param_values[:,6],
                       param_values[:,0],
                       c=collapse_days[:,1],
                       cmap=cmap,
                       s=0.5)

    # add surface data for boundary separating successful and failed states of the world
    pts_ineq = ax2.plot_surface(b, m, a, color='black', alpha=0.25, zorder=1)

    # add reference point to plot
    pt_ref = ax2.scatter(0.5, 0.7, 0.005, c='black', s=50, zorder=0)

    # set up plot aesthetics and labels
    ax2.set_xlabel("b")
    ax2.set_ylabel("m")
    ax2.set_zlabel("a")
    ax2.set_zlim([0.0, 2.0])
    ax2.set_xlim([0.0, 1.0])
    ax2.set_ylim([0.0, 1.5])
    ax2.xaxis.set_view_interval(0, 0.5)
    ax2.set_facecolor('white')
    ax2.view_init(12, -17)
    ax2.set_title('Robust policy')

    # set up colorbar
    sm.set_array([collapse_days.min(), collapse_days.max()])
    cbar = fig.colorbar(sm)
    cbar.set_label('Days with predator collapse')

    return ax1, ax2

