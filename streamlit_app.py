import streamlit as st
import algorithm

# Custom CSS to style the app
def set_custom_style():
    st.markdown(
        """
        <style>
        :root {
    --primary-color: #FFEFCB; /* Off-white for a clean and modern look */
    --secondary-color: #FF6F61; /* Vibrant coral for accents */
    --text-color: #333333; /* Dark gray for improved readability */
    --background-color: #F0F0F0; /* Light gray background for subtle contrast */
}
        body {
            font-family: 'Roboto', sans-serif;
            background-color: var(--background-color);
            color: var(--text-color);
        }
        .header {
            background-color: var(--primary-color);
            padding: 2rem 0;
            text-align: center;
            color: white;
            margin-bottom: 2rem;
        }
        h1 {
            font-size: 4rem;
        }
        .course-selector {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 0rem;
            text-align: center;
            display: none;
        }
        .submit-button {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 1rem 1.5rem;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.2rem;
            transition: background-color 0.3s;
        }
        .submit-button:hover {
            background-color: var(--secondary-color);
        }
        .footer {
            text-align: center;
            padding: 1.5rem;
            background-color: var(--primary-color);
            color: white;
            margin-top: 2rem;
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
    st.markdown(
        '<span class="course-selector">'
        '</span>',
        unsafe_allow_html=True
    )
    return st.text_input("Enter a course name")

def submit_button(selected_course):
    if st.button('Submit', key="submit", help="Click to submit the selected course"):
        if selected_course:
            course_details = algorithm.final(selected_course)
            st.write(f"### You entered: {selected_course}")
            st.write(f"**Course Details:** {course_details}")
        else:
            st.write("Please enter a course name.")

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
    selected_course = course_selector()
    submit_button(selected_course)
    footer()

if __name__ == "__main__":
    main()