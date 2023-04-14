import streamlit as st

def read_data (txt_file, output_dict):
    '''
    Reads in interview text file as dictionary

    txt_file: Text file name/path
    output_dict: variable name of resulting dict
    '''

    with open(txt_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip('\n')
            (key, val) = line.split(":")
            output_dict[key] = val

    return output_dict

def interview_response (name, image_file, ques_ans, essence = False):
    ''' 
    Loads image, questions, and responses of interviewee into 3 st.columns

    name: Interviewees Name
    image_file: Image of the interviewee
    ques_ans: Dict of questions and response to be displayed
    essence: Displays a message under the image if True
    '''

    st.header(name)
    col1, col2, col3 = st.columns(3)
    with col1: 
        st.image(image_file)
        if essence == True:
            st.write ("Unfortunately, 9 months after this interview occured, Essence was killed while working.")
    with col2: 
        questions = st.selectbox("Select a question", 
        ques_ans.keys())
    with col3:
        for key in ques_ans.keys():
            if questions == key:
                st.write(ques_ans[key])

# Page configuration
st.set_page_config(page_title="Stories of Sex Workers", layout="wide")

# Read in interview data 
amber_dict = {}
amber_dict = read_data("data/Amber_interview.txt", amber_dict)

essence_dict = {}
essence_dict = read_data("data/Essence_Interview.txt", essence_dict)

exotic_dict = {}
exotic_dict = read_data("data/Exotic_Interview.txt", exotic_dict)

# Page Display
st.sidebar.title("Interviewees")
st.title("Stories of Sex Workers")

# Sidebar dropdown 
app_mode = st.sidebar.selectbox("Select an Interview",
    ["Main", "Amber", "Essence", "Exotic"])

# Main page with images of each interviewee
if app_mode == "Main":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Amber")
        st.image("data/Amber.png", use_column_width=True)
    with col2:
        st.header("Essence")
        st.image("data/Essence.png", use_column_width=True)
    with col3:
        st.header("Exotic")
        st.image("data/Exotic.png", use_column_width=True)

# Interviewee specific pages displaying image, questions, and responses
elif app_mode == "Amber":
    interview_response("Amber", "data/Amber.png", amber_dict)
elif app_mode == "Essence":
    interview_response("Essence", "data/Essence.png", essence_dict, True)
elif app_mode == "Exotic":
    interview_response("Exotic", "data/Exotic.png", exotic_dict)