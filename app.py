from flask import Flask, redirect, url_for
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_func():  # put application's code here
    found = False
    if found:
        return render_template('Index.html', name1='Tomer')
    else:
        return render_template('Index.html')


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/about')
def about_func():  # return about page
    return render_template('about.html')


@app.route('/Catalog')
def catalog_func():
    return render_template(('Catalog.html'))


@app.route('/assignment8')
def ass_func():
    name = 'Tomer'
    # dicionary
    profile = {'name': 'Guy', 'university': 'second_name'}
    # list
    degrees = ['BSc', 'MSc', 'dr']
    # tupple
    hobbies = ('art', 'surf', 'music', 'drive')
    university = 'BGU'
    second_name = 'Tom'
    return render_template('assignment8.html', name='Yuval'
                           , second_name=second_name, uni=university, profile=profile, degrees=degrees, hobbies=hobbies)


@app.route('/Login')
def login_func():
    return render_template(('login.html'))


@app.route('/Singup')
def signUp_func():
    return render_template(('Singup.html'))

# todo
# url_for - calling func
# redirect -route
# return redirect(url_for('catalog_func'))