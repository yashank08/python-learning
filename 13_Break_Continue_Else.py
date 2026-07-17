for i in range(0,100):
    if i == 51:
        break
    print(i)

for i in range(0,100):
    if i == 75:
        continue
    print(i)

for i in range(0,100):
    if i == 55:
        print("break statement executed")
        break
    print(i)

else:
    print("break statement not executed")