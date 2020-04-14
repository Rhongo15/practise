test_cases = int(input())

def allocation(no, budget, houses):
    counter = 0
    amount = 0
    for i in houses:
        if (amount+i) <= budget:
            amount = amount + i
            counter += 1
            print(amount)
    return counter;

case = []

for i in range(test_cases):
    no_of_houses,budget = [int(x) for x in input().split()]
    house = [int(x) for x in input().split()]
    house.sort()
    buy = allocation(no_of_houses, budget, house)
    case.append(buy)
    
for i in range(test_cases):
    print("Case #%d: %d" %(i+1, case[i]))