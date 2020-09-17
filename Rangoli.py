def Rangoli(n):
  x = list(map(chr , range(97,97+n)))

  y =x[n-1::-1]+x[1:n]
  z = len('-'.join(y))

  for i in range(1,n):
    print(('-'.join(x[n-1:n-i:-1]+x[n-i:n])).center(z,'-'))


  for i in range(n,0,-1):
        print(('-'.join(x[n-1:n-i:-1]+x[n-i:n])).center(z,'-'))


if __name__ == '__main__':


    x = int(input())
    print(Rangoli(x))
