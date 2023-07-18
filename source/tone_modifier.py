import streamlit as st
import pandas as pd
from source.ready_to_response import ready_response

def Tone_Modifier(vAR_input_model,col1,col2):
    # w1,col1,col2,w2=st.columns((2,5.5,5.5,.5))
    with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Prompt Functionality</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_Category_Tonemodifier = ['Select','Friendly + professional','Authoritative + informative','Urgent + persuasive','Casual + conversational','Professional + trustworthy','Humorous + informal','Professional + straightforward','Serious + empathetic','Positive + enthusiastic','Authoritative + professional','Casual + funny','Authoritative + expert']

        vAR_input = st.selectbox('',vAR_Category_Tonemodifier)
    
    if vAR_input == 'Friendly + professional':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('You are a sales representative. You want to assist the customers in a friendly and professional way with few words.')
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Authoritative + informative':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('You are a leader in India. Tell us about a research in the authoritative and informative tone with few words.')
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Urgent + persuasive':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('You are a sales agent. You want to convince the customer to buy your product in an urgent and persuasive tone in few words.')
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Casual + conversational':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('You have won a trophy. You want to coney this message to your neighbors in a casual and conversational tone.')
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Professional + trustworthy':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('You want to play with your friends. How do you convince your parents in a professional and trustworthy tone. The content should be in a single paragraph.')
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Humorous + informal':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('There is a guard dog in our office. Tell about the dog in a humorous and informal tone in few words.')
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Professional + straightforward':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('You are conducting an interview. Ask the candidate whether he has any question regarding the company in a professional and straightforward tone.')
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Serious + empathetic':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('Your friend lost some money in gambling. Tell us how you will help your friend in his financial crisis in serious and empathetic tone in few words.')
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Positive + enthusiastic':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('You are a product owner. Tell us about your products in a positive and enthusiastic tone in few words.')
        ready_response(vAR_input_model)

    elif vAR_input == 'Authoritative + professional':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('You are a leader. Tell us your commitments in an authoritative and professional tone in few words.')
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Casual + funny':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('You are Comedian. Tell me a joke in casual and funny tone.')
        ready_response(vAR_input_model)

    elif vAR_input == 'Authoritative + expert':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('You are an expert  in IT. Explain the current challenges and opportunities in an authoritative and expert tone with few words.')
        ready_response(vAR_input_model)