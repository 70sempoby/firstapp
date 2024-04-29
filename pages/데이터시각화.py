import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# csv_file = st.file_uploader(label="파일을 업로드하세요. 단, CSV파일만 가능합니다.")
# if csv_file is not None :
#     csv_file_df = pd.read_csv(csv_file, encoding= "euc-kr")
#     st.write(csv_file_df.head())

# # chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# # st.write(chart_data)

# #st.write(csv_file_df['species'].value_counts())
# st.bar_chart(csv_file_df['species'].value_counts())
# #st.bar_chart(csv_file_df['island'].value_counts())

# fig, ax = plt.subplots()
# # ax.hist(csv_file_df['bill_length_mm'], bins=20)
# sns.histplot(csv_file_df['bill_length_mm'], binrange=[30,60], binwidth=2.5)
# st.pyplot(fig)

# 입력한 데이터 파일의 특정 열에 대해 그래프 그리기
csv_file = st.file_uploader(label="데이터 파일을 업로드하세요. 단, CSV파일만 가능합니다.")

if csv_file is not None :
    csv_file_df = pd.read_csv(csv_file, encoding= "euc-kr")
    st.write(csv_file_df.head())

    column = st.radio(label="열 이름을 선택해주세요.", options = csv_file_df.columns)
    st.subheader(column, "의 분포 시각화", divider='rainbow')
    st.bar_chart(csv_file_df[column].value_counts())

    fig, ax = plt.subplots()
    sns.histplot(csv_file_df[column], binrange=[2500, 7000], binwidth=100)
    st.pyplot(fig)
