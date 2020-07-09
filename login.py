import streamlit as st
import sqlite3
import plotly.express as px


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

        vendors = ["A", "B", "C", "D", None, "E", "F", "G", "H", None]
        sectors = ["Tech", "Tech", "Finance", "Finance", "Other",
           "Tech", "Tech", "Finance", "Finance", "Other"]
        regions = ["North", "North", "North", "North", "North",
           "South", "South", "South", "South", "South"]
        sales = [1, 3, 2, 4, 1, 2, 2, 1, 4, 1]
        df = pd.DataFrame(dict(vendors=vendors, sectors=sectors, regions=regions, sales=sales))
        df["all"] = "all" # in order to have a single root node
        print(df)
        fig = px.treemap(df, path=['all', 'regions', 'sectors', 'vendors'], values='sales')
        st.plotly_chart(fig)

         

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
        
