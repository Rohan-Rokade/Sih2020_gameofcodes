import streamlit as st
import pandas as pd
import numpy as np
from random import choice as c
import matplotlib.pyplot as plt

dataset=pd.read_csv("https://github.com/Rohan-Rokade/networkdetector/blob/master/sihdata.csv")

st.title('NETWORK DETECTION')
st.write(dataset)

st.header("Plotting on Indian Map")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [19.07,72.87],
    columns=['lat', 'lon'])

st.map(map_data)

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
    



