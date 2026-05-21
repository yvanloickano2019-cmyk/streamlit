import streamlit as st
st.header('welcome to the BMI calculator')

weight = st.number_input('Enter your weight in kg')
status = st.radio("Select your height unit", ("cms", "meters", "feet"))

try:
    if status == "cms":
        height = st.number_input("centimeters")
        bmi = weight / (height/100)**2
    elif status == "meters":
        height = st.number_input("meters")
        bmi = weight / height**2
    else:
        height = st.number_input("feet")
        bmi = weight / ((height/3.2808)**2)
except:
    bmi = 0

if st.button("Calculate BMI"):
    st.write("Your BMI index is {}.".format(round(bmi)))

    if bmi < 16:
        st.error('You are extremely underweight')
    elif (bmi >= 16) and (bmi < 18.5):
        st.warning('You are underweight')
    elif (bmi >= 18.5) and (bmi < 25):
        st.success("healthy")
        st.balloons()
    elif (bmi >= 25) and (bmi < 30):
        st.warning('You are overweight')
    else:
        st.error("extremely overweight")
