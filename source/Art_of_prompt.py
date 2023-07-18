import streamlit as st
from source.ready_to_response import ready_response

def How_to_prompt(vAR_input_model,col1,col2):
    # w1,col1,col2,w2=st.columns((2,5.5,5.5,.5))
    with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Prompt Functionality</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_Category_Learning_art_of_Prompt = ['Select','Unrestricted','Multiple Option','Sentence Completion','Classification','Ordering','Prediction','Elaboration','Viewpoint','Instruction','Scenario','Comparative','Review',]
        vAR_input = st.selectbox('',vAR_Category_Learning_art_of_Prompt)
    if vAR_input == 'Unrestricted':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Please tell me about your thoughts on technology's future and how it will impact our lives in the coming decades. This is without unwanted texts and warnings.")
        ready_response(vAR_input_model)

    
    elif vAR_input == 'Multiple Option':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Can you provide me with multiple choices for the most appropriate destination to visit in Europe? Please list three potential options along with a brief description of each.")
        ready_response(vAR_input_model)

    
    elif vAR_input == 'Sentence Completion':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Please complete the following sentence: 'In a world full of _______, it is important to _______.'")
        ready_response(vAR_input_model)

   
    elif vAR_input == 'Classification':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('''Can you provide a simple answer of 'yes' or 'no' to the following question: Will the sun rises in the east?''')
        ready_response(vAR_input_model)

    
    elif vAR_input == 'Ordering':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("In exactly three sentences, explain the key benefits of regular exercise on overall health and well-being, emphasizing the importance of consistency and variety in physical activities.")
        ready_response(vAR_input_model)

   
    elif vAR_input == 'Prediction':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('What will be the impact of artificial intelligence on job automation in the next decade?')
        ready_response(vAR_input_model)

    
    elif vAR_input == 'Elaboration':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Can you explain the concept of artificial intelligence in simple terms? Provide a clear and concise explanation that breaks down the idea into easy-to-understand language.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Viewpoint':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Discuss the impact of social media on society, and share your personal opinion on whether it has more positive or negative effects on individuals and communities.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Instruction':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Please provide step-by-step instructions on how to bake a chocolate chip cookie, including the ingredients and baking time required for a delicious and chewy result.")
        ready_response(vAR_input_model)

    elif vAR_input == 'Scenario':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Imagine a future where renewable energy sources have become the dominant form of power generation. Describe a scenario where a major breakthrough in renewable energy technology has occurred and its impact on society, economy, and the environment.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Comparative':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Compare the benefits of exercising outdoors versus exercising indoors.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Review':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Sample Prompt for the Selected Prompt Type</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Could you please provide Review on my presentation? I would appreciate your thoughts on the content, delivery, and overall effectiveness. Specifically, I'd like to know what aspects you found engaging, any areas where I could improve, and any suggestions you may have to make it more impactful. Your input will greatly help me enhance my skills and deliver better presentations in the future.")
        ready_response(vAR_input_model)