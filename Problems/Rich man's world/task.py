deposit = int(input())
n_years = 0
while deposit < 700000:
    n_years += 1
    deposit *= 1.071
print(n_years)
