import random

class GeneticAlgorithmParcel:
    def __init__(self, parameters):
        self.numOfChromosome = parameters["numOfChromosome"]
        self.products = parameters["products"]
        self.numOfDimension = len(self.products)
        self.cr = parameters["crossoverRate"]
        self.mr = parameters["mutationRate"]
        self.maxGeneration = parameters["maxGen"]
        self.budget = parameters["budget"]
        self.stoppingFitness = parameters["stoppingFitness"]
        self.maxQtyPerProduct = parameters.get("maxQtyPerProduct", 5)

    def calculateTotalPrice(self, chromosome):
        total = 0
        for i in range(len(chromosome)):
            total += chromosome[i] * self.products[i]["price"]
        return total

    def repairChromosome(self, chromosome):
        chromosome = chromosome.copy()
        total_price = self.calculateTotalPrice(chromosome)
        
        while total_price > self.budget:
            non_zero_indices = [i for i in range(len(chromosome)) if chromosome[i] > 0]
            if not non_zero_indices:
                break
            random_index = random.choice(non_zero_indices)
            chromosome[random_index] -= 1
            total_price = self.calculateTotalPrice(chromosome)
        
        return chromosome

    def calcFitnessValue(self, chromosome):
        total_price = self.calculateTotalPrice(chromosome)
        if total_price > self.budget:
            excess = total_price - self.budget
            return 1 / (1 + excess * 1000)
        else:
            selisih = self.budget - total_price
            return 1 / (1 + selisih)

    def replaceChromosomesElement(self, chromosomes, chromosome, index):
        chromosomes[index] = chromosome
        return chromosomes

    def selectCandidateChromosomes(self, probCummulatives, chromosomes):
        rets = []
        for i in range(len(probCummulatives)):
            randomValue = random.uniform(0, 1)
            if i < len(probCummulatives) - 1:
                if randomValue > probCummulatives[i] and randomValue <= probCummulatives[i + 1]:
                    rets.append({"index": i + 1, "chromosome": chromosomes[i + 1]})
            else:
                if randomValue > probCummulatives[i]:
                    rets.append({"index": i, "chromosome": chromosomes[i]})
        return rets

    def selectRouletteWheelChromosome(self, fitnessValues, chromosomes):
        probCummulative = 0
        probCummulatives = []
        
        for fitnessValue in fitnessValues:
            probability = fitnessValue / sum(fitnessValues)
            probCummulative = probCummulative + probability
            probCummulatives.append(probCummulative)

        selectedCandidateChromosomes = self.selectCandidateChromosomes(probCummulatives, chromosomes)
        
        while len(selectedCandidateChromosomes) == 0:
            selectedCandidateChromosomes = self.selectCandidateChromosomes(probCummulatives, chromosomes)
        
        return selectedCandidateChromosomes

    def generateRandomValues(self):
        rets = []
        for i in range(self.numOfChromosome):
            if random.uniform(0, 1) < self.cr:
                rets.append(i)
        return rets

    def generateInitialPopulation(self):
        chromosomes = []
        for _ in range(self.numOfChromosome):
            chromosome = []
            for _ in range(self.numOfDimension):
                qty = random.randint(0, self.maxQtyPerProduct)
                chromosome.append(qty)
            chromosome = self.repairChromosome(chromosome)
            chromosomes.append(chromosome)
        return chromosomes

    def printParcelDetails(self, chromosome):
        total_price = self.calculateTotalPrice(chromosome)
        print("\n" + "="*60)
        print("DETAIL PAKET PARCEL TERPILIH:")
        print("="*60)
        
        for i in range(len(chromosome)):
            if chromosome[i] > 0:
                product = self.products[i]
                subtotal = chromosome[i] * product["price"]
                print(f"{product['name']:35s} x{chromosome[i]} = Rp {subtotal:>10,}")
        
        print("-"*60)
        print(f"{'TOTAL BELANJA':35s}      = Rp {total_price:>10,}")
        print(f"{'BUDGET':35s}      = Rp {self.budget:>10,}")
        print(f"{'KEMBALIAN':35s}      = Rp {self.budget - total_price:>10,}")
        print("="*60)

    def dataUser(self):
        name_user = "Hidayat Lossen"
        nim_user = "2300018116"
        course_user = "Teknik Optimasi 2026 - A"
        print("\n=== Data Mahasiswa ===")
        print(f"Nama : {name_user}")
        print(f"NIM  : {nim_user}")
        print(f"UAS  : {course_user}\n")

    def mainGA(self):
        print("\n" + "="*60)
        print("GENETIC ALGORITHM - OPTIMASI PAKET PARCEL")
        print("="*60)
        print(f"Budget           : Rp {self.budget:,}")
        print(f"Jumlah Kromosom  : {self.numOfChromosome}")
        print(f"Crossover Rate   : {self.cr}")
        print(f"Mutation Rate    : {self.mr}")
        print(f"Max Generation   : {self.maxGeneration}")
        print(f"Jumlah Produk    : {self.numOfDimension}")
        print("="*60 + "\n")

        chromosomes = self.generateInitialPopulation()
        generation_results = []

        fitnessValues = []
        for chromosome in chromosomes:
            fitnessValues.append(self.calcFitnessValue(chromosome))

        candidateNewChromosomes = self.selectRouletteWheelChromosome(fitnessValues, chromosomes)

        for candidateNewChromosome in candidateNewChromosomes:
            chromosomes = self.replaceChromosomesElement(
                chromosomes,
                candidateNewChromosome["chromosome"],
                candidateNewChromosome["index"],
            )

        for k in range(self.maxGeneration):
            print(f"Generation-{k+1}", end=" ")
            
            randomIndexValues = self.generateRandomValues()
            while len(randomIndexValues) <= 1:
                randomIndexValues = self.generateRandomValues()

            selectedChromosomesToCrossover = []
            for i in randomIndexValues:
                selectedChromosomesToCrossover.append({"chromosomes": chromosomes[i], "index": i})

            parentCandidatesIndex = []
            for i in selectedChromosomesToCrossover:
                for j in selectedChromosomesToCrossover:
                    if i["index"] != j["index"]:
                        parentCandidatesIndex.append([i["index"], j["index"]])

            sortedParentIndexes = []
            for parentIndex in parentCandidatesIndex:
                parentIndex.sort()
                sortedParentIndexes.append(parentIndex)

            finalParentIndexes = []
            for sortedParentIndex in sortedParentIndexes:
                if sortedParentIndex not in finalParentIndexes:
                    finalParentIndexes.append(sortedParentIndex)

            tempOffsets = []
            offsets = []
            for parentsIndex in finalParentIndexes:
                cutPointIndex = random.randint(0, self.numOfDimension - 1)
                if cutPointIndex == self.numOfDimension - 1:
                    for i in range(self.numOfDimension):
                        if i < self.numOfDimension - 1:
                            tempOffsets.append(chromosomes[parentsIndex[1]][i])
                        else:
                            tempOffsets.append(chromosomes[parentsIndex[0]][cutPointIndex])
                else:
                    for i in range(self.numOfDimension):
                        if i <= cutPointIndex:
                            tempOffsets.append(chromosomes[parentsIndex[0]][i])
                        else:
                            tempOffsets.append(chromosomes[parentsIndex[1]][i])
                
                tempOffsets = self.repairChromosome(tempOffsets)
                offsets.append(tempOffsets)
                tempOffsets = []

            tempChromosomes = []
            chromosomesOffsets = chromosomes + offsets
            for chromosome in chromosomesOffsets:
                fitnessValue = self.calcFitnessValue(chromosome)
                tempChromosomes.append([fitnessValue, chromosome])

            tempChromosomes.sort(reverse=True)
            chromosomes = []
            for i in range(len(tempChromosomes)):
                if i <= self.numOfChromosome - 1:
                    chromosomes.append(tempChromosomes[i][1])

            tempChromosomes = []
            numOfMutation = round(self.mr * (self.numOfChromosome * self.numOfDimension))
            
            for i in range(numOfMutation):
                selectedChromosomeIndex = random.randint(0, self.numOfChromosome - 1)
                selectedGenIndex = random.randint(0, self.numOfDimension - 1)
                mutatedChromosome = chromosomes[selectedChromosomeIndex].copy()
                mutatedChromosome[selectedGenIndex] = random.randint(0, self.maxQtyPerProduct)
                mutatedChromosome = self.repairChromosome(mutatedChromosome)
                chromosomes[selectedChromosomeIndex] = mutatedChromosome

            for chromosome in chromosomes:
                fitnessValue = self.calcFitnessValue(chromosome)
                total_price = self.calculateTotalPrice(chromosome)
                tempChromosomes.append([fitnessValue, chromosome, total_price])

            bestChromosome = max(tempChromosomes)
            selisih = self.budget - bestChromosome[2]
            
            generation_results.append({
                'generation': k + 1,
                'fitness': bestChromosome[0],
                'kembalian': selisih
            })
            
            print(f"-> Nilai Optimasi: {bestChromosome[0]:.6f}, Total: Rp {bestChromosome[2]:,}, Kembalian: Rp {selisih:,}")
            
            if self.stoppingFitness <= bestChromosome[0]:
                print(f"\n✓ Stopping criteria tercapai di generasi ke-{k+1}!")
                break
            
            tempChromosomes = []

        print("\n" + "="*60)
        print("Soal 1a. TABEL NILAI MINIMUM (KEMBALIAN) PER GENERASI")
        print("="*60)
        print(f"{'Generasi':<15} {'Kembalian (Rp)':<20}")
        print("-" * 35)
        for result in generation_results:
            print(f"{result['generation']:<15} {result['kembalian']:<20,.2f}")
        print("="*60)
        
        print("\n" + "="*60)
        print("Soal 1b. HASIL AKHIR OPTIMASI")
        print("="*60)
        
        finalChromosomes = []
        for chromosome in chromosomes:
            fitnessValue = self.calcFitnessValue(chromosome)
            total_price = self.calculateTotalPrice(chromosome)
            finalChromosomes.append([fitnessValue, chromosome, total_price])
        
        bestSolution = max(finalChromosomes)
        
        print(f"Nilai Optimasi  : {bestSolution[0]:.6f}")
        print(f"Total Belanja   : Rp {bestSolution[2]:,}")
        print(f"Budget          : Rp {self.budget:,}")
        print(f"Kembalian       : Rp {self.budget - bestSolution[2]:,}")
        
        min_kembalian_gen = min(generation_results, key=lambda x: x['kembalian'])
        print(f"Ditemukan pada Generasi ke-{min_kembalian_gen['generation']}")
        print("="*60)
        
        self.printParcelDetails(bestSolution[1])
        self.dataUser()
        
        return bestSolution[1]


