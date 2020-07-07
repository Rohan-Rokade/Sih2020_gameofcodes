import streamlit as st
import pandas as pd
import numpy as np
from random import choice as c
import matplotlib.pyplot as plt

data=pd.read_csv("https://github.com/Rohan-Rokade/networkdetector/blob/master/sihdata.csv",header=None,error_bad_lines=False)

st.title('NETWORK DETECTION')


st.header("Plotting on Indian Map")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [19.07,72.87],
    columns=['lat', 'lon'])

st.map(map_data)

data['LSA'].replace('Chennai','Tamil Nadu',inplace=True)
data['LSA'].replace('Kolkata','West Bengal',inplace=True)
data['LSA'].replace('Mumbai','Maharashtra',inplace=True)
data['LSA'].replace('North East','Arunachal Pradesh',inplace=True)
data['LSA'].replace('UP East','UP',inplace=True)
data['LSA'].replace('UP West','UP',inplace=True)


def calculate_city(LSA):
    City=''
    if(LSA=='Andhra Pradesh'):
        L1=['visakhapatnam','vijayawada','guntur','nellore','kurnool']
        City=c(L1)
    if(LSA=='Assam'):
        L2=['guwahati','silchar','dibrugarh','jorhat','nagaon']
        City=c(L2)
    if(LSA=='Bihar'):
        L3=['patna','gaya','bhagalpur','muzzafarpur','purnia']
        City=c(L3)
    if(LSA=='Delhi'):
        City='delhi'
    if(LSA=='Gujarat'):
        L4=['ahmedabad','surat','vadodara','rajkot','bhavnagar']
        City=c(L4)
    if(LSA=='Haryana'):
        L5=['faridabad','gurugram','panipat','ambala','yamunanagar']
        City=c(L5)
    if(LSA=='Jammu & Kashmir'):
        L6=['srinagar','jammu','anantnag','udhampur','baramula']
        City=c(L6)
    if(LSA=='Himachal Pradesh'):
        L7=['shimla','solan','dharamsala','baddi','nahan']
        City=c(L7)
    if(LSA=='Karnataka'):
        L8=['bengaluru','mysuru','hubli-dharwad','kalaburagi','mangaluru']
        City=c(L8)
    if(LSA=='kerala'):
        L9=['kochi','trivandrum','kozhikode','kollam','thrissur']
        City=c(L9)
    if(LSA=='Madhya Pradesh'):
        L10=['indore','bhopal','jabalpur','gwalior','ujjain']
        City=c(L10)
    if(LSA=='Maharashtra'):
        L11=['mumbai','pune','nagpur','aurangabad','nanded']
        City=c(L11)
    if(LSA=='Arunchal Pradesh'):
        L12=['changlang','dibang','kameng','siang','kumey']
        City=c(L12)
    if(LSA=='Orissa'):
        L13=['bhubaneswar','cuttack','rourkela','brahmapur','puri']
        City=c(L13)
    if(LSA=='Punjab'):
        L14=['lahore','faisalabad','rawalpindi','ludhiana','amritsar']
        City=c(L14)
    if(LSA=='Rajasthan'):
        L15=['jaipur','jodhpur','kota','bikaner','ajmer']
        City=c(L15)
    if(LSA=='Tamil Nadu'):
        L16=['Chennai','coimbatore','madurai','tiruppur','salem']
        City=c(L16)
    if(LSA=='UP'):
        L17=['kanpur','lucknow','agra','meerut','varanasi']
        City=c(L17)
    if(LSA=='West Bengal'):
        L18=['kolkata','bankura','hugli','nadia','haora']
        City=c(L18)
    return City
data['City']=data['LSA'].apply(calculate_city)





if st.checkbox('Show HISTOGRAM'):
    st.markdown("**_my First analysis reports_**",unsafe_allow_html=False)
    html_code="""<div style= "background-color:teals; padding:10px"><h2 style="color:red;text-align:center;">Analysis on basis of ISP</h2></div>"""

    st.markdown(html_code,unsafe_allow_html=True)
    plt.hist(dataset.Service_Provider)
    plt.show()
    st.pyplot()

lsa_l=dataset['LSA'].unique()



if st.checkbox('Statewise Analysis'):
    
    option = st.selectbox('Select  the state',lsa_l)
    x=option
    dataset2=dataset.loc[dataset['LSA']==x]
    st.write('You selected ',x)
    
    city_l=dataset2['Service_Provider'].unique()

    if st.checkbox("Service Provider"):
        
            option2=st.selectbox("Select ISP",city_l)
            st.write("selected",option2)
            y=option2
            
            dataset3=dataset2.loc[dataset['Service_Provider']==y]

            plt.hist(dataset3.City)
            plt.show()
            st.pyplot()
    



