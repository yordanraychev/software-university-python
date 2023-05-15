chicken_quantity = int(input())
fish_quantity = int(input())
vegetarian_quantity = int(input())
chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery = 2.50
menus_price= chicken_menu * chicken_quantity \
             + fish_menu * fish_quantity \
             + vegetarian_quantity * vegetarian_menu
dessert_price = menus_price * 0.2
total_sum = menus_price + dessert_price + delivery
print(total_sum)
