# 3장 연습문제

# 1. 다음 코드의 결과값은 무엇일까.

# a = "Life is too short, you need python"
# if "wife" in a: print("wife")
# elif "python" in a and "you" not in a: print("python")
# elif "shirt" not in a: print("shirt")
# elif "need" in a: print("need")
# else: print("none")

result = """ shirt 가 True 라고 보여짐. 이유는 not 연산자가 붙을 경우 False가 True로 뒤바뀌기 때문에 True를 가져 코드를 실행함. """


# 2.while 문을 사용해 1부터 1000 까지의 자연수 중 3의 배수의 합을 구하라.
a = [1, 1001, 0]
while a[0] < a[1]:
    if a[0] % 3 == 0:
        a[2] += a[0]
        
    a[0] += 1
    
print(a[2])


# 3.while문을 사용하여 별(*)을 표시하라.
# *
# **
# ***
# ****
# *****

star = [1, '*']
while star[0] < 6:
    print('*' * star[0])
    star[0] += 1



# 4.for문을 사용해 1부터 100까지의 숫자를 출력하자.
for i in range(1, 101):
    print(i)
    


# 5. for문을 사용하여 A학급의 평균 점수를 구하자.
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
score = 0
for i in a:
    score += i
    
score = score / len(a)
print('A 반의 평균 점수는 {}점 입니다.'.format(score))



# 6. 아래 코드를 리스트 내포 코드로 변환 해보자.
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)
