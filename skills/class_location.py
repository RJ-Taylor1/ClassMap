from models import ClassLocation

def get_class_location(course_code):
    # Mock data for demonstration purposes
    class_locations = {
        'Chem 2010': ClassLocation('Science Building', 'Room 101'),
        'Math 2020': ClassLocation('Math Building', 'Room 202')
    }

    return class_locations.get(course_code, None)
