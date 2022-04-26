import numpy as np
import matplotlib.pyplot as plt

def fitting(difficulty, quality, name='plot', degree = 5, scale = 1):
    '''
    
    A function which plots a linear regression model for applicant response performance
    against task difficulty.
    
    Parameters
    ----------
    quality: array
        List of response quality from a scale of 1 - 10
        
    name: str
        Applicant Name, default set to blank
        
    degree: int
        Degree of polynomial fit, default set to 5
    
    Returns
    ----------
    None
    
    '''
    #Initialize Prompt difficulty, quality and polynomial fits
    P = difficulty
    Q = quality * scale
    Zfit = np.polyfit(P, Q, degree)
    Fit = np.poly1d(Zfit)

    #Plotting
    plt.ylabel('Quality of Explanation')
    plt.xlabel('Difficulty of Task')
    plt.xticks(np.arange(0,11))
    plt.title(f'Applicant {name} Best Fit')
    plt.plot(P, Fit(P))
    plt.scatter(P, Q)

    #save plot to images directory
    import os

    #get the root directory path
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    new_plot = f'plots\{name}.png'
    plt.savefig(os.path.join(ROOT_DIR, new_plot)) 
    plt.close()