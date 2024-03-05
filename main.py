from itertools import combinations

# Data_List = """abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+|}{[]\=-`:;"'?/>.<,/}"""
Data_List = input("Enter Possible Alphabates: ")

letters = list(Data_List)

for r in range(1, len(letters)):
    comb = combinations(letters, r)

    for c in comb:
        print("".join(c), c)
        with open("wordlist.txt", "a") as data:
            data.write("".join(c) + "\n")
