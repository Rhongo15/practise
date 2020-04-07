#https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f
test_cases = int(input())

cases = []

for i in range(test_cases):
    c = input()
    cases.append(c)
 
    
def nest(a):
    open_brackets = 0
    nest_list = []
    for i in range(a[0]):
        nest_list.append('(')
    open_brackets = a[0]
    nest_list.append(str(a[0]))
    for i in range(1, len(a)):
        x = a[i]
        y = a[i-1]
        diff = abs(x - y)
        if x < y:
            for i in range(diff):
                nest_list.append(')')
            nest_list.append(str(x))
            open_brackets = open_brackets - diff
        elif x > y:
            for i in range(diff):
                nest_list.append('(')
            nest_list.append(str(x))
            open_brackets = open_brackets + diff
        else:
            nest_list.append(str(x))
    for i in range(open_brackets):
        nest_list.append(')')
    result = ''.join(nest_list)
    return result;
    
c = 1
for i in cases:
    split_a = [int(d) for d in i]
    result = nest(split_a)
    print("Case #%d: %s" %(c, result))
    c = c+1
    

    
        
        
