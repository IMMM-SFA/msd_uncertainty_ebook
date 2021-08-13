import numpy as np
import itertools
import matplotlib.pyplot as plt
from matplotlib import patheffects as pe


def inequality(b, m, h, K):

    return (b**m) / (h*K)**(1-m)


def plot_uncertainty_relationship(param_values, collapse_days):
    """Explore the relationship between uncertain factors and performance."""

    b = np.linspace(start=0.005, stop=1, num=1000)
    m = np.linspace(start=0.1, stop=1.5, num=1000)
    h = np.linspace(start=0.001, stop=1, num=1000)
    K = np.linspace(start=100, stop=2000, num=1000)
    b, m = np.meshgrid(b, m)
    a = inequality(b, m, h, K)
    a = a.clip(0, 2)

    cmap = plt.cm.get_cmap("RdBu_r")

    fig = plt.figure(figsize=plt.figaspect(0.5), dpi=600, constrained_layout=True)

    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    sows = ax1.scatter(param_values[:,1], param_values[:,6], param_values[:,0], c=collapse_days[:,0], cmap=cmap, s=0.5)
    pts_ineq = ax1.plot_surface(b, m, a, color='black', alpha=0.25, zorder=1)
    pt_ref = ax1.scatter(0.5,0.7,0.005, c='black', s=50, zorder=0)
    sm = plt.cm.ScalarMappable(cmap=cmap)
    ax1.set_xlabel("b")
    ax1.set_ylabel("m")
    ax1.set_zlabel("a")
    ax1.set_zlim([0.0,2.0])
    ax1.set_xlim([0.0,1.0])
    ax1.set_ylim([0.0,1.5])
    ax1.xaxis.set_view_interval(0,  0.5)
    ax1.set_facecolor('white')
    ax1.view_init(12, -17)
    ax1.set_title('Profit maximizing policy')

    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    sows = ax2.scatter(param_values[:,1], param_values[:,6], param_values[:,0], c=collapse_days[:,1], cmap=cmap, s=0.5)
    pts_ineq = ax2.plot_surface(b, m, a, color='black', alpha=0.25, zorder=1)
    pt_ref = ax2.scatter(0.5,0.7,0.005, c='black', s=50, zorder=0)
    sm = plt.cm.ScalarMappable(cmap=cmap)
    ax2.set_xlabel("b")
    ax2.set_ylabel("m")
    ax2.set_zlabel("a")
    ax2.set_zlim([0.0,2.0])
    ax2.set_xlim([0.0,1.0])
    ax2.set_ylim([0.0,1.5])
    ax2.xaxis.set_view_interval(0,  0.5)
    ax2.set_facecolor('white')
    ax2.view_init(12, -17)
    ax2.set_title('Robust policy')

    sm = plt.cm.ScalarMappable(cmap=cmap)
    sm.set_array([collapse_days.min(), collapse_days.max()])
    cbar = fig.colorbar(sm)
    cbar.set_label('Days with predator collapse')


def plot_solutions(objective_performance, profit_solution, robust_solution):
    """Plot the identified solutions with regards to their objective performance."""

    fig = plt.figure(figsize=(18, 9))  # create the figure
    ax = fig.add_subplot(1, 1, 1)  # make axes to plot on

    objs_labels = ['Net present\nvalue (NPV)',
                   'Prey population deficit',
                   'Longest duration\nof low harvest',
                   'Worst harvest instance',
                   'Variance of harvest',
                   'Duration of predator\npopulation collapse']  # Constraint (always 0)

    # Normalization across objectives
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

    cmap = plt.cm.get_cmap("Blues")

    # Plot all solutions
    for i in range(len(norm_reference[:, 0])):
        ys = np.append(norm_reference[i, :], 1.0)
        xs = range(len(ys))
        ax.plot(xs, ys, c=cmap(ys[0]), linewidth=2)

    # To highlight robust solutions
    ys = np.append(norm_reference[profit_solution, :], 1.0)  # Most profitable
    xs = range(len(ys))
    l1 = ax.plot(xs[0:6], ys[0:6], c=cmap(ys[0]), linewidth=3, label='Most robust in NPV',
                 path_effects=[pe.Stroke(linewidth=6, foreground='darkgoldenrod'), pe.Normal()])
    ys = np.append(norm_reference[robust_solution, :], 1.0)  # Most robust in all criteria
    xs = range(len(ys))
    l2 = ax.plot(xs[0:6], ys[0:6], c=cmap(ys[0]), linewidth=3, label='Most robust across criteria',
                 path_effects=[pe.Stroke(linewidth=6, foreground='gold'), pe.Normal()])

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap)
    sm.set_array([objective_performance[:, 0].min(), objective_performance[:, 0].max()])
    cbar = fig.colorbar(sm)
    cbar.ax.set_ylabel("\nNet present value (NPV)")

    # Tick values
    minvalues = ["{0:.3f}".format(mins[0]), "{0:.3f}".format(-mins[1]),
                 str(-mins[2]), "{0:.3f}".format(-mins[3]), "{0:.2f}".format(-mins[4]), str(0)]
    maxvalues = ["{0:.2f}".format(maxs[0]), "{0:.3f}".format(-maxs[1]),
                 str(-maxs[2]), "{0:.2f}".format(maxs[3]), "{0:.2f}".format(-maxs[4]), str(0)]

    ax.set_ylabel("Preference ->", size=12)
    ax.set_yticks([])
    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.set_xticklabels([minvalues[i] + '\n' + objs_labels[i] for i in range(len(objs_labels))])

    # make a twin axis for toplabels
    ax1 = ax.twiny()
    ax1.set_yticks([])
    ax1.set_xticks([0, 1, 2, 3, 4, 5])
    ax1.set_xticklabels([maxvalues[i] for i in range(len(maxs)+1)])

    return ax1


