population = [int(s) for s in input().split(", ")]
minimum_wealth = int(input())
parts = len(population)
if parts * minimum_wealth <= sum(population):
    while min(population) < minimum_wealth:
        for index, part in enumerate(population):
            if part < minimum_wealth:
                diff = minimum_wealth - part
                population[index] += diff
                maximum_wealth_index = population.index(max(population))
                population[maximum_wealth_index] -= diff
    print(population)
else:
    print("No equal distribution possible")
