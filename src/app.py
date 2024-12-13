import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy  as np 
import sklearn
from PIL import Image
import streamlit as st
import pickle
 


model=pickle.load(open("../models/saved/model.pkl","rb"))



st.title('House Price Prediction')
st.sidebar.header('House Data')
image = Image.open('../data/download.jpg')
st.image(image, '')

# FUNCTION
def House_report():
    # House-specific inputs
    Square_Feet = st.number_input('Square Feet',min_value=0) 
    Num_Bedrooms = st.number_input('Number of Bedrooms',min_value=0, step=1) 
    Num_Bathrooms = st.number_input('Number of Bathrooms',min_value=0, step=1)  
    Num_Floors = st.number_input('Number of Floors',min_value=0, step=1)  
    Year_Built = st.number_input('Year Built',min_value=0, step=1)   
    has_Garden = st.selectbox("Does the house have a  Gareden",["Yes", "No"])
    if has_Garden == "Yes":
        Has_Garden = 1
    else:
        Has_Garden = 0 
    has_pool = st.selectbox("Does the house have a pool?",["Yes", "No"])
    if has_pool == "Yes":
        Has_Pool = 1
    else:
        Has_Pool = 0
    Garage_Size = st.number_input('Garage Size',min_value=0) 
    Location_Score = st.number_input('Location Score',min_value=0)  
    Distance_to_Center = st.number_input('Distance to Center (in km)',min_value=0)  


    Hous_report_data = {
      'Square_Feet':Square_Feet,
      'Num_Bedrooms': Num_Bedrooms,
      'Num_Bathrooms':Num_Bathrooms,
      'Num_Floors':Num_Floors,
      'Year_Built':Year_Built,
      'Has_Garden':Has_Garden,
      'Has_Pool': Has_Pool,
      'Garage_Size':Garage_Size,
      "Location_Score": Location_Score,
      "Distance_to_Center": Distance_to_Center

  }
    data = pd.DataFrame(Hous_report_data, index=[0])
    return data

House_data = House_report()
st.header('House Data')
st.write(House_data)

price = model.predict(House_data)
st.subheader('House Price')
st.subheader('$'+str(np.round(price[0], 2)))