def fish_game(vars, additional_inputs, N=100, tSteps=100, nObjs=5, nCnstr=1):
    """Define the problem to be solved.

    :param vars:                        contains all C, R, W
    :param additional_inputs:           contains defined management strategy and SOW params
    :param N:                           Number of realizations of environmental stochasticity
    :param tSteps:                      no. of timesteps to run the fish game on
    :param nObjs:                       no. of objectives in output
    :param nCnstr:                      no. of objectives in output

    """
    # Get chosen strategy
    strategy = additional_inputs[0]

    # Get system behavior parameters (need to convert from string to float)
    a = float(additional_inputs[1])
    b = float(additional_inputs[2])
    c = float(additional_inputs[3])
    d = float(additional_inputs[4])
    h = float(additional_inputs[5])
    K = float(additional_inputs[6])
    m = float(additional_inputs[7])
    sigmaX = float(additional_inputs[8])
    sigmaY = float(additional_inputs[9])

    x = np.zeros(tSteps + 1)  # Create prey population array
    y = np.zeros(tSteps + 1)  # Create predator population array
    z = np.zeros(tSteps + 1)  # Create harvest array

    # Create array to store harvest for all realizations
    harvest = np.zeros([N, tSteps + 1])

    # Create array to store effort for all realizations
    effort = np.zeros([N, tSteps + 1])

    # Create array to store prey for all realizations
    prey = np.zeros([N, tSteps + 1])

    # Create array to store predator for all realizations
    predator = np.zeros([N, tSteps + 1])

    # Create array to store metrics per realization
    NPV = np.zeros(N)
    cons_low_harv = np.zeros(N)
    harv_1st_pc = np.zeros(N)
    variance = np.zeros(N)

    # Create arrays to store objectives and constraints
    objs = [0.0] * nObjs
    cnstr = [0.0] * nCnstr

    # Create array with environmental stochasticity for prey
    epsilon_prey = np.random.normal(0.0, sigmaX, N)

    # Create array with environmental stochasticity for predator
    epsilon_predator = np.random.normal(0.0, sigmaY, N)

    # Go through N possible realizations
    for i in range(N):

        # Initialize populations and values
        x[0] = prey[i, 0] = K
        y[0] = predator[i, 0] = 250
        z[0] = effort[i, 0] = hrvSTR([x[0]], vars, [[0, K]], [[0, 1]])
        NPVharvest = harvest[i, 0] = effort[i, 0] * x[0]

        # Go through all timesteps for prey, predator, and harvest
        for t in range(tSteps):

            if x[t] > 0 and y[t] > 0:

                x[t + 1] = (x[t] + b * x[t] * (1 - x[t] / K) - (a * x[t] * y[t]) / (np.power(y[t], m) + a * h * x[t]) -
                            z[t] * x[t]) * np.exp(epsilon_prey[i])  # Prey growth equation
                y[t + 1] = (y[t] + c * a * x[t] * y[t] / (np.power(y[t], m) + a * h * x[t]) - d * y[t]) * np.exp(
                    epsilon_predator[i])  # Predator growth equation

                if t <= tSteps - 1:

                    if strategy == 'Previous_Prey':
                        input_ranges = [[0, K]]  # Prey pop. range to use for normalization
                        output_ranges = [[0, 1]]  # Range to de-normalize harvest to
                        z[t + 1] = hrvSTR([x[t]], vars, input_ranges, output_ranges)

            prey[i, t + 1] = x[t + 1]
            predator[i, t + 1] = y[t + 1]
            effort[i, t + 1] = z[t + 1]
            harvest[i, t + 1] = z[t + 1] * x[t + 1]
            NPVharvest = NPVharvest + harvest[i, t + 1] * (1 + 0.05) ** (-(t + 1))

        NPV[i] = NPVharvest
        low_hrv = [harvest[i, j] < prey[i, j] / 20 for j in
                   range(len(harvest[i, :]))]  # Returns a list of True values when there's harvest below 5%

        count = [sum(1 for _ in group) for key, group in itertools.groupby(low_hrv) if
                 key]  # Counts groups of True values in a row

        if count:  # Checks if theres at least one count (if not, np.max won't work on empty list)
            cons_low_harv[i] = np.max(count)  # Finds the largest number of consecutive low harvests
        else:
            cons_low_harv[i] = 0

        harv_1st_pc[i] = np.percentile(harvest[i, :], 1)
        variance[i] = np.var(harvest[i, :])

    # Calculate objectives across N realizations
    objs[0] = -np.mean(NPV)  # Mean NPV for all realizations
    objs[1] = np.mean((K - prey) / K)  # Mean prey deficit
    objs[2] = np.mean(cons_low_harv)  # Mean worst case of consecutive low harvest across realizations
    objs[3] = -np.mean(harv_1st_pc)  # Mean 1st percentile of all harvests
    objs[4] = np.mean(variance)  # Mean variance of harvest

    cnstr[0] = np.mean((predator < 1).sum(axis=1))  # Mean number of predator extinction days per realization

    return objs, cnstr


