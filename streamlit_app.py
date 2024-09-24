import streamlit as st
import algorithm
import graph

# Custom CSS to style the app
def set_custom_style():
    st.markdown(
        """
        <style>
        :root {
            --primary-color: #FFFFFF;
            --secondary-color: #000000;
            --text-color: #333333;
            --background-color: #FFFFFF;
            --button-bg-color: #000000;
            --button-text-color: #FFFFFF;
        }
        body {
            font-family: 'Roboto', sans-serif;
            background-color: var(--background-color);
            color: var(--text-color);
        }
        .header {
            background-color: var(--background-color);
            color: var(--primary-color);
            padding: 2rem 0;
            text-align: center;
            margin-bottom: 2rem;
            border-bottom: 1px solid #EEEEEE;
        }
        h1 {
            font-size: 4rem;
            color: var(--primary-color:);
        }
        h3 {
            color: var(--primary-color:);
        }
        p {
            color: var(--primary-color:);
            font-size: 1.2rem;
        }
        .course-selector {
            background-color: var(--primary-color);
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
            text-align: center;
        }
        .stButton > button {
            background-color: var(--button-bg-color);
            color: var(--button-text-color);
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            transition: background-color 0.3s;
        }
        .stButton > button:hover {
            background-color: #333333;
        }
        .footer {
            text-align: center;
            color: var(--text-color);
            padding: 1.5rem;
            background-color: var(--primary-color);
            margin-top: 2rem;
            border-top: 1px solid #EEEEEE;
        }
        .footer img {
            width: 24px;
            height: 24px;
            vertical-align: middle;
            margin: 0 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def header():
    st.markdown(
        '<div class="header">'
        '<h1>NKU Course Navigator</h1>'
        '<h3>Find and navigate your courses with ease</h3>'
        '</div>',
        unsafe_allow_html=True
    )

def course_selector():
    if 'selected_course' not in st.session_state:
        st.session_state['selected_course'] = ""
    
    st.session_state['selected_course'] = st.text_input(
        "Enter a course name", 
        st.session_state['selected_course']
    )

def buttons():
    col1, col2 = st.columns([8, 1])
    
    with col1:
        if st.button('Submit', key="submit", help="Click to submit the selected course"):
            if st.session_state['selected_course']:
                course_details = algorithm.final(st.session_state['selected_course'])
                graphs = graph.generate_graph(course_details)
                st.write(f"### You entered: {st.session_state['selected_course']}")
                st.image(graphs, caption="Course Prerequisites Graph")
            else:
                st.write("Please enter a course name.")
    
    with col2:
        if st.button('Clear', key="clear", help="Click to clear the input"):
            st.session_state['selected_course'] = ""


def footer():
    st.markdown(
        """
        <div class="footer">
            <p>&copy; 2024 NKU Data Science Club</p>
            <a href="https://www.instagram.com/nku_data_science_club/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" />
            </a>
            <a href="https://discord.gg/Q6URhaSz55" target="_blank">
                <img src="https://static.cdnlogo.com/logos/d/15/discord.svg" alt="Discord" />
            </a>
            <a href="https://www.nku.edu/academics/informatics/beyond/student-organizations.html" target="_blank">
                <img src="https://content.sportslogos.net/logos/33/5047/full/northern_kentucky_norse_logo_secondary_2014_sportslogosnet-1943.png" alt="NKU Student Organizations Page" />
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    set_custom_style()
    header()
    course_selector()
    buttons()
    footer()

if __name__ == "__main__":
    main()



