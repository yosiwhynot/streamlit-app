import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'x': [10, 20, 30, 40],
    'y1': [1, 4, 9, 16],
    'y2': [11, 24, 9, 6]
})
st.line_chart(df.set_index('x'))

st.title("📦 모듈과 라이브러리")

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

st.warning("이 예제에서는 my_module 내용을 아래에 직접 구현하여 오류 없이 실행됩니다.")

# 실제 모듈처럼 기능 구현
class my_module:
    my_var = 'my_var'
    @staticmethod
    def my_func():
        return 'my_func'
    @staticmethod
    def _my_private_func():
        return 'my_private_func'


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

code_import = '''
import my_module

print(my_module.my_var)         # 'my_var'
print(my_module.my_func())      # 'my_func'

# 언더스코어로 시작하는 함수는 일반적으로 숨겨진 기능
# print(my_module._my_private_func())  # 사용 비추천
'''
st.code(code_import, language='python')


# 3. import 예시 실행
st.subheader("3. 모듈 import 예시")

st.markdown("### ✅ 1) `import 모듈명` 방식")

try:
    st.write("my_module.my_var:", my_module.my_var)
    st.write("my_module.my_func():", my_module.my_func())
    # 의도적 오류 처리 예시
    st.write("my_module.my_private_func(): (예외 처리 예시)")
    try:
        st.write(my_module.my_private_func())  # 존재하지 않음
    except Exception as e:
        st.write("오류 발생:", str(e))
    st.write("my_module._my_private_func():", my_module._my_private_func())
except Exception as e:
    st.error(str(e))

# 4. import 별명 사용
st.subheader("4. import 별명 사용 (`as`)")

mm = my_module
st.write("mm.my_var:", mm.my_var)
st.write("mm.my_func():", mm.my_func())
st.write("mm._my_private_func():", mm._my_private_func())

# 5. 외부 라이브러리 사용
st.subheader("5. 외부 라이브러리 사용 예시")

st.markdown("""
- **NumPy**: 수학/과학 계산에 사용하는 핵심 라이브러리  
- **Matplotlib**: 시각화를 위한 대표적인 그래프 라이브러리  
""")

st.write("numpy.sum([1,2,3,4,5]) =", np.sum([1, 2, 3, 4, 5]))

fig, ax = plt.subplots()
ax.plot([10, 20, 30, 40], [1, 4, 9, 16], 'rs--', label='red square line')
ax.plot([10, 20, 30, 40], [11, 24, 9, 6], 'g^-', label='green triangle line')
ax.legend()
st.pyplot(fig)
