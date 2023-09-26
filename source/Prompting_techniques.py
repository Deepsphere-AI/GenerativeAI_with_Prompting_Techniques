import streamlit as st
import pandas as pd
from source.ready_to_response import ready_response

def Prompt_technique(vAR_input_model,col1,col2):
    # w1,col1,col2,w2=st.columns((2,5.5,5.5,.5))
    with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Prompt Functionality</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_Category_Learning = ['Select','Defining Roles','Temperature','Provide Examples','Mode']
        vAR_input = st.selectbox('',vAR_Category_Learning)
    
    if vAR_input == 'Defining Roles':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('Imagine yourself as an adventurous space traveller who falls on a mysterious alien world. Tell about your interactions with extraterrestrial beings and reveal the secrets of this fascinating realm.')
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Temperature':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('Talk about how climate change is affecting marine ecosystems, emphasising the difficulties facing marine biodiversity and the steps being taken to counteract these consequences. Give a comprehensive explanation using 0.6 temperature.')
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Provide Examples':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('Generate choose the best answers with only two options. Example: In which direction the sun rises a) East b) West Answer: East')
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Mode':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('Please present a strong argument in paragraphs that explains the advantages of renewable energy.')
        ready_response(vAR_input_model)