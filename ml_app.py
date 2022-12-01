import streamlit as st
import joblib
import os
import numpy as np
import utils


def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model


def run_ml_app():
    st.subheader("머신러닝")

    # st.markdown(utils.attrib_info)
    
    
    #lay out
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('입력값을 조정하세요')
        sepal_length = st.select_slider('Sepal Length', options=np.arange(1,11))
        sepal_width = st.select_slider('Sepal Width', options=np.arange(1,11))
        petal_length = st.select_slider('Petal Length', options=np.arange(1,11))
        petal_width = st.select_slider('Petal Width', options=np.arange(1,11))
        sample = [sepal_length, sepal_width, petal_length, petal_width]
        # st.write(sample)

    with col2:
        st.subheader('예측결과를 확인해 주세요')
        # st.write(sample)
        # 리스트를 2차원 배열로 만듬
        single_sample = np.array(sample).reshape(1, -1)
        # st.write(single_sample.shape)
        # st.write(single_sample)

        # 모델 불러오기
        model = load_model('models\logistic_regression_model_iris_221208.pkl')
        # st.write(model.classes_)
        prediction = model.predict(single_sample)
        pred_prob = model.predict_proba(single_sample)
        # st.write(prediction)
        # st.write(pred_prob)
        st.write(pred_prob)
        if prediction == 0:
            st.success('Setosa 종입니다.')
            st.write('Setosa 확률 :' , np.round(pred_prob[0][0]*100), "%")
            st.write('Versicolor 확률 :' , np.round(pred_prob[0][1]*100), "%")
            st.write('Virginica 확률 :' , np.round(pred_prob[0][2]*100), "%")
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Irissetosa1.jpg/220px-Irissetosa1.jpg')
        elif prediction == 1:
            st.success('Versicolor 종입니다.')
            st.success('Setosa 종입니다.')
            st.write('Setosa 확률 :' , np.round(pred_prob[0][0]*100), "%")
            st.write('Versicolor 확률 :' , np.round(pred_prob[0][1]*100), "%")
            st.write('Virginica 확률 :' , np.round(pred_prob[0][2]*100), "%")
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/220px-Blue_Flag%2C_Ottawa.jpg')
        elif prediction == 2:
            st.success('Virginica 종입니다')
            st.success('Setosa 종입니다.')
            st.write('Setosa 확률 :' , np.round(pred_prob[0][0]*100), "%")
            st.write('Versicolor 확률 :' , np.round(pred_prob[0][1]*100), "%")
            st.write('Virginica 확률 :' , np.round(pred_prob[0][2]*100), "%")
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/220px-Iris_virginica_2.jpg')
        else:
            pass