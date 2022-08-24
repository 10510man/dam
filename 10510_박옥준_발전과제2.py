arr = [['김유신', 70, 80, None], ['이순신', 95, 85, None], ['홍길동', 75, 60, None]]
for i in range(3):
    arr[i][3] = (arr[i][1] + arr[i][2])/2

name = input('성적 조회할 학생 이름 입력: \n')
for i in range(3):
    if arr[i][0] == name:
        k = i
        break
print('===============')
print("이름", arr[k][0])
print('영어 점수:', arr[k][1])
print('수학 점수:', arr[k][2])
print('평균 점수:', arr[k][3])