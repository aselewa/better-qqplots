import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
plt.style.use('classic')

def qqplot_unif(y, ax=None, return_object=False):
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
    
    if ax == None:
        fig, ax = plt.subplots(1,1,dpi=100, facecolor="white")
        
    scale = np.max([x[0],y[0]]) + 0.01
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
    
    if return_object:
        return fig
    
def qqplot_norm(y, ax=None, return_object=False):
    '''
    Plots a quantile-quantile plot for the normal distribution with 95% CI band based on the distribution of order statistics
    '''
    N = len(y)
    y = np.sort(y)
    y_mean = np.mean(y)
    y_std = np.std(y)
    y_normed = (y-y_mean)/y_std
    q = (np.arange(1,N+1,1)-0.5)/N
    x = stats.norm.ppf(q)
    
    # Compute scale limits:
    xmin = np.min([x[0], y_normed[0]]) - 0.1 # give room for points on the edges
    xmax = np.max([x[N-1], y_normed[N-1]]) + 0.1
    ymin = xmin * y_std + y_mean
    ymax = xmax * y_std + y_mean
        
    # Compute the confidence band:
    n_sample = 5000 # number of bootsraps 
    x_matrix = np.sort(stats.norm.rvs(size=(n_sample,N)),axis=1)
    
    alpha = 0.05 # 1 - confidence level
    n_alpha = int(alpha/2 * n_sample)
    
    if N <= 1000:
        fill_range = np.arange(N)
    else: # Down-sample the confidence band
        fill_range = np.concatenate([np.arange(0,N,int(N/1000)), np.array([N-1])])
    
    lowr = np.zeros(len(fill_range))
    uppr = np.zeros(len(fill_range))
    
    for idx,val in enumerate(fill_range):
        x_vec = np.sort(x_matrix[:,val])
        lowr[idx] = x_vec[n_alpha]        
        uppr[idx] = x_vec[n_sample-n_alpha]
    
    lowr = lowr * y_std + y_mean
    uppr = uppr * y_std + y_mean
    
    if ax == None:
        fig, ax = plt.subplots(1,1,dpi=100, facecolor="white")
        
    ax.set_xlim([xmin,xmax])
    ax.set_ylim([ymin,ymax])
    ax.minorticks_on()
        
    ax.set_xlabel('Theoretical Quantile')
    ax.set_ylabel('Sample Quantile')

    ax.fill_between(x[fill_range], lowr, uppr, color='lightgrey')
    ax.scatter(x, y, color='blue')
    ax.plot([xmin,xmax],[ymin,ymax],color='black')
    
    if return_object:
        return fig

