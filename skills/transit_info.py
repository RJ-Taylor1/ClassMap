from models import TransitInfo

def get_transit_info(start_location, end_location):
    # Mock data for demonstration purposes
    transit_info = {
        ('Dorms', 'Science Building'): TransitInfo('Bus 31', '3 minutes'),
        ('Dorms', 'Math Building'): TransitInfo('Bus 32', '5 minutes')
    }

    return transit_info.get((start_location, end_location), None)
