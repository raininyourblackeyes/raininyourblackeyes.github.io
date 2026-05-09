import numpy as np
import matplotlib.pyplot as plt 

N = 10000 #population size initially
I0 = 1 #initial number of infected individuals
S0 = N - I0 #initial number of susceptible individuals
R0 = 0 #initial number of recovered individuals
beta = 0.3 #infection rate
gamma = 0.05 #recovery rate
I = [] #list to store the number of infected individuals at each time step
S = [] #list to store the number of susceptible individuals at each time step
R = [] #list to store the number of recovered individuals at each time step
time_steps = 1000 #number of time steps
for t in range(time_steps): #simulate for 1000 time steps
    I.append(I0)
    S.append(S0)
    R.append(R0)
    infection_prob = beta * I0 / N #probability of infection
    recovery_prob = gamma #probability of recovery
    infect = np.random.choice([0, 1], size=S0, p=[1 - infection_prob, infection_prob]) #randomly select an individual to infect or recover  
    recover = np.random.choice([0, 1], size=I0, p=[1 - recovery_prob, recovery_prob]) #randomly select an individual to infect or recover
    S0 -= np.sum(infect) #update the number of susceptible individuals
    I0 += np.sum(infect) - np.sum(recover) #update the number of infected individuals
    R0 += np.sum(recover) #update the number of recovered individuals

# plot the result

plt.figure(figsize=(10, 6),dpi=80)    
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.plot(S, label='Susceptible')
plt.xlabel('Time')
plt.ylabel('Number of Individuals')
plt.title('SIR Model')
plt.legend()
plt.show()
plt.savefig('D:/IBI/SIR_model.png',format='png')