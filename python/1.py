stackThree = 0 
stackFive = 0
TotalSum = 0

while stackThree < 1002:
    if stackThree == stackFive:
        TotalSum = TotalSum + stackThree
        stackThree = stackThree + 3
        stackFive = stackFive + 5
    elif stackThree > stackFive:
        TotalSum = TotalSum + stackFive
        stackFive = stackFive + 5
    elif stackThree < stackFive:
        TotalSum = TotalSum + stackThree
        stackThree = stackThree + 3

print TotalSum

