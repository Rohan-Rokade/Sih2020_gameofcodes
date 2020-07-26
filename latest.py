import streamlit as st
import pandas as pd
import numpy as np
from random import choice as c
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import plotly.express as px




def load_data():
    df1 = pd.read_csv("C:\\Users\\hp\\Desktop\\January2020_MySpeed.csv")

    df1['signal_strength']=pd.to_numeric(df1['signal_strength'],errors='coerce')
    df1.dropna(inplace=True,axis=0)
    df1.drop(['Data_Speed(Kbps)'],axis=1,inplace=True)
    df1.drop(['Download_Upload'],axis=1,inplace=True)
    df1.rename(columns = {'Service_Area':'State'}, inplace = True) 

    df1['State'].replace('Chennai','Tamil Nadu',inplace=True)
    df1['State'].replace('Kolkata','West Bengal',inplace=True)
    df1['State'].replace('Mumbai','Maharashtra',inplace=True)
    df1['State'].replace('North East','Arunachal Pradesh',inplace=True)
    df1['State'].replace('UP East','UP',inplace=True)
    df1['State'].replace('UP West','UP',inplace=True)


    def calculate_city(state):
        City='XYZ'
        if(state=='Andhra Pradesh'):
            L1=['visakhapatnam','vijayawada','guntur','nellore','kurnool']
            City=c(L1)
        if(state=='Assam'):
            L2=['guwahati','silchar','dibrugarh','jorhat','nagaon']
            City=c(L2)
        if(state=='Bihar'):
            L3=['patna','gaya','bhagalpur','muzzafarpur','purnia']
            City=c(L3)
        if(state=='Delhi'):
            City='delhi'
        if(state=='Gujarat'):
            L4=['ahmedabad','surat','vadodara','rajkot','bhavnagar']
            City=c(L4)
        if(state=='Haryana'):
            L5=['faridabad','gurugram','panipat','ambala','yamunanagar']
            City=c(L5)
        if(state=='Jammu & Kashmir'):
            L6=['srinagar','jammu','anantnag','udhampur','baramula']
            City=c(L6)
        if(state=='Himachal Pradesh'):
            L7=['shimla','solan','dharamsala','baddi','nahan']
            City=c(L7)
        if(state=='Karnataka'):
            L8=['bengaluru','mysuru','hubli-dharwad','kalaburagi','mangaluru']
            City=c(L8)
        if(state=='Kerala'):
            L9=['kochi','trivandrum','kozhikode','kollam','thrissur']
            City=c(L9)
        if(state=='Madhya Pradesh'):
            L10=['indore','bhopal','jabalpur','gwalior','ujjain']
            City=c(L10)
        if(state=='Maharashtra'):
            L11=['mumbai','pune','nagpur','aurangabad','nanded']
            City=c(L11)
        if(state=='Arunachal Pradesh'):
            L12=['changlang','dibang','kameng','siang','kumey']
            City=c(L12)
        if(state=='Orissa'):
            L13=['bhubaneswar','cuttack','rourkela','brahmapur','puri']
            City=c(L13)
        if(state=='Punjab'):
            L14=['lahore','faisalabad','rawalpindi','ludhiana','amritsar']
            City=c(L14)
        if(state=='Rajasthan'):
            L15=['jaipur','jodhpur','kota','bikaner','ajmer']
            City=c(L15)
        if(state=='Tamil Nadu'):
            L16=['Chennai','coimbatore','madurai','tiruppur','salem']
            City=c(L16)
        if(state=='UP'):
            L17=['kanpur','lucknow','agra','meerut','varanasi']
            City=c(L17)
        if(state=='West Bengal'):
            L18=['kolkata','bankura','hugli','nadia','haora']
            City=c(L18)
        return City
    df1['City']=df1['State'].apply(calculate_city)


    def calculate_rating(signal_strength):
        rating=0
        if signal_strength>=-70 :
            rating=5.0
        elif ((signal_strength <-70) and (signal_strength>= -85)) :
            rating=4.0
        elif ((signal_strength<-85) and (signal_strength>= -100)) :
            rating=3.0
        elif ((signal_strength<-100) and (signal_strength >= -110)) :
            rating=2.0
        elif(signal_strength <-110):
            rating=1.0
        return rating

    df1['rating']=df1['signal_strength'].apply(calculate_rating)
    
    return df1

