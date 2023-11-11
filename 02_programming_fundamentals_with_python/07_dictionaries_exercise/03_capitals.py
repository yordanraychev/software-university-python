countries = input().split(", ")
capitals = input().split(", ")
final_information = {countries[index]: capitals[index]
                     for index in range(len(countries))}
for country, capital in final_information.items():
    print(f"{country} -> {capital}")
