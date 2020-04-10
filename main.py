import matplotlib.pyplot as plt
import ODEs

days = 1000
dt = 1/8
startingPopulation = [20, 5]

yaxis = []
#yaxis = (ODEs.eulersMethod(dt, startingPopulation, days, ODEs.twoFishPopulation))
yaxis.append(ODEs.eulersMethod(dt, startingPopulation, days, ODEs.twoFishPopulation))
#yaxis.append(ODEs.eulersMethod(dt*2, startingPopulation, days*2, ODEs.twoFishPopulation))
xaxis = [i*dt+1 for i in range(int(days/dt+1))]



err = ODEs.eulersMethod(dt*2, startingPopulation, days*2, ODEs.twoFishPopulation)


#yaxis.append(ODEs.eulersMethod(dt, [0,30], days, ODEs.twoFishPopulation))
#yaxis.append(ODEs.eulersMethod(dt, [120,0], days, ODEs.twoFishPopulation))

def extractTwoFishTypes(graph):
    P=[]
    G=[]
    for i in range(len(graph)):
        #P.append(yaxis[i][0])
        #G.append(yaxis[i][1])
        P.append(graph[i][0])
        G.append(graph[i][1])
        #PError = abs(P[i] - err[i][0])
        #GError = abs(G[i] - err[i][1])
        print(f"number of fish at day {i*dt} was P={P[i]} and G={G[i]}")#" and the error of P is {PError} and of G {GError}")
    return [P,G]
    
PG_1 = extractTwoFishTypes(yaxis[0])
#PG_2 = extractTwoFishTypes(yaxis[1])
#PG_3 = extractTwoFishTypes(yaxis[2])

plt.plot(PG_1[0],PG_1[1])
#plt.plot(PG_2[0],PG_2[1])
#plt.plot(PG_3[0],PG_3[1])
#plt.plot(xaxis, yaxis)
#plt.plot(xaxis, yaxis[0])
#plt.plot(xaxis, yaxis[1])
plt.autoscale()
plt.ylabel('Fish')
plt.xlabel('Days')
plt.grid(True)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.show()