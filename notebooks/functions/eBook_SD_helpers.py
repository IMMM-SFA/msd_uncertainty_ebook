import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from copy import deepcopy


def check_rdm_meet_criteria(objectives, crit_objs, crit_vals):
    """
    Determines if an objective meets a given set of criteria for a set of SOWs

    Parameters:
        objectives: np array of all objectives across a set of SOWs
        crit_objs: the column index of the objective in question
        crit_vals: an array containing [min, max] of the values

    returns:
        meets_criteria: an numpy array containing the SOWs that meet both min and max criteria

    """

    # check max and min criteria for each objective
    meet_low = objectives[:, crit_objs] >= crit_vals[0]
    meet_high = objectives[:, crit_objs] <= crit_vals[1]

    # check if max and min criteria are met at the same time
    meets_criteria = np.hstack((meet_low, meet_high)).all(axis=1)

    return meets_criteria


def create_sd_input(RDM_objectives, sat_crit):
    """
    Create a boolean array of whether each SOW meets satisfying criteria

    Rel >= 98%
    RF <= 10%
    PFC < 80%
    WCC <= 10%
    UC < 5

    Parameters:
        RDM_objectives: an array with objective values across SOWs for a given
        solution. Each row is a SOW and each column is an objective

        sat_crit: an array with the satisficing criteria (Rel, RF, PFC, WCC, UC)

    returns:
        satisficing, a boolean array containing meets/fails for each
        robustness criteria. Columns = [Util_1_Rel, Util_1_RF, Util_1_PFC, Util_1_WCC, Util_1_UC, Util_1_all,
         Util_2_Rel, Util_2_RF, Util_2_PFC, Util_2_WCC, Util_2_UC, Util_2_all,]
    """
    #  Utility 1
    util_1_rel = check_rdm_meet_criteria(RDM_objectives, [0], [sat_crit[0], 1])
    util_1_rf = check_rdm_meet_criteria(RDM_objectives, [1], [0, sat_crit[1]])
    util_1_pfc = check_rdm_meet_criteria(RDM_objectives, [3], [0, sat_crit[2]])
    util_1_wcc = check_rdm_meet_criteria(RDM_objectives, [4], [0, sat_crit[3]])
    util_1_uc = check_rdm_meet_criteria(RDM_objectives, [5], [0, sat_crit[4]])
    util_1_all = np.vstack((util_1_rel, util_1_rf, util_1_pfc, util_1_wcc, util_1_uc)).all(axis=0)

    # Utility 2
    util_2_rel = check_rdm_meet_criteria(RDM_objectives, [6], [sat_crit[0], 1])
    util_2_rf = check_rdm_meet_criteria(RDM_objectives, [7], [0, sat_crit[1]])
    util_2_pfc = check_rdm_meet_criteria(RDM_objectives, [9], [0, sat_crit[2]])
    util_2_wcc = check_rdm_meet_criteria(RDM_objectives, [10], [0, sat_crit[3]])
    util_2_uc = check_rdm_meet_criteria(RDM_objectives, [11], [0, sat_crit[4]])
    util_2_all = np.vstack((util_2_rel, util_2_rf, util_2_pfc, util_2_wcc, util_2_uc)).all(axis=0)

    indiv_satisficing = [
        util_1_rel * 1,
        util_1_rf * 1,
        util_1_pfc * 1,
        util_1_wcc * 1,
        util_1_uc * 1,
        util_1_all * 1,
        util_2_rel * 1,
        util_2_rf * 1,
        util_2_pfc * 1,
        util_2_wcc * 1,
        util_2_uc * 1,
        util_2_all * 1,
    ]

    return indiv_satisficing


