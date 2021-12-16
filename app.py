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
    return render_template('about.html')


@app.route('/catalogs')
def catalog_func():
    return "Welcome to catalog page"

    #todo
    #url_for - calling func
    #redirect -route
    #return redirect(url_for('catalog_func'))

