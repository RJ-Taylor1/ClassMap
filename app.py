python
from flask import Flask, render_template, request
from skills.class_location import get_class_location
from skills.transit_info import get_transit_info

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        course_code = request.form['course_code']
        start_location = request.form['start_location']
        end_location = request.form['end_location']

        class_location = get_class_location(course_code)
        transit_info = get_transit_info(start_location, end_location)

        return render_template('index.html', class_location=class_location, transit_info=transit_info)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
