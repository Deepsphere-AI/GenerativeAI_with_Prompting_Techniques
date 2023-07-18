import streamlit as st
import pandas as pd
from source.ready_to_response import ready_response

def content_Creation(vAR_input_model,col1,col2):
    # w1,col1,col2,w2=st.columns((2,5.5,5.5,.5))
    with col1:
        st.write('# ')
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Prompt Functionality</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_Category_Learning = ['Select','Essay','Headlines','Articles','Recipe','Video Script','Blog Post']
        vAR_input = st.selectbox('',vAR_Category_Learning)
    
    if vAR_input == 'Essay':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('''"Discuss the impact of social media on modern society and its influence on interpersonal communication.''')
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Headlines':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Breaking News: Scientists Discover New Treatment for Cancer with Remarkable Success Rates")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Articles':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('Explore the history and cultural significance of street art in urban environments')
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Recipe':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("How to make a recipe for homemade chocolate chip cookies that will satisfy your sweet tooth in no time.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Video Script':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Give me a video script for my youtube channel")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Blog Post':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("In this post, I'll share My personal journey of self-discovery and the lessons I've learned along the way. Join me as we delve into the importance of embracing authenticity and finding true happiness.")
        ready_response(vAR_input_model)