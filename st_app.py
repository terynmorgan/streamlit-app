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

def interview_response (name, image_file, ques_ans, amber = False, essence = False, exotic = False):
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
        if amber == True:
            st.markdown(
                        """<a href="https://www.youtube.com/watch?v=kiL03oAt-9k">Amber Full Interview</a>""", unsafe_allow_html=True,
                    )
        if essence == True:
            st.write ("Unfortunately, 9 months after this interview occured, Essence was killed while working.")
            st.markdown(
                    """<a href="https://www.youtube.com/watch?v=n0ApqA1s9f0&list=PLx-RTYDKq6TyXPdyyG1fiqNe1dxB9rGj8&index=4">Essence Full Interview</a>""", unsafe_allow_html=True,
                )
        if exotic == True:
            st.markdown(
                    """<a href="https://www.youtube.com/watch?v=ItUUmukrKM0&list=PLx-RTYDKq6TyXPdyyG1fiqNe1dxB9rGj8&index=2">Exotic Full Interview</a>""", unsafe_allow_html=True,
                )
    with col2: 
        questions = st.selectbox("Select a question", 
        ques_ans.keys())
    with col3:
        for key in ques_ans.keys():
            if questions == key:
                st.markdown("""
                            <style>
                            .big-font {
                                font-size:20px !important;
                            }
                            </style>
                            """, unsafe_allow_html=True)
                st.markdown(f'''<p class="big-font">{ques_ans[key]}</p>''', unsafe_allow_html=True)
                
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
        st.write ("All information found in this application has been transcribed from responses in interviews from Soft White Underbelly: ")
        st.markdown("""<a href="https://www.youtube.com/@SoftWhiteUnderbelly">Soft White Underbelly YouTube Channel</a>""", unsafe_allow_html=True,)
    with col2:
        st.header("Essence")
        st.image("data/Essence.png", use_column_width=True)
    with col3:
        st.header("Exotic")
        st.image("data/Exotic.png", use_column_width=True)
        
# Interviewee specific pages displaying image, questions, and responses
elif app_mode == "Amber":
    interview_response("Amber", "data/Amber.png", amber_dict, amber=True, essence=False, exotic=False)
elif app_mode == "Essence":
    interview_response("Essence", "data/Essence.png", essence_dict, amber=False, essence=True, exotic=False)
elif app_mode == "Exotic":
    interview_response("Exotic", "data/Exotic.png", exotic_dict, amber=False, essence=False, exotic=True)
