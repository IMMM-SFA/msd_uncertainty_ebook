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
