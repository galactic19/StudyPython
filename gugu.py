# 06 -1 단원 
# 단을 입력받아 구구단을 출력 하게 만들어 보자. 리스트로 출력하자.

def GuGu(dan):
    a = []
    for i in range(1,10):
        a.append(int(dan) * i)
    return a

a = input('단을 입력하세요')
print(GuGu(a))



# 06- 2 단원
# 3과 5의 배수 합하기. 3과 5의 배수중 중복 값은 중복 되지 않게 처리하기.

num = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        num += i
print(num)


# 06 -3 단원
# 게시판 페이징 하기
# 함수 이름은 getTotalPage  게시물 총 건수(m) , 한페이지에 보여줄 게시물(n) 수  출력하는 값은 총 페이지 수.

def getTotalPage(n, m) :
    if m % n == 0:
        total = m / n
    else:
        total = (m // n) + 1
    return int(total)

print(getTotalPage(5, 11))
print(getTotalPage(5, 10))
print(getTotalPage(5, 1))


# 06 -4 간단한 메모장 만들기.
# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장.

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    
f.close()
print(memo)



# 06 -5 탭을 4개의 공백으로 바꾸기.
f = open('samole.txt')
content = f.read()
new_content = content.replace("\t", ' '*4)
f.close()

f = open('file.txt', 'a')
f.write(new_content)
f.close()


# 06 -6 하위 디렉토리 검사하기.
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        print('권한이 없어 접근할 수 없는 에러가 발생 했습니다.')
        pass
    

print('검색을 시작합니다.')
search('d:/')
print('검색이 끝났습니다.')