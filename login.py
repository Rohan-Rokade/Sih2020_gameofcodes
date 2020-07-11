import streamlit as st
import pandas as pd
import numpy as np
from random import choice as c
import matplotlib.pyplot as plt 
import plotly.express as px
import time 


st.title("Visualization Of Poor Cellular connectiviy and Analyze Reports")
st.header("hello rohan :sunglasses:")

@st.cache
def load_data():
    dataset = pd.read_csv("https://raw.githubusercontent.com/Rohan-Rokade/networkdetector/master/sihdata.csv")
    dataset['city']='all'
    dataset['LSA'].replace('Chennai','Tamil Nadu',inplace=True)
    dataset['LSA'].replace('Kolkata','West Bengal',inplace=True)
    dataset['LSA'].replace('Mumbai','Maharashtra',inplace=True)
    dataset['LSA'].replace('North East','Arunachal Pradesh',inplace=True)
    dataset['LSA'].replace('UP East','UP',inplace=True)
    dataset['LSA'].replace('UP West','UP',inplace=True)


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
            city=c(L17)
        if(LSA=='West Bengal'):
            L18=['kolkata','bankura','hugli','nadia','haora']
            City=c(L18)
        return City
    dataset['city']=dataset['LSA'].apply(calculate_city)
    return dataset
dt=load_data()
st.table(dt.head())


state_menu=dt['LSA'].unique()
if st.checkbox("Filter by state and city analyze",value=False):
    st.write(state_menu)
    #options = list(range(len(state_menu)))
    #state_option = st.selectbox('select state',options,format_func=lambda x:state_menu[x])
    state_option = st.selectbox('Select  the state',state_menu)
    x=state_option
    dataset1=dt.loc[dt['LSA']==x]
    st.write('You selected :',x)
    st.table(dataset1.describe())
    city_menu=dataset1['city'].unique()
    if st.checkbox("city analyze",value=False):
        st.write(city_menu)
        city_option=st.selectbox('select the city',city_menu)
        y=city_option
        st.write("You Selected:",y)
        dataset2=dataset1.loc[dt['city']==y]
        st.table(dataset2.describe())

        st.subheader("Bar chart Analysis:")
        plt.hist(dataset2.Service_Provider)
        st.pyplot()

        data_canada = dataset2[dataset2['Service_Provider']== 'JIO']
        fig1 = px.bar(data_canada,'Signal_strength')
        st.plotly_chart(fig1)

if st.checkbox(" Maps using  deck gl library"):
        data = pd.DataFrame({
            'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
            'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
            'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
        })
        # Adding code so we can have map default to the center of the data
        midpoint = (np.average(data['lat']), np.average(data['lon']))

        st.deck_gl_chart(
                    viewport={
                        'latitude': midpoint[0],
                        'longitude':  midpoint[1],
                        'zoom': 4
                    },
                    layers=[{
                       'id': "scat-blue",
                 'type': 'ScatterplotLayer',
                 'data': data.iloc[:25],
                 'opacity': 1,
                 'getColor': [75,205,250],
                 'pickable': True,
                 'autoHighlight': True,
                 'getRadius': 200,
                 'radiusMinPixels': 5,
                  },{
                 'id': 'scat-red',
                 'type': 'ScatterplotLayer',
                 'data': data.iloc[25:50],
                 'opacity': 1,
                 'getColor': [255,94,87],
                 'autoHighlight': True,
                 'pickable': True,
                 'getRadius': 200,
                 'radiusMinPixels': 5,
                    }]
                )

if st.checkbox("Display of map using streamlit in-built map method st.map()"):
    st.write("Pretending Maps take some expensive time ,set time delay to 15 secs,once loaded it will diplay done message.")
    with st.spinner('Wait for it...'):
        
        df = pd.DataFrame(np.random.randn(10000, 2) / [50, 50] + [19.0760,72.877],columns=['lat', 'lon'])
        time.sleep(15)
        st.map(df)
    st.success('Done!')

if st.checkbox("Displaying of Tree Plot"):
    st.write("Downloadable img in png format ,can also maximixe image.")
    states=['mh','up','hp','bihar','up','up','bihar','mh','mh','mh','mh','mh','bihar','up']
    cities= ["nanded","lucknow","shimla","patna","agra","lucknow","nalanda","mumbai","pune","pune","mumbai","mumbai","patna","lucknow"]
    #regions = ["North", "North", "North", "North", "North","South", "South", "South", "South", "South"]
    counting = [100,300,400,150,50,200,350,260,450,300,600,200,540,240]
    df = pd.DataFrame(dict(states=states,cities=cities,counting=counting))
    df["country"] = "India" # in order to have a single root node
    print(df)
    fig = px.treemap(df, path=['country', 'states', 'cities'], values='counting')
    st.plotly_chart(fig)





    