def hrvSTR(Inputs, vars, input_ranges, output_ranges, nRBF=2, nIn=1, nOut=1 ):
    """Calculate outputs (u) corresponding to each sample of inputs
    u is a 2-D matrix with nOut columns (1 for each output) and as many rows as
    there are samples of inputs

    :param Inputs:
    :param vars:
    :param input_ranges:
    :param output_ranges:
    :param nRBF:                                    no. of RBFs to use
    :param nIn:                                     no. of inputs (depending on
                                                    selected strategy)
    :param nOut:                                    no. of outputs (depending on
                                                    selected strategy)
    :param N:

    :return:

    """

    # Rearrange decision variables into C, R, and W arrays
    # C and R are nIn x nRBF and W is nOut x nRBF
    # Decision variables are arranged in 'vars' as nRBF consecutive
    # sets of {nIn pairs of {C, R} followed by nOut Ws}
    # E.g. for nRBF = 2, nIn = 3 and nOut = 4:
    # C, R, C, R, C, R, W, W, W, W, C, R, C, R, C, R, W, W, W, W
    C = np.zeros([nIn, nRBF])
    R = np.zeros([nIn, nRBF])
    W = np.zeros([nOut, nRBF])
    for n in range(nRBF):
        for m in range(nIn):
            C[m, n] = vars[(2 * nIn + nOut) * n + 2 * m]
            R[m, n] = vars[(2 * nIn + nOut) * n + 2 * m + 1]
        for k in range(nOut):
            W[k, n] = vars[(2 * nIn + nOut) * n + 2 * nIn + k]

    # Normalize weights to sum to 1 across the RBFs (each row of W should sum to 1)
    totals = np.sum(W, 1)
    for k in range(nOut):
        if totals[k] > 0:
            W[k, :] = W[k, :] / totals[k]

    # Normalize inputs
    norm_in = np.zeros(nIn)
    for m in range(nIn):
        norm_in[m] = (Inputs[m] - input_ranges[m][0]) / (input_ranges[m][1] - input_ranges[m][0])

    # Create array to store outputs
    u = np.zeros(nOut)

    # Calculate RBFs
    for k in range(nOut):

        for n in range(nRBF):
            BF = 0

            for m in range(nIn):
                if R[m, n] > 10 ** -6:  # set so as to avoid division by 0
                    BF = BF + ((norm_in[m] - C[m, n]) / R[m, n]) ** 2
                else:
                    BF = BF + ((norm_in[m] - C[m, n]) / (10 ** -6)) ** 2

            u[k] = u[k] + W[k, n] * np.exp(-BF)

    # De-normalize outputs
    norm_u = np.zeros(nOut)

    for k in range(nOut):
        norm_u[k] = output_ranges[k][0] + u[k] * (output_ranges[k][1] - output_ranges[k][0])

    return norm_u
