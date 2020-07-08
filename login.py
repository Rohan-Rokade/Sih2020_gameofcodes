import streamlit as st
import sqlite3


conn=sqlite3.connect('data.db')
c=conn.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT,password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username,password) VALUES(?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM usertable WHERE username=? AND password=? ',(username,password))
    data=c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM usertable')
    data=c.fetchall()
    return data

def main():
    menu=["Home ","login"]
    choice=st.sidebar.selectbox("Menu",menu,index=0)

    if choice =="Home":
        st.subheader("Home")

    elif choice=="login":
        st.subheader("login section")

        username=st.sidebar.text_input("User Name")
        password=st.sidebar.text_input("Password",type="password")
        
        if st.sidebar.checkbox("Login"):
            
            create_usertable()
            result=login_user(username,password)

            if result:
                
                st.success("Logged in as {}".format(username))

                task=["Analytics","Profiles","engineer"]
                st.selectbox("Task",task)

                if task == "engineer":
                    st.subheader("Engineer")

                elif task=="Analytics":
                    st.subheader("Analytics")

                elif task == "Profiles":
                    st.subheader("Profiles")
            else :
                st.warning("Incorrect username/Password")
        
       

        


if __name__== '__main__':
    main()
        
