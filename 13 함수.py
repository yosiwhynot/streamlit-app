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

# 3. 함수 정의 예제
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

# 6. 튜플 형태로 반환값 받기
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
- 함수 설명은 <code>\"\"\"</code> 또는 <code>'''</code>로 작성  
- 매개변수 타입: <code>변수명: 자료형</code>  
- 반환 타입: <code>-> 자료형</code>  
- <code>help(함수)</code>로 확인 가능 (Streamlit에서는 텍스트로 예시 제공)  
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
def calcSumProductArgs(*inputs):
    """
    입력값들의 합과 곱을 반환하는 함수 (*args 사용)
    """
    import numpy as np
    plus = np.sum(inputs)
    multiple = np.prod(inputs)
    return plus, multiple
'''
st.code(code_args, language='python')

def calcSumProductArgs(*inputs):
    plus = np.sum(inputs)
    multiple = np.prod(inputs)
    return plus, multiple

sum1, product1 = calcSumProductArgs(1, 2, 3)
st.write("입력값: (1, 2, 3) → 합:", sum1, ", 곱:", product1)

sum2, product2 = calcSumProductArgs(1, 2, 3, 4, 5, 6, 7, 8)
st.write("입력값: (1 ~ 8) → 합:", sum2, ", 곱:", product2)

# 9. **kwargs 활용
st.subheader("9. 인수의 개수가 정해지지 않은 함수 (**kwargs)")

st.markdown("""
- `**kwargs`는 여러 개의 이름있는 인자들을 딕셔너리 형태로 받아 처리  
- 내부에서는 `dict`로 사용하며 `.items()`로 key-value 순회 가능  
""")

code_kwargs = '''
def calcSumProductKwargs(**inputs):
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

def calcSumProductKwargs(**inputs):
    plus = 0
    multiple = 1
    for _, value in inputs.items():
        plus += value
        multiple *= value
    return plus, multiple

sum3, product3 = calcSumProductKwargs(a=1, b=2)
st.write("입력값: {'a': 1, 'b': 2} → 합:", sum3, ", 곱:", product3)

sum4, product4 = calcSumProductKwargs(a=1, b=2, c=3, d=4)
st.write("입력값: {'a': 1, 'b': 2, 'c': 3, 'd': 4} → 합:", sum4, ", 곱:", product4)

# 10. 지역변수와 전역변수
st.subheader("10. 지역변수와 전역변수")

st.markdown("""
- **지역변수(local)**: 함수 내에서 선언, 함수 호출 시 생성되고 종료 시 소멸됨  
- **전역변수(global)**: 함수 밖에서 선언, 프로그램 종료 전까지 유지됨  
- 함수 내에서 전역변수를 **변경하려면 `global` 키워드 필요**  
""")

code_scope = '''
# 전역 변수 선언
var_global = '전역 변수'

# 함수 정의
def useGlobalVariable(var_local):
    print(f'[함수 내] 전역 변수 출력: {var_global}')
    print(f'[함수 내] 지역 변수 출력: {var_local}')

# 지역 변수는 함수 호출 시 인자로 전달
useGlobalVariable('입력된 지역 변수')

# 전역 변수는 함수 바깥에서도 사용 가능
print(f'[함수 밖] 전역 변수: {var_global}')

# 지역 변수는 함수 밖에서는 사용 불가 → 예외 발생
try:
    print(f'[함수 밖] 지역 변수: {var_local}')
except NameError as e:
    print(e)
'''
st.code(code_scope, language='python')

# 실제 실행 (Streamlit-safe 방식)
st.markdown("### 🔧 실행 결과")

var_global = '전역 변수'

def useGlobalVariable(var_local):
    global_output = f"[함수 내] 전역 변수 출력: {var_global}"
    local_output = f"[함수 내] 지역 변수 출력: {var_local}"
    return global_output, local_output

out1, out2 = useGlobalVariable('입력된 지역 변수')

st.text(out1)
st.text(out2)
st.text(f"[함수 밖] 전역 변수: {var_global}")

try:
    st.text(f"[함수 밖] 지역 변수: {var_local}")
except NameError as e:
    st.text(f"[함수 밖] 지역 변수 오류: {e}")

# 11. 함수 내에서 전역변수의 변경 (global 없이)

st.subheader("11. 함수 내에서 전역변수의 변경 (global 없이)")

