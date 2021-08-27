Plotting Code Samples
*********************

hymod.ipynb
---------------------------------------

The following are the plotting functions as described in the ``hymod.ipynb`` Jupyter notebook tutorial.

The following are the necessary package imports to run these functions:

.. code-block:: python

    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

    from matplotlib.lines import Line2D


**plot_observed_vs_simulated_streamflow()**
___________________________________________

.. code-block:: python

    def plot_observed_vs_simulated_streamflow(df, hymod_dict, figsize=[12, 6]):
        """Plot observed versus simulated streamflow.

        :param df:              Dataframe of hymod input data including columns for precip, potential evapotranspiration,
                                and streamflow

        :param hymod_dict:      A dictionary of hymod outputs
        :type hymod_dict:       dict

        :param figsize:         Matplotlib figure size
        :type figsize:          list

        """

        # set plot style
        plt.style.use('seaborn-white')

        # set up figure
        fig, ax = plt.subplots(figsize=figsize)

        # plot observed streamflow
        ax.plot(range(0, len(df['Strmflw'])), df['Strmflw'], color='pink')

        # plot simulated streamflow
        ax.plot(range(0, len(df['Strmflw'])), hymod_dict['Q'], color='black')

        # set axis labels
        ax.set_ylabel('Streamflow($m^3/s$)')
        ax.set_xlabel('Days')

        # set plot title
        plt.title('Observed vs. Simulated Streamflow')

        return ax


**plot_observed_vs_sensitivity_streamflow()**
_____________________________________________

.. code-block:: python

    def plot_observed_vs_sensitivity_streamflow(df_obs, df_sim, figsize=[10, 4]):
        """Plot observed streamflow versus simulations generated from sensitivity analysis.

        :param df_obs:          Dataframe of mean monthly hymod input data including columns for precip,
                                potential evapotranspiration, and streamflow

        :param df_sim:          Dataframe of mean monthly simulation data from sensitivity analysis

        :param figsize:         Matplotlib figure size
        :type figsize:          list

        """

        month_list = range(len(df_sim))

        # set up figure
        fig, ax = plt.subplots(figsize=figsize)

        # set labels
        ax.set_xlabel('Days')
        ax.set_ylabel('Flow Discharge (m^3/s)')

        # plots all simulated streamflow cases under different sample sets
        for i in df_sim.columns:
            plt.plot(month_list, df_sim[i], color="pink", alpha=0.2)

        # plot observed streamflow
        plt.plot(month_list, df_obs['Strmflw'], color="black")

        plt.title('Observed vs. Sensitivity Analysis Outputs')

        return ax


**plot_monthly_heatmap()**
__________________________

