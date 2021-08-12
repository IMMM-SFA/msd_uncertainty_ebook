import numpy as np
import itertools

nRBF = 2  # no. of RBFs to use
nIn = 1  # no. of inputs (depending on selected strategy)
nOut = 1  # no. of outputs (depending on selected strategy)

N = 100  # Number of realizations of environmental stochasticity

tSteps = 100  # no. of timesteps to run the fish game on

nObjs = 5  # no. of objectives in output
nCnstr = 1  # no. of objectives in output


# Define problem to be solved
def fish_game(vars,  # contains all C, R, W
              additional_inputs  # Contains defined management strategy and SOW params
              ):
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


# Calculate outputs (u) corresponding to each sample of inputs
# u is a 2-D matrix with nOut columns (1 for each output)
# and as many rows as there are samples of inputs
def hrvSTR(Inputs, vars, input_ranges, output_ranges):
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