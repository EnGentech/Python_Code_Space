matrixList1 = [[2, 5, 1], [7, 3, 4]]
matrixList2 = [[2, 4], [3, 5], [0, 1]]

print('===matrix 1===')
for x in matrixList1:
    for j in x:
        print(j, end=' ')
    print()
print('\n===matrix 2===')
for x in matrixList2:
    for j in x:
        print(j, end=' ')
    print()

print('\n===multiply matrix 1 to matrix2===')
times = len(matrixList2[0])
mulList = []
for x in matrixList1:
    sub_index = 0
    for repeat in range(times):
        total = 0
        innerList = []
        index = 0
        for items in x:
            total += (items * matrixList2[index][sub_index])
            index += 1
        sub_index += 1
        mulList.append(total)

for value in range(len(mulList)):
    if value == len(matrixList2[0]):
        print()
    print(mulList[value], end=' ')