st.markdown("""
- 함수 내에서 전역변수와 **같은 이름의 변수를 새로 할당하면**, 전역변수는 변경되지 않고 **지역변수로 재정의**됨  
- 따라서 실제 전역변수를 변경하려면 `global` 키워드를 사용해야 함  
""")

code_global_fail = '''
var_global = '전역 변수'

def useGlobalVariable(var_local):
    var_global = '전역 변수 아닌 지역변수임'
    print(f"[함수 내] var_global = {var_global}")
    print(f"[함수 내] var_local = {var_local}")

useGlobalVariable('입력된 지역 변수')

# 함수 밖 전역 변수 출력
print(f"[함수 밖] var_global = {var_global}")
'''
st.code(code_global_fail, language='python')

# 실제 실행 결과
st.markdown("### 🔧 실행 결과")

var_global = '전역 변수'

def useGlobalVariable_local_override(var_local):
    var_global = '전역 변수 아닌 지역변수임'
    out1 = f"[함수 내] var_global = {var_global}"
    out2 = f"[함수 내] var_local = {var_local}"
    return out1, out2

a1, a2 = useGlobalVariable_local_override("입력된 지역 변수")
st.text(a1)
st.text(a2)
st.text(f"[함수 밖] var_global = {var_global}")


# 12. 함수 내 전역변수를 변경하는 방법 (global 사용)

st.subheader("12. 함수 내에서 전역변수를 변경하는 방법 (global 사용)")

st.markdown("""
- 함수 내부에서 전역변수를 **수정하려면 반드시 `global 변수명`** 을 먼저 선언해야 함  
- 이 경우 함수 안에서 변경된 값이 전역에 반영됨  
""")

code_global_success = '''
var_global = '전역 변수'

def useGlobalVariable(var_local):
    global var_global
    print(f"[함수 내] var_global = {var_global}")
    print(f"[함수 내] var_local = {var_local}")
    var_global = '이제는 전역 변수임'

useGlobalVariable('입력된 지역 변수')
print(f"[함수 밖] var_global = {var_global}")
'''
st.code(code_global_success, language='python')

# 실제 실행 결과
var_global = '전역 변수'

def useGlobalVariable_with_global(var_local):
    global var_global
    out1 = f"[함수 내] var_global = {var_global}"
    out2 = f"[함수 내] var_local = {var_local}"
    var_global = '이제는 전역 변수임'
    return out1, out2

b1, b2 = useGlobalVariable_with_global("입력된 지역 변수")
st.text(b1)
st.text(b2)
st.text(f"[함수 밖] var_global = {var_global}")


# 13. 람다 함수 (lambda function)
st.subheader("13. 람다 함수 (익명 함수)")

st.markdown("""
- **람다 함수**는 일반 함수를 간단히 표현할 수 있는 한 줄짜리 익명 함수입니다.  
- 기본 문법: `lambda 매개변수: 표현식`  
- 함수 이름 없이 바로 사용하거나 변수에 저장해 사용합니다.  
""")

# 일반 함수와 비교
code_lambda_basic = '''
# 일반 함수 정의
def addTen(x):
    return x + 10

# 일반 함수 호출
addTen(5)

# 람다 함수 정의 및 즉시 호출
(lambda x: x + 10)(5)

# 람다 함수를 변수에 저장하고 호출
addTen = lambda x: x + 10
addTen(5)
'''
st.code(code_lambda_basic, language='python')

# 실제 실행
st.markdown("### 🔧 실행 결과")

# 일반 함수
def addTen_normal(x):
    return x + 10

result_normal = addTen_normal(5)
result_lambda_inline = (lambda x: x + 10)(5)
addTen_lambda_named = lambda x: x + 10
result_named = addTen_lambda_named(5)

st.write("📌 일반 함수 호출: `addTen(5)` →", result_normal)
st.write("📌 람다 함수 직접 호출: `(lambda x: x+10)(5)` →", result_lambda_inline)
st.write("📌 람다 함수 변수 저장 후 호출: `addTen = lambda x: x+10; addTen(5)` →", result_named)


# 14. 람다 함수 응용
st.subheader("14. 람다 함수 응용")

# 1. 외부 변수 사용
st.markdown("### ✅ 1) 외부 변수 사용")

st.markdown("""
- 람다 함수 안에서는 **새로운 변수 생성은 불가**, 하지만 **외부 변수 참조는 가능**  
""")

code_lambda_outer = '''
y = 100
result = (lambda x: x + y)(5)
'''
st.code(code_lambda_outer, language='python')

