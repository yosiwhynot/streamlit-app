import streamlit as st

st.title("📘 리스트 생성 방법 비교: 리스트 컴프리헨션 vs for문 vs map 함수")

# 1. 리스트 컴프리헨션
st.subheader("1. 리스트 컴프리헨션")
code1 = """
nums_comp = [num + 10 for num in range(1, 6)]
print(f'nums_comp = {nums_comp}')
"""
st.code(code1, language='python')

nums_comp = [num + 10 for num in range(1, 6)]
st.write("실행 결과:", nums_comp)

# 2. for문을 사용한 리스트 생성
st.subheader("2. for문을 사용한 리스트 생성")
code2 = """
nums_for = []
for num in range(1, 6):
    nums_for.append(num + 10)
print(f'nums_for = {nums_for}')
"""
st.code(code2, language='python')

nums_for = []
for num in range(1, 6):
    nums_for.append(num + 10)
st.write("실행 결과:", nums_for)

# 3. map 함수 사용
st.subheader("3. map 함수를 사용한 리스트 생성")
code3 = """
def add_ten(num):
    return num + 10

nums_map = list(map(add_ten, range(1, 6)))
print(f'nums_map = {nums_map}')
"""
st.code(code3, language='python')

def add_ten(num):
    return num + 10

nums_map = list(map(add_ten, range(1, 6)))
st.write("실행 결과:", nums_map)


# 4. 함수 적용한 리스트 컴프리헨션
st.subheader("4. 함수를 적용한 리스트 컴프리헨션")

code4 = """
def addString(x):
    return 'int_' + str(x)

nums_func = [addString(num) for num in range(1, 6)]
print(f'nums_func = {nums_func}')
"""
st.code(code4, language='python')

def addString(x):
    return 'int_' + str(x)

nums_func = [addString(num) for num in range(1, 6)]
st.write("실행 결과:", nums_func)


# 5. if 조건문을 적용한 리스트 컴프리헨션
st.subheader("5. if 조건문을 적용한 리스트 컴프리헨션")

# if만 있는 경우
code5a = """
nums_odds = [num for num in range(1, 6) if num % 2 == 1]
print(f'nums_odds = {nums_odds}')
"""
st.code(code5a, language='python')

nums_odds = [num for num in range(1, 6) if num % 2 == 1]
st.write("홀수만 추가된 리스트:", nums_odds)

# if-else를 사용하는 경우
code5b = """
nums_odds_zero = [num if num % 2 == 1 else 0 for num in range(1, 6)]
print(f'nums_odds_zero = {nums_odds_zero}')
"""
st.code(code5b, language='python')

nums_odds_zero = [num if num % 2 == 1 else 0 for num in range(1, 6)]
st.write("홀수는 그대로, 짝수는 0으로:", nums_odds_zero)

# if + 여러 조건문
code5c = """
nums_odds_less6 = [num for num in range(1, 6) if num % 2 == 1 if num < 4]
print(f'nums_odds_less6 = {nums_odds_less6}')
"""
st.code(code5c, language='python')

nums_odds_less6 = [num for num in range(1, 6) if num % 2 == 1 if num < 4]
st.write("홀수이면서 4 미만인 값만:", nums_odds_less6)


# 6. 중첩 리스트 컴프리헨션
st.subheader("6. 중첩 리스트 컴프리헨션")

# 예제 1: x, y 조합 만들기
code6a = """
nums_pairs = [(x, y) for x in range(1, 4) for y in ['a', 'b', 'c']]
print(f'nums_pairs = {nums_pairs}')
"""
st.code(code6a, language='python')

nums_pairs = [(x, y) for x in range(1, 4) for y in ['a', 'b', 'c']]
st.write("모든 조합 결과:", nums_pairs)

# 예제 2: 조건 추가
code6b = """
num_pairs_sum5 = [(x, y) for x in range(1, 6) for y in range(1, 6) if x + y == 5]
print(f'num_pairs_sum5 = {num_pairs_sum5}')
"""
st.code(code6b, language='python')

