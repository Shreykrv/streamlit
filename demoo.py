import streamlit as st

st.title('My First DataScience app')
st.header('My Dataset')
st.subheader('My Dataset')
st.button('Submit')
st.write('IRIS')
st.code('for x in a')


if st.checkbox('I accept all the terms and condition.'):
	st.write('thankyou')


st.selectbox('enter subject',['HTML','js','Python','java'])
#st.slidebox('I accept all the terms and condition.')


#a = st.file_uploader('Upload  your data')
#st.image(a)
st.number_input('select your marks',min_value=1,max_value=100)

st.radio('Please Select Day ',['sun','mon','tue','wed','thru','fri','SAT'])
st.color_picker('Red')





with st.chat_message('USER'):
	st.write('👍👍👍❤️❤️','Hello User')



import pandas as pd



#st.error('this looks cool')
#st.progress(10)
#st.progress(10) with st.spinner('loading...')
st.balloons()


st.snow()


#st.toast('Warming up...')
#st.error('Error message')
#st.warning('Warning message')
#st.info('Info message')
#st.success('Success message')
#st.exception(e)

#with st.echo():st.write('Code will be executed and printed')






#df.pd.read_csv('details.csv')
#st.title('My Intractive DA project')


#if st.checkbox('display data'):st.write(df)
#if st.button('display description'):st.table(df.describe())
#st.date_input('date of Birth')


#st.container()
#d = st.text_input('Entr ur name')
#st.write(d)
#st.number_input('pick',0,100)










import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


df = pd.read_csv("penguins.csv")
df1=df.drop(['Unnamed: 0'], axis=1)

st.title("My streamlit web app")
st.write("This is the raw dataset")
st.write(df1)
st.write("Data Description")
st.write(df1.describe())

st.write("Data Info")
st.write(df1.info())

st.write("Plot")
fig = plt.figure(figsize = (19, 10))

plt.bar(df['island'], df['bill_length_mm'], color='blue')

plt.xlabel('island')

plt.ylabel('bill_length_mm')

plt.title('Matplotlib Bar Chart ')

st.pyplot(fig)



st.write("Scatter Plot")
fig1 = plt.figure(figsize = (19, 10))

plt.scatter(df['island'], df['bill_length_mm'], color='c')

plt.xlabel('island')

plt.ylabel('bill_length_mm')

plt.title('Matplotlib Bar Chart ')

st.pyplot(fig1)



















# Add a selectbox to the sidebar:
#st.sidebar.selectbox('How would you like to be contacted?',('Email', 'Home phone','Mobile phone'))

# Add a slider to the sidebar:
#st.sidebar.slider('Select a range of values',0.0, 100.0, (25.0, 75.0))
