import numpy as up
import matplotlib.pyplot as plt

#define neccessary parameters

beta = 0.3 #infection rate
gamma = 0.05 #recovery rate
time_steps = 1000 #number of time steps
grid_size = 100 #size of the grid
N = grid_size * grid_size #total population size

#initialize the grid with all susceptible individuals except one infected individual in the center
population = np.zeros((grid_size, grid_size), dtype=int) #0 means susceptible, 1 means infected, 2 means recovered

#randomly select one individual to be infected