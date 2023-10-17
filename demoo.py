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












# Add a selectbox to the sidebar:
#st.sidebar.selectbox('How would you like to be contacted?',('Email', 'Home phone','Mobile phone'))

# Add a slider to the sidebar:
#st.sidebar.slider('Select a range of values',0.0, 100.0, (25.0, 75.0))