import pyrebase
import streamlit as st

# Configuration Key
firebaseConfig = {

}

# Firebase authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()

st.title("SMS Spam Detection")
st.header("\n")
st.image("SMS-Spam.jpg",width=500)
st.sidebar.title("Login")

# Authentication
email = st.sidebar.text_input("Enter your email")
password = st.sidebar.text_input("Enter your password",type="password")
choice = st.sidebar.selectbox('Login/Signup',['Login','Sign up'])

if choice == 'Sign up':
  username = st.sidebar.text_input('Enter your username')
  submit = st.sidebar.button("Create account")

  if submit:
    user = auth.create_user_with_email_and_password(email, password)
    st.success('Your account is created successfully!')
    st.balloons()

    # Sign in
    user = auth.sign_in_with_email_and_password(email, password)
    db.child(user['localId']).child("Username").set(username)
    db.child(user['localId']).child("Id").set(user['localId'])
    st.title("Welcome "+username)
    st.info("Login via the dropdown box")

elif choice == 'Login':
  sub = st.sidebar.button("Login")

  if sub:
      try:
        user = auth.sign_in_with_email_and_password(email, password)
        st.success('Login Successfull!')
        html_string = "<a href=https://sms-spam-detection-nextgen.herokuapp.com/>Open app</a>"
        st.markdown(html_string, unsafe_allow_html=True)
      except:
        st.success("Invalid credentials")
