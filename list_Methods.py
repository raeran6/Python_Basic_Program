# list method thorugh user input
list = []
total = 7
nmb = 0
print("Press 1 for insert\n"
      "press 2 Print for the list\n"
      "press 3 for remove\n"
      "press 4 for append\n"

      "press 5 for sort\n"
      "press 6 for pop\n"
      "press 7 for reverse")
while nmb < total:
    N = int(input("enter your choice  "))
    if N == 1:
        n = int(input("enter no  "))
        i = int(input("enter index "))
        list.insert(n, i)
        print(list)
    elif N == 2:
        print(list)
    elif N == 3:
        n = int(input("enter no  "))
        i = int(input("enter index "))
        list.remove(n, i)
        print(list)
    elif N == 4:
        n = int(input("enter the no "))
        list.append(n)
        print(list)
    elif N == 5:
        lst = list.sort()
        print(lst)
    elif N == 6:
        list.pop()
        print(list)
    elif N == 7:
        lst = list.reverse()
        print(list)
    else:
        print("invalid choice")
    nmb = nmb + 1








