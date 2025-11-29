for j in range(3):
    for i in range(5):
        print('*', end = ' ')
    print()

for row in range(4):
    for col in range(4):
        print('*', end = ' ')
    print()

for row in range(5):  
    for col in range(5):  
        print(row, end=' ')  
    print()

for row in range(5):  
    for col in range(5):  
        print(col, end=' ')  
    print()

for row in range(5):  
    for col in range(row + 1):  
        print(col, end=' ')  
    print()

n = int(input("Enter the size: "))
        
for row in range(n):  
    for col in range(n - row):  
        print(col, end=' ')  
    print()

n = int(input("Enter the size: "))

for row in range(n):
    for space in range(n - 1 - row):
        print(' ', end=' ')
    for col in range(row + 1):
        print('*', end=' ')
        
    print()

n = int(input("Enter the size: "))

for row in range(n):
    for space in range(row):
        print(' ', end=' ')
    for col in range(n - row):
        print('*', end=' ')
        
    print()

n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0 or col == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

n = int(input("Enter the size: "))

for row in range(n):
    if row % 2 == 0:  
        for col in range(n):
            print('*', end=' ')
    else:
        for col in range(n):
            if col == 0 or col == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
    print()

n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == n - 1 - row:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == col or col == n - 1 - row:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
