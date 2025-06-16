# 📦  모듈과and라이브러리
st.header("📦 모듈and라이브러리")

# 1. 모듈 만들기
st.subheader("1. 모듈 만들기")

st.markdown("""
- 모듈(Module)은 `.py` 파일 하나로 변수, 함수, 클래스를 정의하여 외부에서 불러와 사용할 수 있도록 만든 코드 파일입니다.
- 예: `my_module.py` 라는 파일을 만들고 다음과 같은 내용을 넣습니다.
""")

code_module = '''
# my_module.py

# 변수 정의
my_var = 'my_var'

# 일반 함수 정의
def my_func():
    return 'my_func'

# 언더스코어(_)로 시작하는 함수는 외부 import 시 보통 숨겨집니다
def _my_private_func():
    return 'my_private_func'
'''
st.code(code_module, language='python')

# 2. 모듈 import 방법
st.subheader("2. 모듈을 import하는 방법")

st.markdown("""
아래 방법 중 하나로 외부 모듈을 불러올 수 있습니다:

1. `import my_module`  
   → `my_module.my_func()` 또는 `my_module.my_var`

2. `import my_module as mm`  
   → `mm.my_func()`

3. `from my_module import my_func`  
   → `my_func()`

4. `from my_module import *` (**비추천**)  
   → 모든 공개 요소 사용 가능하지만 가독성 저하
""")

# 예시 코드 출력만 (실행 X)
code_import = '''
import my_module

print(my_module.my_var)         # 'my_var'
print(my_module.my_func())      # 'my_func'

# 아래 함수는 언더스코어로 시작하므로 일반적으로 직접 접근은 하지 않음
# print(my_module._my_private_func())  # 사용 비추천
'''
st.code(code_import, language='python')

st.warning("⚠ 위 코드는 예시입니다. 실제로 사용하려면 `my_module.py` 파일이 같은 폴더에 존재해야 합니다.")


# 3. 모듈 import 예시
st.subheader("3. import 방식 예시")

st.markdown("### ✅ 1) `import 모듈명` 방식")

code_import1 = '''
import my_module

# 변수 호출
print(my_module.my_var)

# 일반 함수 호출
print(my_module.my_func())

# 프라이빗 함수 호출 (예외 처리)
try:
    print(my_module.my_private_func())
except Exception as e:
    print(e)

# 언더스코어 포함 직접 접근 (비권장)
print(my_module._my_private_func())
'''
st.code(code_import1, language='python')

st.markdown("#### ☑ 예상 출력 결과 (예시 텍스트)")
st.text("""
my_var
my_func
module 'my_module' has no attribute 'my_private_func'
my_private_func
""")

# 4. import as 별명
st.subheader("4. import 시 별명 사용 (`as`)")

st.markdown("### ✅ 2) `import 모듈명 as 별명` 방식")

code_import2 = '''
import my_module as mm

print(mm.my_var)
print(mm.my_func())
print(mm._my_private_func())  # 내부 함수 직접 접근 (비권장)
'''
st.code(code_import2, language='python')

st.markdown("#### ☑ 예상 출력 결과 (예시 텍스트)")
st.text("""
my_var
my_func
my_private_func
""")

st.warning("⚠ 실제 실행하려면 `my_module.py` 파일이 현재 .py 파일과 같은 폴더에 있어야 합니다.")


# 5. 외부 라이브러리 사용: NumPy와 Matplotlib
st.subheader("5. 외부 라이브러리 사용 예시")

st.markdown("""
- **NumPy**: 수학/과학 계산에 사용하는 핵심 라이브러리  
- **Matplotlib**: 시각화를 위한 대표적인 그래프 라이브러리  
- `import numpy`, `import matplotlib.pyplot as plt` 형태로 주로 사용됩니다.
""")

# 코드 예시 출력
code_numpy_plot = '''
import numpy
import matplotlib.pyplot as plt

# 리스트 합 구하기
print(f'numpy.sum([1,2,3,4,5]) = {numpy.sum([1,2,3,4,5])}')

# 그래프 그리기
plt.plot([10,20,30,40], [1,4,9,16], 'rs--')
plt.plot([10,20,30,40], [11,24,9,6], 'g^-')
plt.show()
'''
st.code(code_numpy_plot, language='python')

# 실제 실행 (Streamlit-safe 방식)
import numpy as np
import matplotlib.pyplot as plt

# numpy 합계 출력
np_sum_result = np.sum([1, 2, 3, 4, 5])
st.write(f"numpy.sum([1,2,3,4,5]) = {np_sum_result}")

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot([10,20,30,40], [1,4,9,16], 'rs--', label='red square line')
ax.plot([10,20,30,40], [11,24,9,6], 'g^-', label='green triangle line')
ax.legend()
st.pyplot(fig)


