mackerel_price_per_kg = float(input())
sprat_price_per_kg = float(input())
bonito_kgs = float(input())
scad_kgs = float(input())
mussels_kgs = int(input())

bonito_price = mackerel_price_per_kg + mackerel_price_per_kg * 0.6
bonito_cost = bonito_price * bonito_kgs
scad_price = sprat_price_per_kg + sprat_price_per_kg * 0.8
scad_cost = scad_price * scad_kgs
mussels_price_per_kg = 7.5
mussels_cost = mussels_price_per_kg * mussels_kgs

total_sum = bonito_cost + scad_cost + mussels_cost

print(f"{total_sum:.2f}")
