loaves = float(input("Enter the number of loaves of day old bread being purchased: "))
regular_price = 185 * loaves
discount = regular_price * 0.60
total_price = regular_price - discount

print("Regular price: {:.2f}".format(regular_price))
print("Discount: {:.2f}".format(discount))
print("Total price: {:.2f}".format(total_price))
