import json
from collections import defaultdict

def get_prerequisites(course, data, visited=None, depth=0, max_depth=5):
    if visited is None:
        visited = set()

    course_code = course['Course_Code']
    if course_code in visited or depth >= max_depth:
        return {'Course_Code': course_code, 'Prerequisites': []}

    visited.add(course_code)
    prerequisites = course.get('Prerequisites', [])
    prereq_details = []

    course_dict = {c['Course_Code']: c for c in data}
    for each_entry in prerequisites:
        if each_entry in course_dict:
            nested_prereqs = get_prerequisites(course_dict[each_entry], data, visited.copy(), depth + 1, max_depth)
            prereq_details.append(nested_prereqs)

    return {
        'Course_Code': course_code,
        'Prerequisites': prerequisites,
        'Nested_Prerequisites': prereq_details if prereq_details else None
    }

def format_prerequisites(nested_prereqs):
    result = defaultdict(set)  # Use a set to avoid duplicates
    
    def traverse(course_info):
        course_code = course_info['Course_Code']
        prerequisites = course_info['Prerequisites']
        
        # Add the course and its prerequisites to the result
        result[course_code].update(prerequisites)  # Use update to add unique items
        
        # Traverse nested prerequisites if they exist
        nested_prereqs = course_info.get('Nested_Prerequisites')
        if nested_prereqs:
            for prereq in nested_prereqs:
                traverse(prereq)

    traverse(nested_prereqs)
    return {course: list(prereqs) for course, prereqs in result.items()}  # Convert sets back to lists

def main(course_title, data):
    course_title = course_title.upper().strip()
    course_dict = {course['Course_Code'].upper(): course for course in data if 'Course_Code' in course and course['Course_Code']}
    
    for code, course in course_dict.items():
        if course_title in code:
            return get_prerequisites(course, data)
    
    return False

def course_code_exists(course_code, data):
    course_code = course_code.upper()
    return any(course['Course_Code'] == course_code for course in data)

def get_title(selected_course, data):
    for course in data:
        if course['Course_Code'] == selected_course:
            return course['Course_Title']
    return "Course title not found"

def get_link(selected_course, data):
    for course in data:
        if course['Course_Code'] == selected_course:
            return course['Link']
    return "Course Link not found"

def get_all_courses():
    with open('courses.json', 'r') as f:
        data = json.load(f)
    return [course['Course_Code'] for course in data]

def is_course_in_system(course_code):
    # This is a placeholder implementation. Replace with actual logic to check your course database.
    all_courses = get_all_courses()  # You'll need to implement this function to return all course codes
    return course_code.upper() in all_courses

def final(selected_course):
    title = ""
    link = ""
    output = ""
    selected_course = selected_course.strip().upper()
    user_input = selected_course
    with open('courses.json', 'r') as f:
        data = json.load(f)
    # Validate input
    if course_code_exists(user_input, data):
        title = get_title(user_input,data)
        link = get_link(user_input,data)
        output = format_prerequisites(main(user_input, data))
        return title,link,output
    else:
        return("Course code not found. Please enter a valid course code.")
