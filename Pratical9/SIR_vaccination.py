import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm

N = 10000 #population size initially
beta = 0.3 #infection rate
gamma = 0.05 #recovery rate
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] #vaccination rates from 0% to 100%
time_steps = 1000 #number of time steps

plt.figure(figsize=(10, 6),dpi=100)
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates))) #create 11 colors from the viridis color map

for rate, color in zip(vaccination_rates, colors):
    R0 = 0 #initial number of recovered individuals
    V0 = int(rate * N) #initial number of vaccinated individuals
    if V0 == N: # If the whole population is vaccinated, there is no infected person
        I0 = 0
        S0 = 0    
    else:    
        I0 = 1 #initial number of infected individuals
        S0 = N - I0 - V0 #initial number of susceptible individuals
    I = [] #list to store the number of infected individuals at each time step
    S = [] #list to store the number of susceptible individuals at each time step
    R = [] #list to store the number of recovered individuals at each time step
    for t in range(time_steps): #simulate for 1000 time steps
        I.append(I0)
        S.append(S0)
        R.append(R0)
        infection_prob = beta * I0 / N #probability of infection
        infection_prob = min(max(infection_prob, 0), 1) #ensure the probability is between 0 and 1
        recovery_prob = gamma #probability of recovery
        if S0 > 0: #Randomly decide how many susceptible people become infected
            infect = np.random.choice([0, 1], size=S0, p=[1 - infection_prob, infection_prob]) #0 means not infected and 1 means infected
            new_infections = int(np.sum(infect))
        else:
            new_infections = 0
        if I0 > 0: #Randomly decide how many infected poeple recover    
            recover = np.random.choice([0, 1], size=I0, p=[1 - recovery_prob, recovery_prob]) #0 means not recovered and 1 means recovered
            new_recoveries = int(np.sum(recover))
        else:
            new_recoveries = 0
        # You cannot infect more people than susceptible people
        new_infections = min(new_infections, S0)

        # You cannot recover more people than infected people
        new_recoveries = min(new_recoveries, I0)

        S0 -= new_infections #update the number of susceptible individuals
        I0 += new_infections - new_recoveries #update the number of infected individuals
        R0 += new_recoveries #update the number of recovered individuals

        S0 = max(int(S0), 0) #ensure the number of susceptible individuals is not negative
        I0 = max(int(I0), 0) #ensure the number of infected individuals is not negative
        R0 = max(int(R0), 0) #ensure the number of recovered individuals is not negative

    #plot the results
    label_next = str(int(rate * 100)) + '%'
    plt.plot(I, label=label_next, color = color)

#finish the plot
plt.xlabel('Time')
plt.ylabel('Number of Individuals')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend(title = 'Vaccination rate')
plt.tight_layout()
plt.savefig('D:/IBI/SIR_vacciation_model.png',format='png')
plt.show()