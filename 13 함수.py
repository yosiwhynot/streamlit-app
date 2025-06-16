import streamlit as st
import numpy as np

st.title("📘 파이썬 함수의 정의와 호출")

# 1. 함수의 정의
st.subheader("1. 함수의 정의")

code1 = """
def 함수명(매개변수1, 매개변수2=기본값, ...):
    실행문1
    실행문2
    ...
    return 반환값
"""
st.code(code1, language='python')

st.markdown("""
- `def` 키워드로 정의하고, 괄호 안에 매개변수 작성  
- `parameter`는 외부에서 입력으로 전달되는 변수  
- `return` 키워드로 결과를 반환 (없으면 `None` 반환)  
""")

# 2. 함수명 작성법
st.subheader("2. 함수명 작성법")

st.markdown("""
- 함수 이름은 **기능을 알 수 있도록** 명확하게  
- 관례적으로 `snake_case` 사용, 최근엔 `camelCase`도 일부 사용됨  
""")

st.code("""
snake_case 예: sort_array, get_data  
camelCase 예: sortArray, getData
""", language='text')

# 3. 함수 예제 정의
st.subheader("3. 함수 정의 예제: 두 수의 합과 곱")

code2 = '''
def calcSumProduct(a, b):
    plus = a + b
    multiple = a * b
    return plus, multiple
'''
st.code(code2, language='python')

def calcSumProduct(a, b):
    plus = a + b
    multiple = a * b
    return plus, multiple

result = calcSumProduct(3, 5)
st.write("실행 결과 (3, 5):", result)

# 4. 반환값을 변수 없이 바로 사용하는 경우
st.subheader("4. 반환값을 변수 없이 바로 사용하는 경우")

code4 = '''
print(calcSumProduct(2, 5))
'''
st.code(code4, language='python')

st.write("실행 결과:", calcSumProduct(2, 5))

# 5. 반환값 중 하나만 사용하는 예제
st.subheader("5. 반환값 중 하나만 사용하는 경우")

code5 = '''
sum, _ = calcSumProduct(4, 6)
print(f'sum = {sum}')
'''
st.code(code5, language='python')

sum_only, _ = calcSumProduct(4, 6)
st.write("실행 결과: sum =", sum_only)

# 6. 튜플로 반환값 받기
st.subheader("6. 튜플 형태로 반환값 받기")

code6 = '''
result = calcSumProduct(5, 2)
print(result)
'''
st.code(code6, language='python')

result_tuple = calcSumProduct(5, 2)
st.write("실행 결과 (튜플 전체):", result_tuple)

# 7. 함수 주석과 타입 힌트
st.subheader("7. 함수 주석과 타입 힌트")

st.markdown("""
- 함수 설명은 `"""` 또는 `'''`로 작성  
- 매개변수 타입: `변수명: 자료형`  
- 반환 타입: `-> 자료형`  
- `help(함수)`로 확인 가능 (Streamlit에서는 텍스트로 예시 제공)  
""")

code7 = '''
def calcSumProduct(a: int, b: int = 10) -> int:
    """
    calcSumProduct 함수는 a와 b를 더한 값과 곱한 값을 튜플로 반환하는 함수이다.
    """
    plus = a + b
    multiple = a * b
    return plus, multiple
'''
st.code(code7, language='python')

def calcSumProduct(a: int, b: int = 10) -> int:
    plus = a + b
    multiple = a * b
    return plus, multiple

st.write("f-string 사용 예시:")
a, b = 3, 5
st.write(f"a = {a}, b = {b} → 더한 값 = {a + b}, 곱한 값 = {a * b}")

st.subheader("📌 help(calcSumProduct) 호출 예시")
st.code("""
Help on function calcSumProduct in module __main__:

calcSumProduct(a: int, b: int = 10) -> int
    calcSumProduct 함수는 a와 b를 더한 값과 곱한 값을 튜플로 반환하는 함수이다.
""", language='text')

# 8. *args 활용
st.subheader("8. 인수의 개수가 정해지지 않은 함수 (*args)")

st.markdown("""
- `*args`는 여러 개의 위치 인수를 받을 수 있습니다.  
- 내부에서는 `tuple`로 처리됩니다.  
""")

code_args = '''
def calcSumProduct2(*inputs):
    """
    입력값들의 합과 곱을 반환하는 함수 (*args 사용)
    """
    import numpy as np
    plus = np.sum(inputs)
    multiple = np.prod(inputs)
    return plus, multiple
'''
st.code(code_args, language='python')

def calcSumProduct2(*inputs):
    plus = np.sum(inputs)
    multiple = np.prod(inputs)
    return plus, multiple

sum1, product1 = calcSumProduct2(1, 2, 3)
st.write("입력값: (1, 2, 3) → 합:", sum1, ", 곱:", product1)

sum2, product2 = calcSumProduct2(1, 2, 3, 4, 5, 6, 7, 8)
st.write("입력값: (1 ~ 8) → 합:", sum2, ", 곱:", product2)

# 9. **kwargs 활용
st.subheader("9. 인수의 개수가 정해지지 않은 함수 (**kwargs)")

st.markdown("""
- `**kwargs`는 여러 개의 이름있는 인자들을 딕셔너리 형태로 받아 처리  
- 내부에서는 `dict`로 사용하며 `.items()`로 key-value 순회 가능  
""")

code_kwargs = '''
def calcSumProduct2(**inputs):
    """
    입력된 key-value 값들의 합과 곱을 반환하는 함수 (**kwargs 사용)
    """
    plus = 0
    multiple = 1
    for _, value in inputs.items():
        plus += value
        multiple *= value
    return plus, multiple
'''
st.code(code_kwargs, language='python')

def calcSumProduct2(**inputs):
    plus = 0
    multiple = 1
    for _, value in inputs.items():
        plus += value
        multiple *= value
    return plus, multiple

sum3, product3 = calcSumProduct2(a=1, b=2)
st.write("입력값: {'a': 1, 'b': 2} → 합:", sum3, ", 곱:", product3)

sum4, product4 = calcSumProduct2(a=1, b=2, c=3, d=4)
st.write("입력값: {'a': 1, 'b': 2, 'c': 3, 'd': 4} → 합:", sum4, ", 곱:", product4)
