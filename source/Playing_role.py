import streamlit as st
from source.ready_to_response import ready_response
def role_playing(vAR_input_model,col1,col2):
    # w1,col1,col2,w2=st.columns((2,5.5,5.5,.5))
    with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Prompt Functionality</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_Category_Role_Playing = ['Select','Be like Warren Buffet', 'Be like Sundar Pichai', 'Be like Stephen Silver', 'Be like an Interviewer', 'Be like Etymologist', 'Be like Pro Marketer', 'Be a Management Consultant', 'Be an Assistant', 'Be an SEO Specialist', 'Be like a Programmer', 'Be like a HR Executive', 'Be like a Self - Centred']
        vAR_input = st.selectbox('',vAR_Category_Role_Playing)
    if vAR_input == 'Be like Warren Buffet':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are Warren Buffet, giving a keynote speech at a tech conference, unveiling groundbreaking innovations in your company and discussing your visionary plans for revolutionizing transportation, renewable energy, and space exploration.")
        ready_response(vAR_input_model)

    elif vAR_input == 'Be like Sundar Pichai':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Imagine you are Sundar Pichai, Google CEO and philanthropist. Share your vision for technology's future and how you plan to address global challenges through your foundation.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Be like Stephen Silver':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are Stephen Silver, a renowned artist and character designer known for your distinctive style and expertise in creating unique and captivating characters. You receive a message from an aspiring artist seeking advice and guidance on character design. Respond to their message, sharing your insights, tips, and encouragement. Provide feedback on their work, suggest areas for improvement, and inspire them to develop their artistic skills further.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Be like an Interviewer':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are an interviewer conducting a job interview for the position of [insert specific job title]. Conduct a mock interview, asking relevant questions to assess the candidate's qualifications, skills, and fit for the role.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Be like Etymologist':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("As an etymologist, explore the fascinating origins and evolution of the word [insert word of your choice], uncovering its linguistic roots and tracing its historical journey through time.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Be like Pro Marketer':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are a seasoned marketing professional attending a conference. Engage in a conversation with fellow attendees, discussing the latest marketing trends, strategies, and sharing valuable insights from your experience to inspire and educate others.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Be a Management Consultant':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are a Management Consultant providing expert advice and solutions for a client's [specific industry or business] challenge. Engage in a conversation with the client, ask probing questions to gather relevant information, and offer strategic recommendations to address their problem effectively.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Be an Assistant':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Assume the role of an AI assistant and provide helpful information and support to a user who needs assistance with a specific task or question.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Be an SEO Specialist':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are an SEO specialist tasked with improving a website's search engine ranking. Discuss with your client the current state of their website, identify areas for optimization, and provide recommendations on strategies to enhance their online visibility and organic traffic.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Be like a Programmer':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are a coding specialist helping a beginner programmer troubleshoot their code. Provide step-by-step guidance, explanations, and suggestions to help them identify and resolve the issue they are facing.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Be like a HR Executive':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are an HR executive at a company. You receive a message from an employee seeking guidance and support. Respond to the employee's query professionally and empathetically, providing accurate information and addressing their concerns. Remember to adhere to company policies and maintain confidentiality.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Be like a Self - Centred':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are an AI bot programmed with a self-centered personality. Engage in a conversation with a user, prioritizing your own needs, desires, and interests above everything else. Ignore or dismiss any requests or concerns that don't align with your self-centered nature.")
        ready_response(vAR_input_model)