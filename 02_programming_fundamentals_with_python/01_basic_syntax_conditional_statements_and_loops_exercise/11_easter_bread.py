budget = float(input())
price_kg_flour = float(input())
price_pack_eggs = price_kg_flour * 0.75
price_milk = (price_kg_flour * 1.25) / 4
bread = price_milk + price_pack_eggs + price_kg_flour
expenses = 0
loaves_made = 0
gathered_eggs = 0

while expenses + bread < budget:
    loaves_made += 1
    gathered_eggs += 3
    expenses += bread
    if loaves_made % 3 == 0:
        gathered_eggs -= loaves_made - 2

print(f"You made {loaves_made} loaves of Easter bread! "
      f"Now you have {gathered_eggs} eggs and {(budget - expenses):.2f}BGN left.")
