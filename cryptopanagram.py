#https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
from math import gcd

def check(v,p):
    for i in p:
        for j in p:
            if i*j == v:
                return i,j

def key_val(x,ap):
    for k,v in ap.items():
        if x == v:
            return k

def decrypt(panagram):
    s = set()
    ap = {}
    msg = []
    for i in range(len(panagram)-1):
        x = panagram[i]
        y = panagram[i+1]
        if x == y:
            continue
        a = gcd(x,y)
        b = x/a
        c = y/a
        s.add(int(a))
        s.add(int(b))
        s.add(int(c))

    p = list(s)    
    p.sort()

    alpha = list('abcdefghijklmnopqrstuvwxyz')

    for i in range(len(p)):
        ap[alpha[i]] = p[i]

    for i in panagram:
        a,b = check(i,p)
        x = key_val(a,ap)
        y = key_val(b,ap)
        if not msg:
            msg.append(x)
            msg.append(y)
        else:
            if msg[-1] == x:
                msg.append(y)
            else:
                msg.append(x)

    message = ''.join(msg)
    return (message);

case = []
C = int(input())
for i in range(C):
    N,T = input().split()
    panagram = [int(x) for x in input().split()] 
    message = decrypt(panagram)
    case.append(message)

for i in range(len(case)):
    print('CASE #{}:{}'.format(i+1,case[i]))
