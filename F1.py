import pandas as pd
import streamlit as st
from PIL import Image

data=pd.read_excel("F1.xlsx")
print(len(data["Constructor"]))
st.set_page_config(
    page_title="Formula 1 Analysis",
    page_icon="F1.png",
    layout="wide"
)
st.sidebar.success("2023 Constructors")
images=["Ferrari.png","RB.png","Mercs.png","Mclaren.png","alp.png","af.png","alphatauri.png","Williams.png"]
st.sidebar.image(images,width=150)
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    image1 = Image.open('F1.png')
    st.image(image1,width=200)

with col3:
    st.write(' ')

st.dataframe(data,width=100000)
# ---- MAINPAGE ----
st.title(" Constructors Championship")
st.markdown("###")
st.text("Note that before 1958 constructors data is not available but you will get drivers data in the drivers championship")

n = int(st.number_input("Enter your season",step=1,format="%d"))
st.subheader(data.iloc[n])
st.markdown("""---""")
data['Constructor'].value_counts()
my_constructors=[16,9,8,8,7,5,2,2,2,1,1,1,1,1]
print(len(my_constructors))
image = Image.open('Figure_1.png')
st.image(image, width=1000)
## Drivers
d_data=pd.read_excel("Drivers.xlsx")
print(len(d_data))
st.title("Drivers Championship")
st.dataframe(d_data,width=100000)
m = int(st.number_input("Enter your season",key="a",step=1,format="%d"))
data.convert_dtypes(convert_string=True)
st.subheader(d_data.iloc[m])
image = Image.open('Figure_2.png')
st.image(image)
