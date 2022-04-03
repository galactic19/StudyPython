# 점프 투 파이썬 02 연습 문제

# 1.홍길동의 평균 점수를 구하자. 국어:80, 영어:75, 수학:55

hong = {'국어':80, '영어':75, '수학':55}
score = 0
for i in hong:
    score += hong[i]

score = score/len(hong)
print('홍길동의 평균 점수는 {}점 입니다.'.format(score))


# 2.자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해보자.
num = 13
if(num%2 != 0):
    print('짝수입니다.')


# 3.홍길동의 주민번호를 연월일 부분과 그 뒤 숫자부분으로 나누어 출력하자.
jumin = '881120-1068234'
jumin_num = jumin.split('-')

print(jumin_num[0], jumin_num[1])


# 4.주민번호 뒷자리의 맨 첫번째 숫자를 출력해보자.
print(jumin_num[1][0:1])


# 5. 문자열 a:b:c:d 를 a#b#c#d로 바꿔 출력하자.
abc = 'a:b:c:d'
abc = abc.replace(':', '#')
print(abc)


# 6.[1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어 보자.
lst = [1,3,5,4,2]
lst.sort()
lst.reverse()
print(lst)


# 7.['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
tooShort = ','.join(['Life', 'is', 'too', 'short'])
tooShort = tooShort.replace(',', ' ')
print(tooShort)


# 8.(1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
tp = 1,2,3
tp = tp + (4,)
print(tp)


# 9.다음과 같은 딕셔너리 a가 있다.
# >>> a = dict()
# >>> a
# {}

# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
# a['name'] = 'python'
# a[('a',)] = 'python' <-- 오류 발생. 이유는 값을 넣을때는 ['name'] 형식으로 삽입 가능하며, 인덱스 네임의 형식이 틀렸다.
# a[[1]] = 'python' <-- 오류 발생. 이유는 첫번째 인덱스가 없이 두번째 인덱스로 접근하려 하고 있으며, 이중 리스트라면 [0][1] 과 같은 형식으로 접근 해야한다.
# a[250] = 'python'


# 10.딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
a = {'A':90, 'B':80, 'C':70}
b = a.pop('B')
print(b)


# 11. a리스트에서 중복 숫자를 제거해 보자.
uniqNum = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
uniqNum = set(uniqNum)
print(uniqNum)


# 12. 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 
#     다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 
#     그리고 이런 결과가 오는 이유에 대해 설명해 보자.

a = b = [1,2,3]
a[1] = 4
print(b) 

#  답변 : 변수의 값이 같으므로, 별개의 변수로 인식하지 않고, 하나의 메모리를 참조한다.
#  id(a), id(b) 를 해본다면 메모리 참조값이 같은것을 확인할 수 있고, a값을 변경하면 b값도 함께 변경한다.
#  만약 a,와b를 다르게 생성하고 싶다면 b = a[:] , 또는 copy 모듈을 사용해 copy(a) 와 같은식으로 처리해야 한다.

