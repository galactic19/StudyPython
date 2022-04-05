#04장 연습 문제.

# 1.주어진 자연수가 홀수,짝수인지 판별해 주는 함수를 작성해 보자.
def is_odd(num):
    if num % 2:
        return '홀수 입니다.'
    else:
        return '짝수 입니다.'



# 2. 입력 받은 모든 수의 평균값을 계산하는 함수를 작성하자. (인자의 개수는 정해져 있지 않다.)
def avg_nums(*args):
    if len(args):
        num = 0
        for i in args:
            num += i
            
        num = num / len(args)
        return num
    else: 
        return '인자가 없습니다.'


# 3. 두개의 숫자를 입력받아 덧셈하여 돌려주는 프로그램이다.
"""
input1 = input('첫번째 숫자를 입력하세요')
input2 = input('두번째 숫자를 입력하세요')

total = input1 + input2
print('두수의 합은 %s 입니다.' % total)

3과 6을 입력하여 실행해보니 36의 결과값을 돌려받았다.
잘못된 점을 수정해 보자.
"""
# 수정 코드(답)
# total = int(input1) + int(input2)



# 4. 다음 중 출력 결과가 다른 것 한 개를 골라보자.
"""
1. print("you" "need" "python")
2. print("you"+"need"+"python")
3. print("you","need", "python")
4. print("".join(['you', 'need', 'python']))

정답 : 3번
"""


# 5. test.txt라는 파일에 "Life is too short" 문자열을 저장한 후 출력하는 프로그램을 만들어 보자.
with open('test.txt', 'w') as f:
    f.write("Life is too short")

with open('test.txt', 'r') as f:
    data = f.read()
    print(data)


# 6. 사용자의 입력을 파일test.txt에 저장하는 프로그램을 작성해 보자. ( 기존의 내용을 지속적으로 유지하는 프로그램으로 작성하자.)
user = input('저장할 내용을 입력하세요')

if len(user):
    with open('test.txt','a') as f:
        f.write('\n%s' % user)



# 7. 다음과 같은 내용을 지닌 파일 test.txt가 있다
#    파일의 내용중 'java'라는 문자열을 'python'으로 바꾸어 저장해 보자.
#    "Life is too short" \n "you need java"
with open('test.txt', 'r') as f:
    data = f.read()
    data = data.replace('java', 'python')

with open('test.txt', 'w') as f:
    f.write(data)