def boosted_tree_sd(satisficing, rdm_factors, n_trees, tree_depth, crit_idx):
    """
    Performs boosted trees scenario discovery for a given satisficing criteria

    inputs:
        satisficing: a boolean array containing whether each SOW met
        criteria for a given solution

        rdm_factors: an array with rdm factors comprising each SOW

        n_trees: number of trees for boosting

        tree_depth: max depth of trees

    returns:
        gbc: fit classifier on all data

        gbc_2factors: classifier fit to only the top two factors for plotting

        most_imporant_rdm_factors: the top two rdm factors

        feature_importances: the percentage of leaf impurity reduction by each
        factor

    """

    gbc = GradientBoostingClassifier(n_estimators=n_trees, learning_rate=0.1, max_depth=tree_depth)

    gbc.fit(rdm_factors, satisficing[crit_idx])

    feature_importances = deepcopy(gbc.feature_importances_)
    most_influential_factors = np.argsort(feature_importances)[::-1]

    gbc_2factors = GradientBoostingClassifier(
        n_estimators=n_trees, learning_rate=0.1, max_depth=tree_depth
    )

    most_important_rdm_factors = rdm_factors[:, most_influential_factors[:2]]
    gbc_2factors.fit(most_important_rdm_factors, satisficing[crit_idx])

    return gbc, gbc_2factors, most_important_rdm_factors, feature_importances


def plot_selected_tree_maps(rob_idx, time_period, factor1_idx, factor2_idx, sat_crit, sol_num, ax):
    """
    Performs gbc classification and plots a factor map

    inputs:
        rob_idx: int, index of the criteria to print (utility 0, all is 5, 1 is 11)
        time_period: string, "Long_term", "Mid_term" or "Short_term"
        factor1_idx: index of first factor to predict performance with
        factor2_idx: index of the second factor to predict performance with
        sat_crit: an array with the satisficing criteria (Rel, RF, PFC, WCC, UC)
        sol_num: string, the number of the solution to be evaluated
        ax: the axis object to be plotted on
    """

    # load rdm file
    rdm_factors = np.loadtxt("data/DU_Factors.csv", delimiter=",")

    RDM_objectives = np.loadtxt("data/" + time_period + "_performance.csv", delimiter=",")

    # indiv_robustness = np.loadtxt('../results/DU_reevaluation/robustness_form3_' + time_period + '.csv', delimiter=',')
    indiv_robustness = 0.95
    SD_input = create_sd_input(RDM_objectives, sat_crit)

    if rob_idx == 5:
        print("Factor map for Bedford")
    elif rob_idx == 11:
        print("Factor map for Greene")
    else:
        print("Factor map for other criteria")

    rdm_names = [
        "Near-term demand\ngrowth scaling",
        "Mid-term demand\ngrowth scaling",
        "Long-term demand growth",
        "Bond term multiplier",
        "Bond interest multiplier",
        "Discount rate multiplier",
        "Restriction\n effectiveness",
        "Permitting time multiplier",
        "Construction\n time multiplier",
        "Inflow Amplitude",
        "Inflow frequency",
        "Inflow phase",
        "Average Demand Growth",
    ]

    # CHANGE!
    # if indiv_robustness[int(sol_num), rob_idx] < 0.999:
    if indiv_robustness < 0.999:
        gbc, gbc_2factors, most_important_rdm_factors, feature_importances = boosted_tree_sd(
            SD_input, rdm_factors, 500, 4, rob_idx
        )

        # predict across 2D features space
        gbc_2factors = GradientBoostingClassifier(n_estimators=500, learning_rate=0.1, max_depth=4)

        selected_factors = rdm_factors[:, [factor1_idx, factor2_idx]]
        gbc_2factors.fit(selected_factors, SD_input[rob_idx])

        # plot prediction contours
        x_data = selected_factors[:, 0]
        y_data = selected_factors[:, 1]

        x_min, x_max = (x_data.min(), x_data.max())
        y_min, y_max = (y_data.min(), y_data.max())

        xx, yy = np.meshgrid(
            np.arange(x_min, x_max * 1.001, (x_max - x_min) / 100),
            np.arange(y_min, y_max * 1.001, (y_max - y_min) / 100),
        )

        dummy_points = list(zip(xx.ravel(), yy.ravel()))

        z = gbc_2factors.predict_proba(dummy_points)[:, 1]
        z[z < 0] = 0.0
        z = z.reshape(xx.shape)

        ax.contourf(xx, yy, z, [0, 0.9, 1.0], cmap="RdBu", alpha=0.6, vmin=0.35, vmax=1.1)
        ax.scatter(
            selected_factors[:, 0],
            selected_factors[:, 1],
            c=SD_input[rob_idx],
            cmap="Reds_r",
            edgecolor="grey",
            alpha=0.6,
            s=15,
            linewidth=0.5,
        )
        xlabel = (
            rdm_names[factor1_idx] + " (" + str(int(feature_importances[factor1_idx] * 100)) + "%)"
        )
        ylabel = (
            rdm_names[factor2_idx] + " (" + str(int(feature_importances[factor2_idx] * 100)) + "%)"
        )
        ax.set_xlabel(xlabel, fontsize=12)
        ax.set_ylabel(ylabel, fontsize=12)

        ax.set_xlim([min(selected_factors[:, 0]), max(selected_factors[:, 0])])
        ax.set_ylim([min(selected_factors[:, 1]), max(selected_factors[:, 1])])

    else:
        # plot prediction contours
        x_data = rdm_factors[:, factor1_idx]
        y_data = rdm_factors[:, factor2_idx]

        x_min, x_max = (x_data.min(), x_data.max())
        y_min, y_max = (y_data.min(), y_data.max())

        xx, yy = np.meshgrid(
            np.arange(x_min, x_max * 1.001, (x_max - x_min) / 100),
            np.arange(y_min, y_max * 1.001, (y_max - y_min) / 100),
        )

        dummy_points = list(zip(xx.ravel(), yy.ravel()))

        z = np.ones(len(xx) ** 2)
        z = z.reshape(xx.shape)
        ax.contourf(xx, yy, z, [0, 0.9, 1.0], cmap="RdBu", alpha=0.6, vmin=0.0, vmax=1.1)

        ax.scatter(
            rdm_factors[:, factor1_idx],
            rdm_factors[:, factor2_idx],
            c=SD_input[rob_idx],
            cmap="Reds_r",
            edgecolor="grey",
            alpha=0.6,
            s=15,
            linewidth=0.5,
        )
        ax.set_xlabel(rdm_names[factor1_idx] + "(0%)", fontsize=8)
        ax.set_ylabel(rdm_names[factor2_idx] + "(0%)", fontsize=8)
        ax.set_xlim([min(rdm_factors[:, factor1_idx]), max(rdm_factors[:, factor1_idx])])
        ax.set_ylim([min(rdm_factors[:, factor2_idx]), max(rdm_factors[:, factor2_idx])])


