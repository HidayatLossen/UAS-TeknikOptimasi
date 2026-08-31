matriks = [
    [0,    364, 156, 325,  152, 328,  335,  302, 265,  174],   
    [364,   0,  297, 574,  273, 577,  583,  492, 450,  315], 
    [156,  297, 0,   325,  26.1, 328, 335,  203, 161,  19.6], 
    [325,  574, 325,   0,   266,   4, 21.6, 52.6, 82.1, 236], 
    [152,  273, 26.1,266,  0,    271, 326,  246,  185,  44], 
    [328,  577, 328,   4,  271, 0,    20.1, 50.9, 85,  239], 
    [335,  583, 335, 21.6, 326, 20.1, 0,    70.3, 100, 254], 
    [302,  492, 203, 52.6, 246, 50.9, 70.3, 0,    40.2, 194], 
    [265,  450, 161, 82.1, 185, 85,   100, 40.2, 0,    155], 
    [174,  315, 19.6, 236,  44, 239,  254, 194, 155, 0]    
]

cityNames = [
    "Kos", "Sunan Gunung Jati (Cirebon)", "Sunan Kudus", "Sunan Giri (Gresik)",
    "Sunan Kalijaga (Demak)", "Sunan Gresik", "Sunan Ampel (Surabaya)",
    "Sunan Drajat (Lamongan)", "Sunan Bonang (Tuban)", "Sunan Muria (Kudus)"
]

parameters = {
    'Q': 100,
    'rho': 0.05,      
    'antSize': 17,    
    'matriks': matriks,
    'maxIter': 35,    
    'cityNames': cityNames
}

import random, sys

class AntColonyOptimizationTSP:
    def __init__(self, parameters, start):
        self.params = parameters
        self.start = start

    def ACOTSProblem(self):
        tabuList = []; feromon = 1/len(self.params['matriks'])
        finalDistance = []; allDistances = []
        finalResults = []; bestSolutions = []

        for iter in range(self.params['maxIter']):
            # print(f"\n iterasi ke-{iter}")
            for i in range(self.params['antSize']):
                if self.start:
                    nextCity = self.start[0]
                else:
                    nextCity = random.randint(0, len(self.params['matriks'])-1)
                tabuList.append([nextCity])
            # print(tabuList)
        

            temp = []; city = []; pairedCity = []; matriks = self.params['matriks']
            for i in range(len(matriks)-1):
                for j in range(len(tabuList)):
                    r = random.uniform(0,1)
                    for cityID in range(len(matriks)):
                        for k in tabuList[j]:
                            temp.append(k)
                            temp.append(cityID)
                        if temp.count(cityID) == len(tabuList[j]):
                            city.append(tabuList[j][-1])
                            city.append(cityID)
                        else:
                            city.append(cityID)
                            city.append(cityID)
                        pairedCity.append(city)
                        city = []; temp = []
                    pairedDistances = self.getDistance(pairedCity)
                    pairedCity = []
                    probNextCities = self.getProbNextCities(pairedDistances, feromon)
                    nextCities = self.getNextCites(probNextCities, r)
                    tabuList[j].append(nextCities)
            # print(tabuList)
            # print()
            # sys.exit()

            for k in range(len(tabuList)):
                for l in range(len(tabuList[k])-1):
                    city.append(tabuList[k][l])
                    city.append(tabuList[k][l+1])
                    pairedCity.append(city)
                    city = []
                pairedCity.append([tabuList[k][-1], tabuList[k][0]])
                # print(pairedCity)
                pairedDistances = self.getDistance(pairedCity)
                name = self.getPairedCityName(tabuList[k])
                finalDistance.append([name, pairedDistances])
                allDistances.append(sum(pairedDistances))
                pairedCity = []
            # sys.exit()

            minIndex = allDistances.index(min(allDistances))
            finalResults.append(finalDistance[minIndex])
            bestSolutions.append(min(allDistances))
            finalDistance = []; allDistances = []; tabuList = []

        shortestRoutes = finalResults[bestSolutions.index(min(bestSolutions))]
        print("\n" + "="*60)
        print("Soal 2a. Tabel Nilai Minimum Per Iterasi")
        print("="*60)
        print(f"{'Iterasi':<10} {'Nilai Minimum (km)':<20}")
        print("-" * 30)
        for idx, minVal in enumerate(bestSolutions, 1):
            print(f"{idx:<10} {minVal:<20.2f}")
        
        print("\n" + "="*60)
        print(f"soal 2b. NILAI MINIMUM GLOBAL/AKHIR")
        print("="*60)
        print(f"Jarak Terpendek: {min(bestSolutions):.2f} km")
        print(f"Ditemukan pada iterasi ke-{bestSolutions.index(min(bestSolutions)) + 1}")
        # print(f"\n {shortestRoutes}", '\n')


        print('\n\n=== Rute terpendek ziarah makam wali songo:   ===')
        # print(f"\nAntar Kota : \n{shortestRoutes[0]}")
        # print(f"\nJarak Antar Kota (km): \n{shortestRoutes[1]}\n\n")
        print(f"{shortestRoutes}", '\n')
        for i in shortestRoutes[0]:
            print(i)
        print(shortestRoutes[0][0])
        print(f'Total : {sum(shortestRoutes[1])} kilometer')
        self.dataUser()

    def dataUser(self):
        name_user = "Hidayat Lossen"
        nim_user = "2300018116"
        course_user = "Teknik Optimasi 2026 - A"
        print("\n\n=== Data User UAS ===")
        print(f"Nama : {name_user}")
        print(f"NIM  : {nim_user}")
        print(f"UAS : {course_user}")

    def getDistance(self, pairedCities):
        rets = []
        for i in pairedCities:
            for j in range(len(self.params['matriks'])):
                for k in range(len(self.params['matriks'][j])):
                    if i[0] == j and i[1] == k:
                        rets.append(self.params['matriks'][j][k])
        return rets

    def getProbNextCities(self, distancePaired, feromon):
        ret = []
        for distance in distancePaired:
            if distance == 0:
                val = 0
            else:
                val = (1/distance) * feromon
            ret.append(val)
        return ret

    def getNextCites(self, probNextCities, r):
        tmp = 0
        for i in range(len(probNextCities)):
            if sum(probNextCities) != 0:
                tmp = tmp + (probNextCities[i]/sum(probNextCities))
            else:
                tmp = 0
            if r < tmp:
                i
                break
        return i

    def getPairedCityName(self, tabuList):
        rets = []
        for i in tabuList:
            for j in range(len(self.params['cityNames'])):
                if i == j:
                    rets.append(self.params['cityNames'][j])
        return rets

aco = AntColonyOptimizationTSP(parameters, start=[0])
aco.ACOTSProblem()