data=load_data()


st.header("Exploratory Data Analysis Report")
if st.checkbox("Generate Data Profiling"):
    profile=ProfileReport(data)
    st_profile_report(profile)


st.header("Visualization of data acrcross all over India")
st.markdown(
    f'<div style="color: purple ; font-size: medium">{"Treemap charts visualize hierarchical data using nested rectangles.The hierarchy is defined by labels  and parents attributes. Click on one sector to zoom in/out, which also displays a pathbar in the upper-left corner of your treemap. To zoom out you can use the path bar as well."}</div>',
    unsafe_allow_html=True)
if st.checkbox("Show/Hide  Hierarchial Clustering."):
    with st.spinner('Wait for it...'):
        data['country']='India'
        fig = px.treemap(data, path=['country','State','City'])
        st.plotly_chart(fig)


st.header("Analysis and Visualization At State Level")
if st.checkbox("Show/Hide  Analysis and Visualization At State Level",value=False):

    state_arr=data.State.unique()
    emp_arr=['']
    state_menu=np.append(emp_arr,state_arr)
    
    state_selected = st.selectbox('Select one State:',state_menu, format_func=lambda u: 'Select an option' if u == '' else u)
    if state_selected:
        x1=state_selected
        st.success("You selected a state")
        st.subheader("Select the methodlogy for visualization")

        visl_arr=['Signal Strength','Service Provider']
        visl_ch = st.radio("select an option",visl_arr)

        if visl_ch == 'Service Provider':
            with st.spinner('Wait for it...'):
                dt1= data.loc[data.State== x1]
                fig1 = px.pie(dt1, names='Service_provider', title='  Visualize on basis of Service Provider(At State level)')
                fig1.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig1)

        else:
            with st.spinner('Wait for it...'):
                dt2= data.loc[data.State== x1].groupby('signal_strength').count()
                fig2=px.bar(dt2,y='Service_provider',text='Service_provider',labels={'Service_provider':'No of observations'},opacity=1,title='Visualize on Basis of Signal strength(At State Level)')
                fig2.update_traces(texttemplate='%{text:.1s}',textposition='outside')
                fig2.update_layout(uniformtext_minsize=5, uniformtext_mode='show')
                st.plotly_chart(fig2)

    else:
        st.warning('No option selected')


st.header("Analysis and Visualization At City Level")
if st.checkbox("Show/Hide  Analysis and Visualization At City Level",value=False):
    city1_arr=data['City'].unique()
    city1_selected = st.selectbox('Select a city (or there will be random city by default)',city1_arr)
    xz=city1_selected
    
    visl1_arr=['Signal Strength(city level)','Service Provider(city level)']
    visl1_ch = st.radio("select an option",visl1_arr)

    if visl1_ch == 'Service Provider(city level)':
        with st.spinner('Wait for it...'):
            dt5= data.loc[data.City== xz]
            fig5 = px.pie(dt5, names='Service_provider', title='  Visualize on basis of Service Provider(At State level)')
            fig5.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig5)

    else:
        with st.spinner('Wait for it...'):
            dt6= data.loc[data.City== xz].groupby('signal_strength').count()
            fig6=px.bar(dt6,y='Service_provider',text='Service_provider',labels={'Service_provider':'No of observations'},opacity=1,title='Visualize on Basis of Signal strength(At State Level)')
            fig6.update_traces(texttemplate='%{text:.1s}',textposition='outside')
            fig6.update_layout(uniformtext_minsize=5, uniformtext_mode='show')
            st.plotly_chart(fig6)