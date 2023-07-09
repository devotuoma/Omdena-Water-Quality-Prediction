import base64
import numpy as np
import streamlit as st
from Omdena_Rwanda_Water_model import predict

with open("C:/Users/Akunna Anyamkpa/Omdena_Rwanda_Water.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.experimental_memo
def image(file):
    with open(file, "rb") as f:
        data = f.read() 
    return base64.b64encode(data).decode()

pics = image("blue.jpg")

page_image = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{pics}");
background-size: 200%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>
""" 

st.markdown(page_image, unsafe_allow_html=True)

st.sidebar.header("PREDICTION DASHBOARD")

with st.container():
    st.title('OMDENA WATER QUALITY PREDICTION PROJECT')

    st.markdown(
    "WELCOME TO THIS APPLICATION DESIGNED TO FORECAST WATER POTABILITY USING PROVIDED INPUTS")

st.write('---')

# Colour (TCU)
Colour = st.text_input("Colour (TCU)", " ")

# Turbidity (NTU)
Turbidity = st.text_input("Turbidity (NTU)", " ")
 
# pH
pH = st.text_input("pH", " ")

# Conductivity (uS/cm)
Conductivity = st.text_input("Conductivity (uS/cm)", " ")
  
# Total Dissolved Solids (mg/l)
TotalDissolvedSolids = st.text_input("Total Dissolved Solids (mg/l)", " ")

# Total Hardness (mg/l as CaCO3)
TotalHardness = st.text_input("Total Hardness (mg/l as CaCO3)", " ")

# Aluminium (mg/l)
Aluminium = st.text_input("Aluminium (mg/l)", " ")

# Chloride (mg/l)
Chloride = st.text_input("Chloride (mg/l)", " ")

# Total Iron (mg/l)
TotalIron = st.text_input("Total Iron (mg/l)", " ")

# Sodium (mg/l)
Sodium = st.text_input("Sodium (mg/l)", " ")

# Sulphate (mg/l)
Sulphate = st.text_input("Sulphate (mg/l)", " ")

# Zinc (mg/l)
Zinc = st.text_input("Zinc (mg/l)", " ")

# Magnesium (mg/l)
Magnesium = st.text_input("Magnesium (mg/l)", " ")

# Calcium (mg/l)
Calcium = st.text_input("Calcium (mg/l)", " ")

# Potassium (mg/l)
Potassium = st.text_input("Potassium (mg/l)", " ")

# Nitrate (mg/l)
Nitrate = st.text_input("Nitrate (mg/l)", " ")

# Phosphate (mg/l)
Phosphate = st.text_input("Phosphate (mg/l)", " ")


if st.button('Check Status'):
    
    cost = predict(np.array([[Colour, Turbidity, pH, Conductivity, TotalDissolvedSolids, TotalHardness, Aluminium, Chloride, TotalIron, Sodium, Sulphate, Zinc, Magnesium, Calcium, Potassium, Nitrate, Phosphate]])) 

    val = cost[0]
    
    if val == 0:
        st.text("Water is Potable")
        st.text(val)
    else:
        st.text("Water is Not Potable") 
        st.text(val)