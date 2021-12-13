from flask import Flask, redirect , url_for
app = Flask(__name__)

@app.route('/home_page')
@app.route('/home')
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


@app.route('/about', methods=['post'])
def about_func():
    #TODO
    # Do something DB
    return "Welcome to about page"

# check



@app.route('/catalogs')
def catalog_func():
    return "Welcome to catalog page"

    #todo
    #url_for - calling func
    #redirect -route
    #return redirect(url_for('catalog_func'))

# Ars!!!!!