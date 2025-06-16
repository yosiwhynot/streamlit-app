import streamlit as st

# 제목
st.title("📘 리스트 컴프리헨션과 map 함수 사용 예제")

# 설명
st.write("Python에서 리스트를 다루는 다양한 방법에 대해 알아봅니다.")

# 코드 예제 1
st.subheader("1. 리스트 컴프리헨션")
code1 = """
nums_comp = [num+10 for num in range(1, 6)]
print(f'nums_comp = {nums_comp}')
"""
st.code(code1, language='python')

# 코드 예제 실행 결과
nums_comp = [num+10 for num in range(1, 6)]
st.write("실행 결과:", nums_comp)

# 코드 예제 2
st.subheader("2. map 함수")
code2 = """
def add_ten(num):
    return num + 10

nums_map = list(map(add_ten, range(1, 6)))
print(f'nums_map = {nums_map}')
"""
st.code(code2, language='python')

def add_ten(num):
    return num + 10

nums_map = list(map(add_ten, range(1, 6)))
st.write("실행 결과:", nums_map)
