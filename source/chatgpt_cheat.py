import streamlit as st
from source.Art_of_prompt import How_to_prompt
from source.Content_Creation import content_Creation
from source.Knowledge import learn
from source.writing_formats import writing
from source.jailbreak import jail_breake
from source.Prompting_techniques import Prompt_technique
from source.tone_modifier import Tone_Modifier
from source.Playing_role import role_playing

def Chatgpt_Cheat(col1,col2):
    # w1,col1,col2,w2=st.columns((1.5,3.5,3.5,0.3))
    # cc2,cc1,cc3=st.columns((2,8,0.2))
    with col1:
        st.markdown("### ")
        # st.write('# ')
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Model</span></p>", unsafe_allow_html=True)
    with col2:
        # st.markdown("## ")
        vAR_Model = ['GPT-3','GPT-3.5','GPT-4']
        vAR_input_model = st.radio(' ',vAR_Model,horizontal=True,index=0)
    if vAR_input_model != 'Select':
        with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_Category = ['Select','Art of Prompt','Character Play','Expertise','Writing Formats','Content Creation','Prompting Methods']
            vAR_input = st.selectbox(' ',vAR_Category)
        if vAR_input =='Character Play':
            role_playing(vAR_input_model,col1,col2)
        elif vAR_input =='Expertise':
            learn(vAR_input_model,col1,col2)
        elif vAR_input =='Writing Formats':
            writing(vAR_input_model,col1,col2)
        elif vAR_input =='Art of Prompt':
            How_to_prompt(vAR_input_model,col1,col2)
        elif vAR_input == 'Prompting Methods':
            Prompt_technique(vAR_input_model,col1,col2)
        elif vAR_input == 'Tone Modifier':
            Tone_Modifier(vAR_input_model,col1,col2)
        elif vAR_input == 'Content Creation':
            content_Creation(vAR_input_model,col1,col2)