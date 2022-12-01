import streamlit as st

def run_about_app():
    st.subheader('About')
    submenu = st.sidebar.selectbox("서브메뉴", ['참조 사이트', '나의 GitHub'])
    if submenu == '참조 사이트':
        
        st.markdown('### 참조 사이트')
        st.markdown('#### 더 북 : https://thebook.io/006723/ch04/01/')
        st.markdown('#### Streamlit Documentation : https://docs.streamlit.io/library/api-reference/widgets/st.selectbox')
    
    elif submenu == '나의 GitHub':
        
        st.markdown('## 나의 Github : https://github.com/gdr1112/human-22.08-23.02')