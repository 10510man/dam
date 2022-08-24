arr = [['일', 70, 80, None], ['이', 95, 85, None],['삼', 75, 60, None]]
for i in range(3):
    arr[i][3] = (arr[i][1] + arr[i][2])/2
    for j in range(4):
        print(arr[i][j], end = '\t')
    print('\n')