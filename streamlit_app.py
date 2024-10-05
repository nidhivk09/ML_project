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
  bill_depth_mm=st.slider('Bill dept (mm)',13.1,21.5,17.2)
  flipper_length_mm=st.slider('Flipper length (mm)',172.0,231.0,201.0)
  body_mass_g=st.slider('Body mass (g) ',2700.0,6300.0,4207.0)

# create dataframe for input features

 data={'island':island,'bill_length_mm':bill_length_mm,'gender':gender,'bill_depth_mm':bill_depth_mm, 'flipper_length_mm':flipper_length_mm,'body_mass_g':body_mass_g}

input_df=pd.DataFrame(data,index=[0])
input_penguins=pd.concat([input_df,X],axis=0)

input_penguins
                              
                                
