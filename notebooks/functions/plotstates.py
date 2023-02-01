import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plotTimeSeries(Q, hidden_states, ylabel):
 
    sns.set_theme(style='white')
    fig = plt.figure()
    ax = fig.add_subplot(111)
 
    xs = np.arange(len(Q))+1909
    masks = hidden_states == 0
    ax.scatter(xs[masks], Q[masks], c='r', label='Dry State')
    masks = hidden_states == 1
    ax.scatter(xs[masks], Q[masks], c='b', label='Wet State')
    ax.plot(xs, Q, c='k')
     
    ax.set_xlabel('Year',fontsize=16)
    ax.set_ylabel(ylabel,fontsize=16)
    fig.subplots_adjust(bottom=0.2)
    matplotlib.rc('legend', fontsize = 16)
    plt.legend() 
    ax.set_xlabel("Year",fontsize=16)
    ax.set_ylabel("Annual Flow (cubic feet per year)",fontsize=16)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
 
    return None
 