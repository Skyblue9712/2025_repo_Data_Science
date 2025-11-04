import streamlit as st
st.title("My Streamlit App")
st.subheader('My first web app using python')
st.text('this is some simple text')

# st.text_input('enter your name', placeholder='type here', value='default name')
#st.text_area('enter your address')
#st.number_input('enter your age', min_value=1, max_value=100, step=1)
#st.date_input('enter your dob') 

c1,c2=st.columns(2)

b=c1.number_input('Enter First number')
d=c2.number_input('Enter Second number')  


operations=['Add','Subtract','Multiply','Divide']
choice = st.radio('Select Operation', options=operations)

submit_btn=st.button('Calculate')

result= 0

if choice=='Add' and submit_btn:
    result=b+d
    st.success(f'The sum is {result}')
elif choice=='Subtract' and submit_btn:
    result=b-d
    st.success(f'The difference is {result}')
elif choice=='Multiply' and submit_btn:
    result=b*d
    st.success(f'The product is {result}')
elif choice=='Divide' and submit_btn:
    if d!=0:
        result=b/d
        st.success(f'The quotient is {result}')
    else:
        st.error('Division by zero is not allowed')     

# st.markdown(f' 
#             ### result : {result}
#            ')

st.success(f'Result Calculated: {result}')
st.balloons()
st.snow()
st.toast('Calculation Complete!')
st.header('Thank you for using the calculator app!')    