y = 100
res_outer = (lambda x: x + y)(5)
st.write("y = 100일 때, (lambda x: x + y)(5) →", res_outer)

# 2. 조건부 표현식
st.markdown("### ✅ 2) 조건부 표현식")

st.markdown("""
- 람다 안에서도 `if ~ else` 구문 사용 가능  
- 예: 3의 배수일 때만 문자열 반환  
""")

code_conditional = '''
(lambda x: '3의 배수 ' + str(x) if x % 3 == 0 else x)(9)
'''
st.code(code_conditional, language='python')

res_cond = (lambda x: '3의 배수 ' + str(x) if x % 3 == 0 else x)(9)
st.write("입력 9 →", res_cond)

# 복합 조건문
st.markdown("**🧠 복합 조건문 (3으로 나누어떨어지면 str, 나머지가 1이면 float)**")

code_multi_cond = '''
(lambda x: '3의 배수 ' + str(x) if x % 3 == 0 
          else float(x) if x % 3 == 1 
          else x)(9)
'''
st.code(code_multi_cond, language='python')

res_multi = (lambda x: '3의 배수 ' + str(x) if x % 3 == 0 else float(x) if x % 3 == 1 else x)(9)
st.write("입력 9 →", res_multi)

# 3. 인자 여러 개
st.markdown("### ✅ 3) 인자 여러 개 사용")

st.markdown("""
- 람다 함수는 여러 개의 인자도 받을 수 있음  
- 예: `x`가 3의 배수면 `x`, 아니면 `x + y` 반환  
""")

code_multi_args = '''
(lambda x, y: x if x % 3 == 0 else x + y)(3, 4)
'''
st.code(code_multi_args, language='python')

res_multi_args = (lambda x, y: x if x % 3 == 0 else x + y)(3, 4)
st.write("입력 (3, 4) →", res_multi_args)


# 15. 람다 함수의 map() 활용
st.subheader("15. 람다 함수의 map() 활용")

st.markdown("""
- `map(함수, 반복가능한 객체)`는 각 요소에 함수를 적용한 결과를 반환합니다.  
- 람다 함수와 함께 사용하면 **짧은 변환 함수**를 효율적으로 작성할 수 있습니다.  
- 결과는 list로 감싸서 확인합니다.  
""")

# 예제 1: 각 요소에 +10
st.markdown("### ✅ 각 요소에 +10 적용")

code_map1 = '''
list(map(lambda x: x + 10, [1, 2, 3]))
'''
st.code(code_map1, language='python')

st.write("결과:", list(map(lambda x: x + 10, [1, 2, 3])))

# 예제 2: 조건부 문자열 처리
st.markdown("### ✅ 3의 배수면 문자열 반환, 아니면 원래 숫자")

code_map2 = '''
ldMultiple3 = lambda x: '3의 배수 ' + str(x) if x % 3 == 0 else x
list(map(ldMultiple3, range(10)))
'''
st.code(code_map2, language='python')

ldMultiple3 = lambda x: '3의 배수 ' + str(x) if x % 3 == 0 else x
st.write("결과:", list(map(ldMultiple3, range(10))))

# 예제 3: 복합 조건 처리 (3의 배수, 나머지 1이면 float, 아니면 그대로)
st.markdown("### ✅ 복합 조건 표현식 map 적용")

code_map3 = '''
ldMultiple3 = lambda x: '3의 배수 ' + str(x) if x % 3 == 0 
                else float(x) if x % 3 == 1 
                else x
list(map(ldMultiple3, range(10)))
'''
st.code(code_map3, language='python')

ldMultiple3 = lambda x: '3의 배수 ' + str(x) if x % 3 == 0 else float(x) if x % 3 == 1 else x
st.write("결과:", list(map(ldMultiple3, range(10))))

# 예제 4: map 함수에서 인자 2개 받기
st.markdown("### ✅ map에서 인자 여러 개: (x, y)")

code_map4 = '''
ldMultiple3 = lambda x, y: x if x % 3 == 0 else x + y
list(map(ldMultiple3, range(10), [100 + i for i in range(10)]))
'''
st.code(code_map4, language='python')

ldMultiple3 = lambda x, y: x if x % 3 == 0 else x + y
x_vals = list(range(10))
y_vals = list(range(100, 110))
st.write("입력 x:", x_vals)
st.write("입력 y:", y_vals)
st.write("결과:", list(map(ldMultiple3, x_vals, y_vals)))
