print("How many city names you want enter")   # Question no :- 9
n = int(input())
print("please enter",n,"city names")
citylist = []
i = 0
while i<n:
    citylist.append(input())
    i += 1
print(citylist)
print()