products = [
    {"name": "VIDORAN Xmart 5+ Cokelat 700g", "price": 49400},
    {"name": "VIDORAN Xmart 1+ Madu 125g", "price": 10900},
    {"name": "BEAR BRAND Colagen 189ml", "price": 9900},
    {"name": "INDOMIE Nyemek Jogja Rendang", "price": 3450},
    {"name": "INDOMIE Hype Abis Bangladesh", "price": 2950},
    {"name": "RICHEESE Wafer", "price": 5000},
    {"name": "HERBAKOF Sirsak Mint 100ml", "price": 20000},
    {"name": "SO FRESH M. Angin Citrus", "price": 12500},
    {"name": "SOSOFT Detergen 700ml", "price": 16500},
    {"name": "BAGUS Karbol Pine 575ml", "price": 10900},
    {"name": "BEBEK Pembersih Kloset", "price": 19900},
    {"name": "PLOSSA Blue Mountain 10ml", "price": 14900},
    {"name": "SPONGEBOB Buddies Figure", "price": 29900},
    {"name": "GABBY'S Dollhouse", "price": 24900},
    {"name": "APOLO Snap Toys", "price": 29900},
    {"name": "APOLO Majestic Sand", "price": 37900},
    {"name": "BARBIE Jet Tag Snowflakez", "price": 49900},
    {"name": "HOT WHEELS 25th Anniv", "price": 59900},
]

parameters = {
    "numOfChromosome": 25,
    "crossoverRate": 0.23,
    "mutationRate": 0.1,
    "maxGen": 55,
    "budget": 125000,
    "stoppingFitness": 0.99,
    "products": products,
    "maxQtyPerProduct": 5,
}

if __name__ == "__main__":
    runGA = GeneticAlgorithmParcel(parameters)
    bestSolution = runGA.mainGA()