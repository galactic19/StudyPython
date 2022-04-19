# 08장 종합문제.

# 1. 문자열 바꾸기.
# a:b:c:d 를 split 와 join을 사용하여 a#b#c#d 로 고치자.

from ast import With
from copyreg import constructor


a = "a:b:c:d"
a = a.split(':')
a = "#".join(a)


# 2. 딕셔너리 값 추출하기.
# 다음은 딕셔너리의 a에서 'C'라는 key에 해당하는 value를 출력하는 프로그램이다.
# >>> a = {'A':90, 'B':80}
# >>> a['C']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'C'


dic = {'A':90, 'B':80}
if not 'C' in dic:
    dic['C'] = 70
    
print(dic)


# 3. 리스트의 더하기와 extend 함수
# 다음과 같은 리스트 a가 있다.
# >>> a = [1, 2, 3]
# 리스트 a에 [4, 5]를 + 기호를 사용하여 더한 결과는 다음과 같다.
# >>> a = [1, 2, 3]
# >>> a = a + [4,5]
# >>> a
# [1, 2, 3, 4, 5]
# 리스트 a에 [4,5]를 extend를 사용하여 더한 결과는 다음과 같다.
# >>> a = [1, 2, 3]
# >>> a.extend([4, 5])
# >>> a
# [1, 2, 3, 4, 5]
# + 기호를 사용하여 더한 것과 extend한 것의 차이점이 있을까? 있다면 그 차이점을 설명하시오.



# 4. 리스트 총합 구하기.
# 다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상 점수의 총합을 구하시오.
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

B = list(filter(lambda x : x > 50, A))
print(sum(B))


# 5. 피보나치 함수.
# 첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후에 이어지는 항은 이전의 두 항을 더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다.
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# 입력을 정수 n으로 받았을 때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.

# 내가 작성.
def pic(num) :
    numList = [0]
    for i in range(1, num):
        if not numList[-1] > 1:
            numList.append(i)
        else:
            numList.append(numList[-2] + numList[-1])
    return numList

print(pic(10))
# print(pic(100))

# 책의 답안 이 코드 이해가 잘 안감.
# def fib(n):
#     if n == 0 : return 0
#     if n == 1 : return 1
#     return fib(n-2) + fib(n-1)
    
# for i in range(10):
#     print(fib(i))



# 6. 숫자의 총 합 구하기.
# 사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램을 작성하시오. (단 숫자는 콤마로 구분하여 입력한다.)
def plus(*args):
    return sum(tuple(args))

print(plus(1,2,3,4,6,7))


# 7. 한 줄 구구단.
# 사용자로부터 2~9의 숫자 중 하나를 입력받아 해당 숫자의 구구단을 한 줄로 출력하는 프로그램을 작성하시오.

# q = input('출력할 구구단의 단을 입력 하세요')

# for i in range(1,10):
#     print(int(q) * i, end=' ')



# 8. 다음과 같은 내용의 파일 abc.txt가 있다.
# AAA
# BBB
# CCC
# DDD
# EEE
# 이 파일의 내용을 역순으로 바꾸어 저장하시오.

f = open('memo.txt', 'r')
read = f.readlines()
f.close()
read_reverse = []

while read:
    read_reverse.append(read.pop())

f = open('memo.txt', 'w')
for i in read_reverse:
    if not '\n' in i:
        i += '\n'
    f.write(i)
f.close();



# 9. 평균값 구하기.
# 다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다. 
# sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.
# 70
# 60
# 55
# 75
# 95
# 90
# 80
# 80
# 85
# 100

total_point = []
arg = 0;

with open('sample.txt', 'r') as f:  
    for i in f.readlines():
        total_point.append(int(i.replace('\n', '')))

arg = sum(total_point) / len(total_point)

with open('result.txt', 'w') as f:
    f.write(str(arg))

print(arg) # 79.0


# 10. 사칙 연산 계산기.
# 다음과 같이 동작하는 클래스 Calculator을 작성하세요
# >>> cal1 = Calculator([1,2,3,4,5])
# >>> cal1.sum() # 합계
# 15
# >>> cal1.avg() # 평균
# 3.0
# >>> cal2 = Calculator([6,7,8,9,10])
# >>> cal2.sum() # 합계
# 40
# >>> cal2.avg() # 평균
# 8.0


class Calculator:
    def __init__(self, *args):
        self.args = args
        self.total = 0
    def sum(self):
        for i in self.args:
            for j in i:
                self.total += j
        return self.total

    def avg(self):
        for i in self.args:
            return self.total / len(i)



