from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)


@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_func():  # put application's code here
    return render_template('Index.html')


if __name__ == '__main__':
    app.run(debug=True)



@app.route('/about')
def about_func(): # return about page
    name = 'Tomer'
    profile={'name': 'Guy', 'university':'second_name'}
    degrees=['BSc','MSc']
    hobbies=('art','surf','music')
    university = 'BGU'
    second_name = 'Tom'
    return render_template('about.html', name='Yuval'
        ,second_name=second_name, uni=university
        ,profile=profile,degrees=degrees,hobbies=hobbies)



@app.route('/catalogs')
def catalog_func():
    return "Welcome to catalog page"

    #todo
    #url_for - calling func
    #redirect -route
    #return redirect(url_for('catalog_func'))