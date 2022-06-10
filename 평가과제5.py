import random
print('1~100까지의 숫자(정수) 중 컴퓨터가 생각한 숫자를 맞혀보세요.')
print('기회는 6번 입니다.')
number =  random.randint(1,101)
for i in range(1,7):
    guess = int(input('숫자는 무엇일까요?\n'))
    if number > guess:
        print('컴퓨터가 생각한 숫자가 더 큽니다.\n')
    elif number < guess:
        print('컴퓨터가 생각한 숫자가 더 작습니다.\n')
    else:
        print('정답입니다.')
        print(i,'번 만에 답을 맞혔습니다.')
        break
if i == 6:
    print('실패! 컴퓨터가 생각한 숫자는', number,'입니다.')
