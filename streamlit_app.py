import streamlit as st
import algorithm
import graph

# Custom CSS to style the app
def set_custom_style():
    st.markdown(
        """
        <style>
        :root {
            --primary-color-light: white;
            --secondary-color-light: white;
            --text-color-light: #333333;
            --background-color-light: #F0F0F0;
            
            --primary-color-dark: black;
            --secondary-color-dark: black;
            --text-color-dark: #ECF0F1;
            --background-color-dark: #34495E;
        }
        body {
            font-family: 'Roboto', sans-serif;
            transition: all 0.3s ease;
        }
        body.light-mode {
            background-color: var(--background-color-light);
            color: var(--text-color-light);
        }
        body.dark-mode {
            background-color: var(--background-color-dark);
            color: var(--text-color-dark);
        }
        .header {
            padding: 2rem 0;
            text-align: center;
            margin-bottom: 2rem;
        }
        .light-mode .header {
            background-color: var(--primary-color-light);
            color: var(--text-color-light);
        }
        .dark-mode .header {
            background-color: var(--primary-color-dark);
            color: var(--text-color-dark);
        }
        h1 {
            font-size: 4rem;
        }
        p {
            font-size: 1.2rem;
        }
        .course-selector {
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
            text-align: center;
        }
        .light-mode .course-selector {
            background-color: white;
        }
        .dark-mode .course-selector {
            background-color: #2C3E50;
        }
        .submit-button, .clear-button {
            border: none;
            padding: 1rem 1.5rem;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.2rem;
            transition: background-color 0.3s;
        }
        .light-mode .submit-button, .light-mode .clear-button {
            background-color: var(--primary-color-light);
            color: var(--text-color-light);
        }
        .dark-mode .submit-button, .dark-mode .clear-button {
            background-color: var(--primary-color-dark);
            color: var(--text-color-dark);
        }
        .submit-button:hover, .clear-button:hover {
            background-color: var(--secondary-color-light);
        }
        .dark-mode .submit-button:hover, .dark-mode .clear-button:hover {
            background-color: var(--secondary-color-dark);
        }
        .footer {
            text-align: center;
            padding: 1.5rem;
            margin-top: 2rem;
        }
        .light-mode .footer {
            background-color: var(--primary-color-light);
            color: var(--text-color-light);
        }
        .dark-mode .footer {
            background-color: var(--primary-color-dark);
            color: var(--text-color-dark);
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

def toggle_theme():
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'
    
    if st.button('Toggle Theme'):
        st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
    
    # Apply the theme
    st.markdown(f"""
        <script>
            var body = window.parent.document.querySelector('body');
            body.classList.remove('light-mode', 'dark-mode');
            body.classList.add('{st.session_state.theme}-mode');
        </script>
        """, unsafe_allow_html=True)

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
    toggle_theme()
    header()
    course_selector()
    buttons()
    footer()

if __name__ == "__main__":
    main()