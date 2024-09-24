import streamlit as st

# Introductory text
st.write("## Welcome to the Course Navigation App!")
st.write("Enter the name of a course below and click 'Submit' to view course details.")

# User input for entering a course name
selected_course = st.text_input("Enter a course name")

# Button to submit and navigate to the course
if st.button('Submit'):
    if selected_course:
        # Call the function from the algorithm module to get the course details
        course_details = selected_course
        
        # Display the selected course and its details
        st.write(f"### You entered: {selected_course}")
        st.write(f"**Course Details:** {course_details}")
    else:
        st.write("Please enter a course name.")

# Additional information or inspiration
st.write(
    "For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
