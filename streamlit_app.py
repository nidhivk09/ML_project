import streamlit as st
import pandas as pd

st.title('Machine Learning App')
st.info('This is a machine learning app.')

with st.expander('Data'):
  st.write('**Raw data**')
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  X=df.drop('species',axis=1)
  X
  
  
  st.write('**Y**')
  Y=df.species
  Y


with st.expander('Data visualization'):
  #"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')


with st.sidebar:
  st.header('Input Features')
  island=st.selectbox('Island',('Boscoe','Dream','Torgersen'))
  gender=st.selectbox('Gender',('male','female'))
  bill_length_mm=st.slider('Bill length (mm)',32.1,59.6,43.9)
                                
