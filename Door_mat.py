n,m = map(int,input().split())
s1 = '.|.'
s2 = 'WELCOME'
# Top Part
for i in range(n//2):
    print((s1*((i*2)+1)).center(m,'-'))
#mid
print(s2.center(m,'-'))

# bottom
for i in range(n//2-1,-1,-1):
    print((s1*((i*2)+1)).center(m,'-'))
