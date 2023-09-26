import streamlit as st
from source.model import *
# from source.gpt_API import generate_response3,generate_response3_5,generate_response4

def ready_response(vAR_input_model):
    w11,col11,col22,w22=st.columns((0.6,3.9,5.9,0.2))
    cc2,cc1,cc3=st.columns((1,6,0.8))
    with col11:
        st.write('### ')
        st.write('## ')
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Start Interaction with the Model ‎ ‎ ‎ ‎ ‎ (User Prompt)</span></p>", unsafe_allow_html=True)
    with col22:
        vAR_para_input = st.text_area('')
        prompt = vAR_para_input
        if vAR_para_input != "":
            st.write(" ")
            if st.button("Sumbit"):
                if vAR_input_model =='GPT-3':
                    respone = generate_response3(prompt)
                if vAR_input_model =='GPT-3.5':
                    respone = generate_response3_5(prompt)
                if vAR_input_model =='GPT-4':
                    respone = generate_response4(prompt)    
                with cc1:
                    st.write("# ")
                    st.success(respone)