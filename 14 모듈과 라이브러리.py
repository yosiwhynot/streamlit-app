# 📦  모듈과 라이브러리
st.header("📦 모듈과 라이브러리")

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