a = Calculator([6,7,8,9,10])
print(a.sum())
print(a.avg())



# 11. 모듈 사용 방법.
# C:\doit 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해 보자. 
# 명령 프롬프트 창에서 파이썬 셸을 열어 이 모듈을 import해서 사용할 수 있는 방법을 모두 기술하시오. (즉 다음과 같이 import mymod를 수행할 때 오류가 없어야 한다.)
# import sys
# sys.path.append('C:\doit')

# import mymod



# 12. 오류와 예외 처리.
# 다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오.
result = 0

try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4
print(result)

# 예상 : IndexError 처음 리스트의 배열이 잘못 되었음. 없은 Index를 가리키고 있음. 그래서 에러, 
#       그리고 마지막에 finally 는 무조건 실행으로 result = 3 + 4 그래서 결과 값 7을 print함.


# 13. DashInsert 함수
# DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 
# 문자열 안에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. DashInsert 함수를 완성하시오.
# 입력 예시: 4546793

# 답안. 못해서 답안 찾음......
data = "4546793"
numbers = list(map(int, data))
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:
        is_odd = num % 2 == 1
        is_next_ood = numbers[i+1] % 2 == 1
        if is_odd and is_next_ood:
            result.append("-")
        elif not is_odd and not is_next_ood:
            result.append('*')
print("".join(result))


# 14. 문자열 압축하기.
# 아래의 문자와 같이 문자열을 정리 하라.
# * 입력 예시: aaabbccccca
# * 출력 예시: a3b2c6a1



from asyncio.windows_events import NULL
from cgi import print_arguments


sms = "aaabbcccccca "


copy_sms = []

def switch(n, str_num):
    return n,str_num 

idx = 1
a,b= NULL, NULL

for i, str_num in enumerate(sms):

    if i == 0:
        a,b = switch(idx, str_num)
        
    elif str_num == b and i > 0:
        idx += 1

    else:
        copy_sms.append(b)
        copy_sms.append(idx)
        idx = 1
        a, b = switch(idx, str_num)


result = "".join([str(i) for i in copy_sms])
print(result.strip())


# 15.Duplicate Numbers
# 0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.
# 입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
# 출력 예시: True False False True False


a = "0123456789 01234 01234567890 6789012345 012322456789"
a = a.split(' ')

def checked(lst):
    for i in list("0123456789"):
        if lst.find(i) == -1 or lst.count(i) > 1:
            return False
    return True

for i, num in enumerate(a):
    print(num, checked(num))



# 16. 모스 부호 해독
# 문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오.

# 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
# 예를 들어 다음 모스 부호는 "HE SLEEPS EARLY"로 해석해야 한다.
# .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--

mors = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
mors = mors.split(" ")

a = {
    "A": ".-", "B":"-...", "C":"-.-.","D":"-..","E":".",
    "F":"..-.", "G":"--.","H":"....","I":"..","J":".---",
    "K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.",
    "Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-",
    "W":".--","X":"-..-","Y":"-.--","Z":"--.."
}

b = {n:i for i,n in a.items()} # 딕셔너리 Key:value 뒤집기.

# print(b)
def mosValsearch(arr):
    mos_result = '';
    for i in arr:
        if i == '':
            mos_result += ' '
        else:
            mos_result += b[i]

    return mos_result[0] + mos_result[1:].lower()

print(mosValsearch(mors))


# 17. 기초 메타 문자.
# 다음 중 정규식 a[.]{3,}b과 매치되는 문자열은 무엇일까?
# 1. acccb
# 2. a....b
# 3. aaab <- ?
# 4. a.cccb



# 18. Q18 문자열 검색
# 다음 코드의 결괏값은 무엇일까?
# >>> import re
# >>> p = re.compile("[a-z]+")
# >>> m = p.search("5 python")
# >>> m.start() + m.end() '1,6'



# 19 그루핑
# 다음과 같은 문자열에서 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을 정규식을 사용하여 작성하시오.
import re

datas = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

p = re.compile("(\d{3}[-]\d{4}[-])\d{4}")
m = p.sub("\g<1>####", datas)
print(m)



# 20. 전방 탐색
# 다음은 이메일 주소를 나타내는 정규식이다. 
# 이 정규식은 park@naver.com, kim@daum.net, lee@myhome.co.kr 등과 매치된다. 
# 긍정형 전방 탐색 기법을 사용하여 .com, .net이 아닌 이메일 주소는 제외시키는 정규식을 작성하시오.
# .*[@].*[.].*$

p = re.compile(".*[@].*[.](?=com$|net$).*$")
print(p.match("ddd@naver.co.kr"))