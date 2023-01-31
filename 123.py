from itertools import permutations
digits = input("Enter three digits: ")
combinations = list(permutations(digits))
for combination in combinations:
    print("".join(combination))
