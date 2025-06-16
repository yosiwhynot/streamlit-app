import streamlit as st

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

code2 = """
def calcSumProduct(a, b):
    plus = a + b
    multiple = a * b
    return plus, multiple
"""
st.code(code2, language='python')

# 함수 실행 및 결과 출력
def calcSumProduct(a, b):
    plus = a + b
    multiple = a * b
    return plus, multiple

result = calcSumProduct(3, 5)
st.write("실행 결과 (3, 5):", result)

# 4. 반환값을 변수 없이 바로 사용하는 예제
st.subheader("4. 반환값을 변수 없이 바로 사용하는 경우")

code4 = """
print(calcSumProduct(2, 5))
"""
st.code(code4, language='python')

st.write("실행 결과:", calcSumProduct(2, 5))

# 5. 반환값 중 하나만 사용하는 예제
st.subheader("5. 반환값 중 하나만 사용하는 경우")

code5 = """
sum, _ = calcSumProduct(4, 6)
print(f'sum = {sum}')
"""
st.code(code5, language='python')

sum_only, _ = calcSumProduct(4, 6)
st.write("실행 결과: sum =", sum_only)

# 6. 튜플로 반환값 한 번에 받기
st.subheader("6. 튜플 형태로 반환값 받기")

code6 = """
result = calcSumProduct(5, 2)
print(result)  # (sum, product)
"""
st.code(code6, language='python')

result_tuple = calcSumProduct(5, 2)
st.write("실행 결과 (튜플 전체):", result_tuple)


# 7. 함수 주석 (Function Annotation)
st.subheader("7. 함수 주석과 타입 힌트")

st.markdown("""
- 함수에 대한 설명은 **함수 바로 아래에 큰따옴표 3개(`"""`)로 작성**  
- **매개변수**에 대한 타입은 `변수명: 자료형`  
- **반환값**에 대한 타입은 `-> 자료형` 형식으로 함수 뒤에 작성  
- `help(함수이름)`으로 함수 주석과 정의를 확인할 수 있음
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

# 실사용 함수 정의
def calcSumProduct(a: int, b: int = 10) -> int:
    """
    calcSumProduct 함수는 a와 b를 더한 값과 곱한 값을 튜플로 반환하는 함수이다.
    """
    plus = a + b
    multiple = a * b
    return plus, multiple

# f-string 예시
st.markdown("**f-string을 사용한 결과 출력 예시:**")
a, b = 3, 5
st.write(f"a = {a}, b = {b} → 더한 값 = {a + b}, 곱한 값 = {a * b}")

# help 결과는 터미널에서 실행해야 보이므로 텍스트로 대신 출력
st.subheader("📌 help(calcSumProduct) 호출 예시 (터미널에서 실행)")
st.code("""
Help on function calcSumProduct in module __main__:

calcSumProduct(a: int, b: int = 10) -> int
    calcSumProduct 함수는 a와 b를 더한 값과 곱한 값을 튜플로 반환하는 함수이다.
""", language="text")



import numpy as np  # numpy는 한 번만 import 되므로 중복해도 괜찮음

# 8. 인수의 개수가 정해지지 않은 함수 (*args)
st.subheader("8. 인수의 개수가 정해지지 않은 함수 (*args)")

st.markdown("""
- `*args`는 **튜플 형태로 인수**를 받아 처리할 수 있게 해주는 기능입니다.  
- 인자의 개수가 유동적일 때 유용하게 사용됩니다.  
- 예제에서는 NumPy를 활용해 입력값의 **합과 곱**을 계산합니다.
""")

# 함수 정의 코드 블럭
code_args_def = """
import numpy as np

def calcSumProduct2(*inputs):
    \"""
    calcSumProduct2 함수는 입력된 값들의 합과 곱을 튜플로 반환합니다.
    \"""
    print(f'inputs = {inputs}')
    plus = np.sum(inputs)
    multiple = np.prod(inputs)
    return plus, multiple
"""
st.code(code_args_def, language='python')

# 실제 함수 정의
def calcSumProduct2(*inputs):
    """
    calcSumProduct2 함수는 입력된 값들의 합과 곱을 튜플로 반환합니다.
    """
    plus = np.sum(inputs)
    multiple = np.prod(inputs)
    return plus, multiple

# 예제 1: (1, 2, 3)
st.subheader("예제 1: 입력값 (1, 2, 3)")

code_args_call1 = """
sum, product = calcSumProduct2(1, 2, 3)
print(f'sum = {sum}, product = {product}')
"""
st.code(code_args_call1, language='python')

sum1, product1 = calcSumProduct2(1, 2, 3)
st.write(f"입력값: (1, 2, 3) → 합: {sum1}, 곱: {product1}")

# 예제 2: (1, 2, 3, 4, 5, 6, 7, 8)
st.subheader("예제 2: 입력값 (1 ~ 8)")

code_args_call2 = """
sum, product = calcSumProduct2(1, 2, 3, 4, 5, 6, 7, 8)
print(f'sum = {sum}, product = {product}')
"""
st.code(code_args_call2, language='python')

sum2, product2 = calcSumProduct2(1, 2, 3, 4, 5, 6, 7, 8)
st.write(f"입력값: (1 ~ 8) → 합: {sum2}, 곱: {product2}")


# 9. 인수의 개수가 정해지지 않은 함수 (**kwargs)
st.subheader("9. 인수의 개수가 정해지지 않은 함수 (**kwargs)")

st.markdown("""
- `**kwargs`는 **딕셔너리 형태의 인자(key=value)**를 여러 개 받을 수 있도록 해줍니다.  
- 함수 내부에서는 `kwargs`가 딕셔너리로 처리되므로 `.items()`로 순회 가능  
""")

# 함수 정의 코드
code_kwargs = """
def calcSumProduct2(**inputs):
    \"""
    calcSumProduct2 함수는 key-value 형태로 전달된 값들의 합과 곱을 반환합니다.
    \"""
    print(f'inputs = {inputs}')
    plus = 0
    multiple = 1
    for _, value in inputs.items():
        plus += value
        multiple *= value
    return plus, multiple
"""
st.code(code_kwargs, language='python')

# 실제 함수 정의
def calcSumProduct2(**inputs):
    plus = 0
    multiple = 1
    for _, value in inputs.items():
        plus += value
        multiple *= value
    return plus, multiple

# 예제 1: a=1, b=2
st.subheader("예제 1: 입력값 a=1, b=2")

code_kwargs_call1 = """
sum, product = calcSumProduct2(a=1, b=2)
print(f'sum = {sum}, product = {product}')
"""
st.code(code_kwargs_call1, language='python')

sum1, product1 = calcSumProduct2(a=1, b=2)
st.write(f"입력값: {{'a': 1, 'b': 2}} → 합: {sum1}, 곱: {product1}")

# 예제 2: a=1, b=2, c=3, d=4
st.subheader("예제 2: 입력값 a=1, b=2, c=3, d=4")

code_kwargs_call2 = """
sum, product = calcSumProduct2(a=1, b=2, c=3, d=4)
print(f'sum = {sum}, product = {product}')
"""
st.code(code_kwargs_call2, language='python')

sum2, product2 = calcSumProduct2(a=1, b=2, c=3, d=4)
st.write(f"입력값: {{'a': 1, 'b': 2, 'c': 3, 'd': 4}} → 합: {sum2}, 곱: {product2}")


