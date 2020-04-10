import numpy as np
from math import ceil


#Differential Equation of fish population
def fishPopulation(startingPopulation, dt):
    P = startingPopulation
    dPdt = 0.7*P*(1-P/750)-20
    P += dPdt * dt
    return P


#System of Differential Equations of rainbow and deadly fish population
def twoFishPopulation(startingPopulations, dt):
    P = startingPopulations[0]
    G = startingPopulations[1]
    #The first equation
    dPdt = 0.7*P-0.007*P**2-0.04*P*G
    #Second equation
    dGdt = -0.25*G+0.008*P*G

    P += dPdt * dt
    G += dGdt * dt
    return [P, G]


def eulersMethod(dt, startingPopulation, days, ode):
    numberOfTimes = int(days/dt)
    if (dt <= 0 or numberOfTimes <= 0 or isinstance(numberOfTimes, int)==False):
         print("Don't do that")
         return [0]*(numberOfTimes-1)

    #This function returns an array that contains the history of the fish population. 
    else:
        currentPopulation = startingPopulation
        populationHistory = [0]
        populationHistory[0] = currentPopulation
        for _ in range(numberOfTimes):
            currentPopulation = ode(currentPopulation, dt)
            populationHistory.append(currentPopulation) 

    return populationHistory