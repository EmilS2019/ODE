import matplotlib.pyplot as plt
import ODEs

days = 100
dt = 1/8
startingPopulation = [30, 5]

yaxis = ODEs.eulersMethod(dt, startingPopulation, days, ODEs.twoFishPopulation)
xaxis = [i for i in range(0,int(days/dt))]
plt.plot(xaxis, yaxis)

plt.ylabel('Fish')
plt.xlabel('Days')
plt.grid(True)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.show()