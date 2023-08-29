import joblib
import streamlit as st


model = joblib.load('modelk.sav')
names=['setosa','versicolor','verginica']





st.title("Predict iris type")

# Add sliders for input fields
sepal_length = st.slider("Sepal Length", float(8), float(5))
sepal_width = st.slider("Sepal Width", float(5), float(3))
petal_length = st.slider("Petal Length", float(7), float(2))
petal_width = st.slider("Petal Width", float(3), float(0.1))


button=st.button('Predict')

if(button):
    sepal_length_value=float(sepal_length)
    sepal_width_value=float(sepal_width)
    petal_length_value=float(petal_length)
    petal_width_value=float(petal_width)
    x=[[sepal_length_value,sepal_width_value,petal_length_value,petal_width_value]]
    predict=model.predict(x)
    st.text('{}'.format(names[predict[0]]))
    st.text('{}'.format(predict))
