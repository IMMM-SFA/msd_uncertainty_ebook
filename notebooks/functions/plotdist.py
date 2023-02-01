from scipy import stats as ss
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def plotDistribution(Q, mus, sigmas, P):
 
    # calculate stationary distribution
    eigenvals, eigenvecs = np.linalg.eig(np.transpose(P))
    one_eigval = np.argmin(np.abs(eigenvals-1))
    pi = eigenvecs[:,one_eigval] / np.sum(eigenvecs[:,one_eigval])
 
    x_0 = np.linspace(mus[0]-4*sigmas[0], mus[0]+4*sigmas[0], 10000)
    fx_0 = pi[0]*ss.norm.pdf(x_0,mus[0],sigmas[0])
 
    x_1 = np.linspace(mus[1]-4*sigmas[1], mus[1]+4*sigmas[1], 10000)
    fx_1 = pi[1]*ss.norm.pdf(x_1,mus[1],sigmas[1])
 
    x = np.linspace(mus[0]-4*sigmas[0], mus[1]+4*sigmas[1], 10000)
    fx = pi[0]*ss.norm.pdf(x,mus[0],sigmas[0]) + \
        pi[1]*ss.norm.pdf(x,mus[1],sigmas[1])
 
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(Q, color='k', alpha=0.5, density=True)
    l1, = ax.plot(x_0, fx_0, c='r', linewidth=2, label='Dry State Distn')
    l2, = ax.plot(x_1, fx_1, c='b', linewidth=2, label='Wet State Distn')
    l3, = ax.plot(x, fx, c='k', linewidth=2, label='Combined State Distn')
 
    fig.subplots_adjust(bottom=0.15)
    handles, labels = plt.gca().get_legend_handles_labels()
    matplotlib.rc('legend', fontsize = 16)
    plt.legend() 
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    return None