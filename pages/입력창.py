import streamlit as st
import random

st.title("여러 가지 입력창")

st.button("리셋 버튼", type="primary")
if st.button('랜덤 숫자 생성'):
    st.write(random.random())
else:
    st.write('Goodbye')

# 버튼 클릭하면 텍스트 문서 다운로드
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

# 링크 버튼
st.link_button("Go to gallery", "https://streamlit.io/gallery")

#체크 박스
agree = st.checkbox('동의합니다.')

if agree:
    st.write('동의하셨습니다. 다음 문항으로 넘어갑니다')
else:
    st.write("동의 버튼을 클릭해야 다음으로 넘어갑니다. ")


# 멀티 셀렉터
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']) # 마지막 줄은 기본 선택 값으로 셋팅 됨. 비어있어도 됨

st.write('You selected:', options)

# 라디오 버튼
genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")


# 숫자 입력
number = st.number_input("숫자를 입력하세요", value=None, placeholder="Type a number...")
st.write('The current number is ', number)

number1 = st.number_input("정수만 입렵됩니다", step = 1, value=None, placeholder="Type a number...")
st.write(f'입력한 결과는 {number1}입니다')

#텍스트 입력창
title = st.text_input('영화제목', 'Life of Brian')
st.write(title, '을 보셨군요!')

title = st.text_area('영화제목', 'Life of Brian')
st.write(title, '을 보셨군요!')

# uploader files1

# uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
# for uploaded_file in uploaded_files:
#     bytes_data = uploaded_file.read()
#     st.write("filename:", uploaded_file.name)
#     st.write(bytes_data)


# # uploader files2
import pandas as pd

# csv파일 불러오기
# uploaded_files1 = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
# for uploaded_file1 in uploaded_files1:
#     #bytes_data = uploaded_file.read()
#     data = pd.read_csv(uploaded_file1) # data = pd.read_csv(uploaded_file1, encoding="utf-8 / euc-kr / cp949")
#     st.write("filename:", uploaded_file1.name)
#     st.write(data)

# 파워포인트 파일 불러오기
uploaded_files1 = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file1 in uploaded_files1:
    #bytes_data = uploaded_file.read()
    data = pd.read_csv(uploaded_file1) # data = pd.read_csv(uploaded_file1, encoding="utf-8 / euc-kr / cp949")
    st.write("filename:", uploaded_file1.name)
    st.write(data)
