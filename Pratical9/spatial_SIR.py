import numpy as np
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
outbreak_center = np.random.choice(range(grid_size), size=2) #randomly select the coordinates of the outbreak center
population[outbreak_center[0], outbreak_center[1]] = 1 #set the outbreak center to be infected

#prepare to store the number of infected individuals at each time step
#we will plot the population at these time points
snapshot_times = [0, 10, 50, 100]
snapshots = {}
snapshots[0] = population.copy() #store the initial state of the population

#simulate the spread of the disease over time

# Pseudocode:
# For each time step:
#   1. Find all infected individuals.
#   2. For each infected individual, check its 8 neighbouring cells.
#   3. If a neighbour is susceptible, it may become infected with probability beta.
#   4. The infected individual may recover with probability gamma.
#   5. Update the population.
#   6. Store selected time points for plotting.

for t in range(1, time_steps + 1):
    new_population = population.copy() #create a copy of the population to update the states simultaneously
    for i in range(grid_size):
        for j in range(grid_size): #traverse all individuals
            if population[i, j] == 1: #if the individual is infected
                #try to infect its neighbors
                for x in range(max(0, i - 1), min(grid_size, i + 2)):
                    for y in range(max(0, j - 1), min(grid_size, j + 2)):
                        if population[x, y] == 0: #if the neighbor is susceptible
                            infection_event = np.random.choice([0, 1], p=[1 - beta, beta]) #infect with probability beta
                            if infection_event == 1:
                                new_population[x, y] = 1 #set the neighbor to be infected
                #try to recover
                recover_event = np.random.choice([0, 1], p=[1 - gamma, gamma]) #recover with probability gamma
                if recover_event == 1:
                    new_population[i, j] = 2 #set the individual to be recovered
    population = new_population #update the population state

    if t in snapshot_times: #store the population state at the specified time points
        snapshots[t] = population.copy()

#plot the snapshots
for time in snapshot_times:
    plt.figure(figsize=(6, 4), dpi = 150)
    plt.imshow(snapshots[time], cmap='viridis', interpolation='nearest', vmin=0, vmax=2) #plot the population state using a color map
    plt.title("Spatial SIR model at time " + str(time))
    colorbar = plt.colorbar(ticks=[0, 1, 2]) #add a color bar to indicate the meaning of colors
    colorbar.ax.set_yticklabels(['Susceptible', 'Infected', 'Recovered'])
    plt.tight_layout()
    plt.show()