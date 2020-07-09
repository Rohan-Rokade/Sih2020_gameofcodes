import streamlit as st
import pandas as pd
import plotly.express as px

st.subheader("Home")

vendors = ["A", "B", "C", "D", None, "E", "F", "G", "H", None]
sectors = ["Tech", "Tech", "Finance", "Finance", "Other", "Tech", "Tech", "Finance", "Finance", "Other"]
regions = ["North", "North", "North", "North", "North", "South", "South", "South", "South", "South"]
sales = [1, 3, 2, 4, 1, 2, 2, 1, 4, 1]
df = pd.DataFrame(dict(vendors=vendors, sectors=sectors, regions=regions, sales=sales))
df["all"] = "all" # in order to have a single root node
print(df)
fig = px.treemap(df, path=['all', 'regions', 'sectors', 'vendors'], values='sales')
st.plotly_chart(fig)

                    
        



