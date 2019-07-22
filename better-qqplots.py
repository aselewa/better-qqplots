import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
plt.style.use('classic')

def qqplot_unif(y, ax=None):
    '''
    Plots a quantile-quantile plot for the uniform distribution with 95% CI band based on the distribution of order statistics
    '''
    N = len(y)
    y = -np.log10(np.sort(y))
    rank = np.arange(1,N+1,1)
    x = -np.log10(rank/N)
    
    alpha = 0.05
    n = N - rank + 1
    lowr = -np.log10(stats.beta.ppf(alpha/2, rank, n))
    uppr = -np.log10(stats.beta.ppf(1-(alpha/2), rank, n))
    
    qq_plotter(x, y, lowr, uppr, ax)
    
def qqplot_norm(y, ax=None):
    '''
    Plots a quantile-quantile plot for the normal distribution with 95% CI band based on the distribution of order statistics
    '''
    pass

def qq_plotter(x, y, lowr, uppr, ax):
    '''
    Helper function for setting up main figure
    x : expected quantiles
    y : observed quantiles
    lowr : lower bound CI
    uppr: upper bound CI
    '''
    if ax == None:
        fig, ax = plt.subplots(1,1,dpi=100, facecolor="white")

    scale = np.max([x[0], y[0]]) + 0.01
    ax.set_xlim([0,scale])
    ax.set_ylim([0,scale])
    ax.minorticks_on()
        
    ax.set_xlabel('Expected ($-$log$_{10}$ p-value)')
    ax.set_ylabel('Observed ($-$log$_{10}$ p-value)')

    ax.fill_between(x, lowr, uppr, color='lightgrey')
    ax.scatter(x, y, color='blue')
    ax.plot([0,scale],[0,scale],color='black') 
    ax.set_xticks(np.arange(0,scale,1))
    ax.set_yticks(np.arange(0,scale,1))

