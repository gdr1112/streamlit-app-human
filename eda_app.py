import streamlit as st
import utils
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
def load_data(path):
    # CSV 파일 가져올시
    df = pd.read_csv(path)
    
    # DB 에서 가져올 경우
    
    #크롤링해서 가져올 경우

    return df

def run_eda_app():
    st.subheader('탐색적 자료 분석')
    # with st.expander('데이터셋 정보'):
    #     st.markdown(utils.attrib_info)
    
    # 데이터셋 불러오기
    DATA_PATH = 'data/iris.csv'
    iris_df = load_data(DATA_PATH)
    # st.dataframe(iris_df)

    # 서브메뉴 지정
    submenu = st.sidebar.selectbox("서브메뉴", ['기술통계량', '그래프'])
    if submenu == '기술통계량':
        st.subheader('기술통계량')
        st.dataframe(iris_df)

        with st.expander('데이터타입'):
            df2 = pd.DataFrame(iris_df.dtypes).transpose()
            df2.index = ['구분']
            st.dataframe(df2)
        
        with st.expander('기술 통계량'):
            st.dataframe(pd.DataFrame(iris_df.describe()).transpose())
        
        st.write('타겟 분포')
        st.dataframe(iris_df['species'].value_counts())
    elif submenu == '그래프':
        st.subheader('그래프')

        # with st.expander('산점도'):
        #     # plotly 그래프
        #     fig1= px.scatter(iris_df,
        #         x = 'sepal_width',
        #         y = 'sepal_length',
        #         color= 'species',
        #         size = 'petal_width',
        #         hover_data=['petal_length'],
        #         title= 'IRIS 산점도')
        #     st.plotly_chart(fig1)
        
        # layouts
        # col1 , col2 = st.columns(2)
        # with col1:
        #     st.subheader('col1')
        #     # seaborn 그래프
        #     fig, ax = plt.subplots()
        #     sns.boxplot(iris_df, x = 'species', y = 'sepal_length', ax=ax)
        #     st.pyplot(fig)
        # with col2:
        #     st.subheader('col2')
        #     # 히스토그램 (Matplotlib)
        #     fig, ax = plt.subplots()
        #     ax.hist(iris_df['sepal_length'], color='green')
        #     st.pyplot(fig)
        # Tabs
        tab1 , tab2 , tab3, tab4, tab5= st.tabs(['전체 산점도', '산점도', '박스 플롯', '히스토그램', '막대그래프'])
        with tab1:
            fig1= px.scatter(iris_df,
                x = 'sepal_width',
                y = 'sepal_length',
                color= 'species',
                size = 'petal_width',
                hover_data=['petal_length'],
                title= 'IRIS 산점도')
            st.plotly_chart(fig1)
            st.success('Iris 데이터 전체를 산점도로 확인할 수 있다.')
        with tab2:
            val_species = st.selectbox('종 선택', ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica', ))
            st.write(val_species)

            result = iris_df[iris_df['species'] == val_species]
            # st.dataframe(result)

            fig1 = px.scatter(result , x ='sepal_width', y = 'sepal_length', size= 'petal_width')
            st.plotly_chart(fig1)
            st.success('Setosa, Versicolor, Virginica 중 하나를 선택해 산점도로 확인 할 수 있다.')
        with tab3:
            fig, ax = plt.subplots()
            sns.boxplot(iris_df, x = 'species', y = 'sepal_length', ax=ax)
            st.pyplot(fig)
            st.success('Iris 데이터를 박스 플롯으로 나타낸 것으로 x축은 종, y축은 꽃받침의 길이를 확인할 수 있다.')
        
        with tab4:
            fig, ax = plt.subplots()
            ax.hist(iris_df['petal_length'], color='green')
            st.pyplot(fig)
            st.success('히스토그램으로 데이터를 나타낸 것으로, x축은 꽃잎의 길이, y축은 전체데이터중 꽃잎의 길이의 갯수를 확인할 수 있다.')
        with tab5:
            
            fig, ax = plt.subplots()
            
            sns.barplot(iris_df, x= 'sepal_length', y='sepal_width', ax=ax, orient='h' )
            st.pyplot(fig)
            st.success('Iris 데이터 전체를 막대그래프로 나타낸 것으로, x축은 꽃받침의 너비, y축은 꽃받침의 길이를 확인할 수 있다. ')
    else:
        pass


### 상단 html 코드 수정 (강사님 주실 예정)
## 