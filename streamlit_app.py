import streamlit as st
import algorithm
import graph

# Custom CSS to style the app
def set_custom_style():
    st.markdown(
        """
        <style>
        :root {
            --primary-color: white;
            --secondary-color: black;
            --background-color: var(--primary-color);
            --text-color: var(--secondary-color);
            --button-bg-color: var(--secondary-color);
            --button-text-color: var(--primary-color);
        }
        @media (prefers-color-scheme: dark) {
            :root {
                --background-color: var(--secondary-color);
                --text-color: var(--primary-color);
                --button-bg-color: var(--primary-color);
                --button-text-color: var(--secondary-color);
            }
        }
        body {
            font-family: 'Roboto', sans-serif;
            background-color: var(--background-color);
            color: var(--text-color);
            transform-origin: 0 0;
        }
        .header {
            background-color: var(--background-color);
            color: var(--text-color);
            padding: 2rem 0;
            text-align: center;
            margin-bottom: 2rem;
            border-bottom: 1px solid var(--text-color);
        }
        h1 {
            font-size: 4rem;
            color: var(--text-color);
        }
        h3 {
            color: var(--text-color);
        }
        p {
            color: var(--text-color);
            font-size: 1.2rem;
        }
        .course-selector {
            background-color: var(--background-color);
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
            opacity: 0.8;
        }
        .footer {
            text-align: center;
            color: var(--text-color);
            padding: 1.5rem;
            background-color: var(--background-color);
            margin-top: 2rem;
            border-top: 1px solid var(--text-color);
        }
        .footer img {
            width: 24px;
            height: 24px;
            vertical-align: middle;
            margin: 0 5px;
            filter: invert(1);
        }
        @media (prefers-color-scheme: dark) {
            .footer img {
                filter: invert(0);
            }
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
                if algorithm.is_course_in_system(st.session_state['selected_course']):
                    course_title, course_link, course_details = algorithm.final(st.session_state['selected_course'])
                    
                    # Store the results in session state
                    st.session_state['course_title'] = course_title
                    st.session_state['course_link'] = course_link
                    st.session_state['course_details'] = course_details
                    st.session_state['show_results'] = True
                else:
                    st.session_state['show_results'] = False
                    st.write("This course is not in the system. Please check the course name and Try Again.")
            else:
                st.session_state['show_results'] = False
                st.write("Please enter a course name.")
    
    with col2:
        if st.button('Clear', key="clear", help="Click to clear the output"):
            st.session_state['show_results'] = False
    
    # Display results if they should be shown
    if st.session_state.get('show_results', False):
        course_title = st.session_state['course_title']
        course_link = st.session_state['course_link']
        course_details = st.session_state['course_details']
        
        if course_details and all(len(prereqs) == 0 for prereqs in course_details.values()):
            st.write(f"### {st.session_state['selected_course'].upper()}: {course_title}")
            st.write("This course needs no prerequisites.")
            st.markdown(f"[Course Link]({course_link})", unsafe_allow_html=True)
        else:
            graphs = graph.generate_graph(course_details)
            st.markdown(f"### {st.session_state['selected_course'].upper()}: {course_title} | [Course Link]({course_link})", unsafe_allow_html=True)
            st.image(graphs, use_column_width="auto", output_format="PNG")

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

def course_navigation():
    st.header("Course Navigation")
    course_selector()
    buttons()

def professor_recommendation():
    st.header("Professor Recommendation")
    st.write("This feature is coming soon. Stay tuned!")

def about_the_club():
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #003366;
        margin-bottom: 20px;
    }
    .club-description {
        font-size: 18px;
        line-height: 1.6;
        margin-bottom: 30px;
        padding: 20px;
        background-color: #f0f8ff;
        border-radius: 10px;
        border-left: 5px solid #003366;
    }
    .team-member {
        margin-bottom: 15px;
        padding: 10px;
        background-color: #e6f2ff;
        border-radius: 5px;
    }
    .team-member-role {
        font-weight: bold;
        color: #003366;
    }
    .team-member-name {
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">About the Data Science Club</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="club-description">
    The Data Science Club is created for all those interested in topics related to Data Science and Data Analytics, 
    not just those interested in pursuing a career in the field. We discuss new technologies, internship/career experiences, 
    and other special topics. All skill levels and majors are welcome.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Our Team")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="team-member">
            <span class="team-member-role">Advisor:</span><br>
            <span class="team-member-name">Dr. YangYang Tao</span><br>
            <span class="team-member-email">taoy1@nku.edu</span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="team-member">
            <span class="team-member-role">E-board Member:</span><br>
            <span class="team-member-name">Mithilesh Sah</span><br>
            <span class="team-member-email">sahm1@nku.edu</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="team-member">
            <span class="team-member-role">President:</span><br>
            <span class="team-member-name">Gaurab Baral</span><br>
            <span class="team-member-email">baralg1@nku.edu</span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="team-member">
            <span class="team-member-role">E-board Member:</span><br>
            <span class="team-member-name">Sushant Man Shrestha</span><br>
            <span class="team-member-email">shresthas11@nku.edu</span>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="team-member">
            <span class="team-member-role">Vice President:</span><br>
            <span class="team-member-name">Aaditya Khanal</span><br>
            <span class="team-member-email">khanala1@nku.edu</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Join Us!")
    st.write("Interested in Data Science? Join our club to learn, collaborate, and grow together!")
    st.markdown("[Link to Club Page](https://www.nku.edu/academics/informatics/beyond/student-organizations.html)")

def main():
    set_custom_style()
    
    # Create a sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Course Navigation", "Professor Recommendation", "About the Club"))
    
    header()
    
    if page == "Course Navigation":
        course_navigation()
    elif page == "Professor Recommendation":
        professor_recommendation()
    elif page == "About the Club":
        about_the_club()
    
    footer()

# Initialize session state variables if they don't exist
if 'show_results' not in st.session_state:
    st.session_state['show_results'] = False
if 'selected_course' not in st.session_state:
    st.session_state['selected_course'] = ""

if __name__ == "__main__":
    main()