.. code-block:: python

    def plot_monthly_heatmap(arr_sim, df_obs, title='', figsize=[14, 6]):
        """Plot a sensitivity metric overlain by observed flow.

        :param arr_sim:         Numpy array of simulated metrics

        :param df_obs:          Dataframe of mean monthly observed data from sensitivity analysis

        :param title:           Title of plot
        :type title:            str

        :param figsize:         Matplotlib figure size
        :type figsize:          list

        """

        # set up figure
        fig, ax = plt.subplots(figsize=figsize)

        # plot heatmap
        sns.heatmap(arr_sim,
                    ax=ax,
                    yticklabels=['Kq', 'Ks', 'Alp', 'Huz', 'B'],
                    cmap=sns.color_palette("ch:s=-.2,r=.6"))

        # setup overlay axis
        ax2 = ax.twinx()

        # plot line
        ax2.plot(np.arange(0.5, 12.5), df_obs['Strmflw'], color='slateblue')

        # plot points on line
        ax2.plot(np.arange(0.5, 12.5), df_obs['Strmflw'], color='slateblue', marker='o')

        # set axis limits and labels
        ax.set_ylim(0, 5)
        ax.set_xlim(0, 12)
        ax.set_xticklabels(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
        ax2.set_ylabel('Flow Discharge($m^3/s$)')

        plt.title(title)

        plt.show()

        return ax, ax2


**plot_annual_heatmap()**
__________________________

.. code-block:: python

    def plot_annual_heatmap(arr_sim, df_obs, title='', figsize=[14,5]):
        """Plot a sensitivity metric overlain by observed flow..

        :param arr_sim:         Numpy array of simulated metrics

        :param df_obs:          Dataframe of mean monthly observed data from sensitivity analysis

        :param title:           Title of plot
        :type title:            str

        :param figsize:         Matplotlib figure size
        :type figsize:          list

        """

        # set up figure
        fig, ax = plt.subplots(figsize=figsize)

        # plot heatmap
        sns.heatmap(arr_sim, ax=ax, cmap=sns.color_palette("YlOrBr"))

        # setup overlay axis
        ax2 = ax.twinx()

        # plot line
        ax2.plot(np.arange(0.5, 10.5), df_obs['Strmflw'], color='slateblue')

        # plot points on line
        ax2.plot(np.arange(0.5, 10.5), df_obs['Strmflw'], color='slateblue', marker='o')

        # set up axis lables and limits
        ax.set_ylim(0, 5)
        ax.set_xlim(0, 10)
        ax.set_yticklabels(['Kq', 'Ks', 'Alp', 'Huz', 'B'])
        ax.set_xticklabels(range(2000, 2010))
        ax2.set_ylabel('Flow Discharge($m^3/s$)')

        plt.title(title)

        return ax, ax2


**plot_varying_heatmap()**
___________________________

.. code-block:: python

    def plot_varying_heatmap(arr_sim, df_obs, title='', figsize=[14,5]):
        """Plot a sensitivity metric overlain by observed flow..

        :param arr_sim:         Numpy array of simulated metrics

        :param df_obs:          Dataframe of mean monthly observed data from sensitivity analysis

        :param title:           Title of plot
        :type title:            str

        :param figsize:         Matplotlib figure size
        :type figsize:          list

        """

        # set up figure
        fig, ax = plt.subplots(figsize=figsize)

        # plot heatmap
        sns.heatmap(arr_sim,
                    ax=ax,
                    yticklabels=['Kq', 'Ks', 'Alp', 'Huz', 'B'],
                    cmap=sns.light_palette("seagreen", as_cmap=True))

        n_years = df_obs.shape[0]

        # setup overlay axis
        ax2 = ax.twinx()

        # plot line
        ax2.plot(range(0, n_years), df_obs['Strmflw'], color='slateblue')

        # plot points on line
        ax2.plot(range(0, n_years), df_obs['Strmflw'], color='slateblue', marker='o')

        # set up axis lables and limits
        ax.set_ylim(0, 5)
        ax.set_xlim(-0.5, 119.5)
        ax2.set_ylabel('Flow Discharge')
        ax.set_xlabel('Number of Months')

        plt.title(title)

        return ax, ax2


**plot_precalibration_flow()**
_______________________________

.. code-block:: python

    def plot_precalibration_flow(df_sim, df_obs, figsize=[10, 4]):
        """Plot flow discharge provided by the ensemble of parameters sets from Pre-Calibration versus the observed
        flow data.

        :param df_sim:          Dataframe of simulated metrics

        :param df_obs:          Dataframe of mean monthly observed data from sensitivity analysis

        :param figsize:         Matplotlib figure size
        :type figsize:          list

        """

        # set up figure
        fig, ax = plt.subplots(figsize=figsize)

        # set axis labels
        ax.set_xlabel('Days')
        ax.set_ylabel('Flow Discharge')

        # plot pre-calibration results
        for i in range(df_sim.shape[1]):
            plt.plot(range(len(df_sim)), df_sim.iloc[:, i],  color="lightgreen", alpha=0.2)

        # plot observed
        plt.plot(range(len(df_sim)), df_obs['Strmflw'],  color="black")

        plt.title('Observed vs. Pre-Calibration Outputs')

        # customize legend
        custom_lines = [Line2D([0], [0],  color="lightgreen", lw=4),
                        Line2D([0], [0], color="black", lw=4)]
        plt.legend(custom_lines, ['Pre-Calibration', 'Observed'])

        return ax


**plot_precalibration_glue()**
_______________________________

.. code-block:: python

    def plot_precalibration_glue(df_precal, df_glue, df_obs, figsize=[10, 4]):
        """Plot flow discharge provided by the ensemble of parameters sets from Pre-Calibration versus the observed
        flow data.

        :param df_sim:          Dataframe of simulated metrics

        :param df_obs:          Dataframe of mean monthly observed data from sensitivity analysis

        :param figsize:         Matplotlib figure size
        :type figsize:          list

        """

        # set up figure
        fig, ax = plt.subplots(figsize=figsize)

        # set axis labels
        ax.set_xlabel('Days')
        ax.set_ylabel('Flow Discharge')

        # plot pre-calibration results
        for i in range(df_precal.shape[1]):
            plt.plot(range(len(df_precal)), df_precal.iloc[:, i],  color="lightgreen", alpha=0.2)

        # plot glue
        for i in range(df_glue.shape[1]):
            plt.plot(range(len(df_glue)), df_glue.iloc[:, i], color="lightblue", alpha=0.2)

        # plot observed
        plt.plot(range(len(df_precal)), df_obs['Strmflw'],  color="black")

        plt.title('Observed vs. Sensitivity Analysis Outputs across GLUE/Pre-Calibration')

        # customize legend
        custom_lines = [Line2D([0], [0],  color="lightgreen", lw=4),
                        Line2D([0], [0], color="lightblue", lw=4),
                        Line2D([0], [0], color="black", lw=4)]
        plt.legend(custom_lines, ['Pre-Calibration', 'GLUE', 'Observed'])

        return ax


fishery_dynamics.ipynb
---------------------------------------

The following are the plotting functions as described in the ``fishery_dynamics.ipynb`` Jupyter notebook tutorial.

The following are the necessary package imports to run these functions:

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt

    from matplotlib import patheffects as pe


**plot_objective_performance()**
_________________________________

.. code-block:: python

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


**plot_factor_performance()**
_________________________________

.. code-block:: python

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