num_pairs_sum5 = [(x, y) for x in range(1, 6) for y in range(1, 6) if x + y == 5]
st.write("x + y = 5인 조합:", num_pairs_sum5)


# 7. 딕셔너리 컴프리헨션
st.subheader("7. 딕셔너리 컴프리헨션")

# 예제 1: 일반적인 for문 방식
code7a = """
ids = [1, 2, 3, 4]
student_names = ['김정욱이', '이광민이', '박현섭', '최덕선']
students_for = {id: name for id, name in zip(ids, student_names)}
print(f'students_for = {students_for}')
"""
st.code(code7a, language='python')

ids = [1, 2, 3, 4]
student_names = ['김정욱이', '이광민이', '박현섭', '최덕선']
students_for = {id: name for id, name in zip(ids, student_names)}
st.write("딕셔너리(zip 사용):", students_for)

# 예제 2: enumerate 사용
code7b = """
student_names = ['김정욱이', '이광민이', '박현섭', '최덕선']
students_enum = {i+1: name for i, name in enumerate(student_names)}
print(f'students_enum = {students_enum}')
"""
st.code(code7b, language='python')

student_names = ['김정욱이', '이광민이', '박현섭', '최덕선']
students_enum = {i+1: name for i, name in enumerate(student_names)}
st.write("딕셔너리(enumerate 사용):", students_enum)

# 예제 3: zip을 딕셔너리로
code7c = """
ids = [1, 2, 3, 4]
student_names = ['김정욱이', '이광민이', '박현섭', '최덕선']
students_zip = dict(zip(ids, student_names))
print(f'students_zip = {students_zip}')
"""
st.code(code7c, language='python')

ids = [1, 2, 3, 4]
student_names = ['김정욱이', '이광민이', '박현섭', '최덕선']
students_zip = dict(zip(ids, student_names))
st.write("딕셔너리(dict + zip):", students_zip)


# 8. Set 컴프리헨션
st.subheader("8. Set 컴프리헨션")

code8a = """
sum_list = [x + y for x in range(1, 6) for y in range(1, 6)]
print(f'sum_list = {sum_list}')
"""
st.code(code8a, language='python')

sum_list = [x + y for x in range(1, 6) for y in range(1, 6)]
st.write("중복을 허용하는 리스트:", sum_list)

code8b = """
sum_set = {x + y for x in range(1, 6) for y in range(1, 6)}
print(f'sum_set = {sum_set}')
"""
st.code(code8b, language='python')

sum_set = {x + y for x in range(1, 6) for y in range(1, 6)}
st.write("중복 없이 저장되는 세트:", sum_set)


# 9. Tuple 컴프리헨션 (제너레이터 표현식)
st.subheader("9. Tuple 컴프리헨션 (제너레이터 표현식)")

code9a = """
nums_pairs_list = [(x, y) for x in range(1, 3) for y in ['a', 'b', 'c']]
print(f'nums_pairs_list = {nums_pairs_list}')
"""
st.code(code9a, language='python')

nums_pairs_list = [(x, y) for x in range(1, 3) for y in ['a', 'b', 'c']]
st.write("리스트로 저장된 쌍:", nums_pairs_list)

code9b = """
nums_pairs_gen = ((x, y) for x in range(1, 3) for y in ['a', 'b', 'c'])
print(f'nums_pairs_gen = {nums_pairs_gen}')
"""
st.code(code9b, language='python')

nums_pairs_gen = ((x, y) for x in range(1, 3) for y in ['a', 'b', 'c'])
st.write("제너레이터 표현식 결과:", nums_pairs_gen)
st.write("제너레이터를 튜플로 변환:", tuple(nums_pairs_gen))

code9c = """
nums_pairs_tuple = tuple((x, y) for x in range(1, 3) for y in ['a', 'b', 'c'])
print(f'nums_pairs_tuple = {nums_pairs_tuple}')
"""
st.code(code9c, language='python')

nums_pairs_tuple = tuple((x, y) for x in range(1, 3) for y in ['a', 'b', 'c'])
st.write("한 번에 튜플로 변환:", nums_pairs_tuple)