def get_factor_importances(satisficing, rdm_factors, n_trees, tree_depth, crit_idx):
    """
    Performs boosted trees scenario discovery for a given satisficing criteria

    inputs:
        satisficing: a boolean array containing whether each SOW met
        criteria for a given solution

        rdm_factors: an array with rdm factors comprising each SOW

        n_trees: number of trees for boosting

        tree_depth: max depth of trees

    returns:
        feature_importances: the importances for each feature

    """

    gbc = GradientBoostingClassifier(n_estimators=n_trees, learning_rate=0.1, max_depth=tree_depth)

    gbc.fit(rdm_factors, satisficing[crit_idx])
    # print('Boosted Trees score: {}'.format(gbc.score(rdm_factors[:], satisficing[crit_idx]*1)))

    feature_importances = deepcopy(gbc.feature_importances_)

    return feature_importances


def open_exploration(utility, objective, time_period, factor1, factor2, ax):
    """
    Performs gbc classification and plots a factor map

    inputs:
        utility: str, the name of the utility to be plotted (Bedford or Greene)
        objective: str, the name of the objective to be plotted
        time_period: str, "long_term", "mid_term" or "short_term"
        factor1: str, the name of first factor to predict performance with
        factor2: str, the name of the second factor to predict performance with
        ax: the axis object to be plotted on
    """

    # process and load data

    if utility == "Bedford":
        if objective == "All" or objective == "all":
            rob_idx = 5
            print("Factor map for Bedford, all factors")
        if (
            objective == "Reliability"
            or objective == "Rel"
            or objective == "reliability"
            or objective == "rel"
        ):
            rob_idx = 0
            print("Factor map for Bedford, reliability")
        if (
            objective == "RF"
            or objective == "Restriction Frequency"
            or objective == "rf"
            or objective == "restriction frequency"
        ):
            rob_idx = 1
            print("Factor map for Bedford, restriction frequency")
        if (
            objective == "PFC"
            or objective == "Peak Financial Cost"
            or objective == "pfc"
            or objective == "peak financial cost"
        ):
            rob_idx = 2
            print("Factor map for Bedford, peak financial cost")
        if (
            objective == "WCC"
            or objective == "Worst Case Cost"
            or objective == "worst case cost"
            or objective == "wcc"
        ):
            rob_idx = 3
            print("Factor map for Bedford, worst case cost")
        if (
            objective == "UC"
            or objective == "Unit Cost"
            or objective == "uc"
            or objective == "unit cost"
        ):
            rob_idx = 4
            print("Factor map for Bedford, unit cost")
    elif utility == "Greene":
        if objective == "All" or objective == "all":
            rob_idx = 11
            print("Factor map for Greene, all factors")
        if (
            objective == "Reliability"
            or objective == "Rel"
            or objective == "reliability"
            or objective == "rel"
        ):
            rob_idx = 6
            print("Factor map for Greene, reliability")
        if (
            objective == "RF"
            or objective == "Restriction Frequency"
            or objective == "rf"
            or objective == "restriction frequency"
        ):
            rob_idx = 7
            print("Factor map for Greene, restriction frequency")
        if (
            objective == "PFC"
            or objective == "Peak Financial Cost"
            or objective == "pfc"
            or objective == "peak financial cost"
        ):
            rob_idx = 8
            print("Factor map for Greene, peak financial cost")
        if (
            objective == "WCC"
            or objective == "Worst Case Cost"
            or objective == "worst case cost"
            or objective == "wcc"
        ):
            rob_idx = 9
            print("Factor map for Greene, worst case cost")
        if (
            objective == "UC"
            or objective == "Unit Cost"
            or objective == "uc"
            or objective == "unit cost"
        ):
            rob_idx = 10
            print("Factor map for Greene, unit cost")
    else:
        print("Utility must be either 'Bedford' or 'Greene'")
        return

    # load rdm file
    rdm_factors = np.loadtxt("data/DU_Factors.csv", delimiter=",")

    RDM_objectives = np.loadtxt("data/" + time_period + "_performance.csv", delimiter=",")

    # indiv_robustness = np.loadtxt('../results/DU_reevaluation/robustness_form3_' + time_period + '.csv', delimiter=',')
    robustness = np.loadtxt("data/" + time_period + "_robustness.csv", delimiter=",")
    indiv_robustness = robustness[rob_idx]
    sat_crit = [0.98, 0.2, 0.8, 0.1, 5]
    SD_input = create_sd_input(RDM_objectives, sat_crit)

    rdm_names = [
        "Near-term demand\ngrowth scaling",
        "Mid-term demand\ngrowth scaling",
        "Long-term demand growth",
        "Bond term multiplier",
        "Bond interest multiplier",
        "Discount rate multiplier",
        "Restriction\n effectiveness",
        "Permitting time multiplier",
        "Construction\n time multiplier",
        "Inflow Amplitude",
        "Inflow frequency",
        "Inflow phase",
        "Average Demand Growth",
    ]

    # Dictionary with DU factor Keys
    DU_Factors = {
        "D1": 0,
        "D2": 1,
        "D3": 2,
        "BT": 3,
        "BM": 4,
        "DR": 5,
        "RE": 6,
        "PM": 7,
        "CT": 7,
        "IA": 9,
        "IF": 10,
        "IP": 11,
    }

    factor1_idx = DU_Factors[factor1]
    factor2_idx = DU_Factors[factor2]

    if indiv_robustness < 0.9999:
        gbc, gbc_2factors, most_important_rdm_factors, feature_importances = boosted_tree_sd(
            SD_input, rdm_factors, 500, 4, rob_idx
        )

        # predict across 2D features space
        gbc_2factors = GradientBoostingClassifier(n_estimators=500, learning_rate=0.1, max_depth=4)

        selected_factors = rdm_factors[:, [factor1_idx, factor2_idx]]
        gbc_2factors.fit(selected_factors, SD_input[rob_idx])

        # plot prediction contours
        x_data = selected_factors[:, 0]
        y_data = selected_factors[:, 1]

        x_min, x_max = (x_data.min(), x_data.max())
        y_min, y_max = (y_data.min(), y_data.max())

        xx, yy = np.meshgrid(
            np.arange(x_min, x_max * 1.001, (x_max - x_min) / 100),
            np.arange(y_min, y_max * 1.001, (y_max - y_min) / 100),
        )

        dummy_points = list(zip(xx.ravel(), yy.ravel()))

        z = gbc_2factors.predict_proba(dummy_points)[:, 1]
        z[z < 0] = 0.0
        z = z.reshape(xx.shape)

        ax.contourf(xx, yy, z, [0, 0.9, 1.0], cmap="RdBu", alpha=0.6, vmin=0.35, vmax=1.1)
        ax.scatter(
            selected_factors[:, 0],
            selected_factors[:, 1],
            c=SD_input[rob_idx],
            cmap="Reds_r",
            edgecolor="grey",
            alpha=0.6,
            s=15,
            linewidth=0.5,
        )
        xlabel = (
            rdm_names[factor1_idx] + " (" + str(int(feature_importances[factor1_idx] * 100)) + "%)"
        )
        ylabel = (
            rdm_names[factor2_idx] + " (" + str(int(feature_importances[factor2_idx] * 100)) + "%)"
        )
        ax.set_xlabel(xlabel, fontsize=12)
        ax.set_ylabel(ylabel, fontsize=12)

        ax.set_xlim([min(selected_factors[:, 0]), max(selected_factors[:, 0])])
        ax.set_ylim([min(selected_factors[:, 1]), max(selected_factors[:, 1])])

    else:
        # plot prediction contours
        x_data = rdm_factors[:, factor1_idx]
        y_data = rdm_factors[:, factor2_idx]

        x_min, x_max = (x_data.min(), x_data.max())
        y_min, y_max = (y_data.min(), y_data.max())

        xx, yy = np.meshgrid(
            np.arange(x_min, x_max * 1.001, (x_max - x_min) / 100),
            np.arange(y_min, y_max * 1.001, (y_max - y_min) / 100),
        )

        dummy_points = list(zip(xx.ravel(), yy.ravel()))

        z = np.ones(len(xx) ** 2)
        z = z.reshape(xx.shape)
        ax.contourf(xx, yy, z, [0, 0.9, 1.0], cmap="RdBu", alpha=0.6, vmin=0.0, vmax=1.1)

        ax.scatter(
            rdm_factors[:, factor1_idx],
            rdm_factors[:, factor2_idx],
            c="white",
            edgecolor="grey",
            alpha=0.6,
            s=15,
            linewidth=0.5,
        )
        ax.set_xlabel(rdm_names[factor1_idx] + "(0%)", fontsize=12)
        ax.set_ylabel(rdm_names[factor2_idx] + "(0%)", fontsize=12)
        ax.set_xlim([min(rdm_factors[:, factor1_idx]), max(rdm_factors[:, factor1_idx])])
        ax.set_ylim([min(rdm_factors[:, factor2_idx]), max(rdm_factors[:, factor2_idx])])
