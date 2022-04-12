# 1. 아래 클래스를 상속하는 Upgrade Calculator 을 만들고 값을 뺄 수 있는 minus 매서드를 추가 하자.
class Calulator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

######## 여기 까지 문제 내용 아래 부터 작성 ########

class Upgrade_calulator(Calulator):
    def minus(self, val):
        self.value -= val


a = Upgrade_calulator()

a.add(10)
a.minus(3)
print(a.value) # 7 출력



# 2. 객체 변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalulator 클래스를 만들어 보자. / 최대값 100을 넘지만 않으면 된다.
class MaxLimitCalulator(Upgrade_calulator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
            print('100까지 제한 되어 있습니다.')\


b  = MaxLimitCalulator()
b.add(50)
b.add(97)

print(b.value) # 100 출력



# 3. 다음 결과를 예측 해보자.
#  - all([1,2, abs(-3)-3]) False
#  - chr(ord('a')) == 'a' 


# 4. filter 과 lambda 를 사용하여 리스트 [1,-2,3,-5,8,-3]에서 음수를 모두 제거 해보자.

a = list(filter(lambda x : x > 0,[1,-2,3,-5,8,-3]))


# 5. 234 라는 10진수의 16진수는 다음과 같이 구한다.
# hex(234)
# 이번에는 반대로 16진수 문자열 0xea를 10진수로 변경 해보자.
int('0xea', 16)


# 6. map과 lambda 를 사용하여 [1,2,3,4] 리스트의 각 요소 값에 3이 곱해진 리스트 를 만들어 보자.
a = list(map(lambda x: x * 3, [1,2,3,4]))


# 7. 다음 리스트의 최대 값과 최소 값을 구하자.
a = [-8, 2, 7, 5, -3, 5, 0, 1]
max(a)
min(a)



# 8. 17/3 의 결과는 다음과 같다. -> 5.66666666667
#    위 결과 값을 소수점 4자리 까지만 반올림 하여 표시 해보자.

a = 17/3
round(a, 4)



# 9. 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트를 작성해 보자.
#  




# 10. os 모듈을 사용하여 다음과 같이 동작 하도록 코드를 작성해 보자.
# - c:\doit 디렉터리로 이동한다.
# - dir 명령을 실행하고 그 결과를 변수에 담는다.
# - dir 명령의 결과를 출력 한다.



# 11. glob 모듈을 사용하여 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.
import glob
a = glob.glob('경로1/경로2/*.py')


# 12. time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자. 2022/04/10 17/22/21
import time

t = time.localtime(time.time())
now = "{}/{}/{} {}/{}/{}".format(t[0], t[1], t[2], t[3], t[4], t[5])



# 13. random 모듈을 사용하여 로또 번호 를 생성해 보자. 중복 숫자 허용안함.
import random

a = []
for i in range(1, 7):
    b = random.randint(1,45)
    if b not in a:
        a.append(b)
        a.sort()
