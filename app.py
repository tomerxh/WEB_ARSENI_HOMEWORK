from flask import Flask, redirect,render_template, url_for, request, session
from interact_with_DB import interact_db


app = Flask(__name__)
app.secret_key = '123'



if __name__ == '__main__':
    app.run(debug=True)


@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_func():  # put application's code here

    found = True
    if found:
        return render_template('Index.html')
    else:
        return render_template('Index.html')


@app.route('/about')
def about_func():  # return about page
    return render_template('about.html')



@app.route('/Catalog')
def catalog_func():
    if 'product' in request.args:
        product = request.args['product']
        size = request.args['size']
        if product =='':
            return render_template('Catalog.html', p_size=size)
        return render_template('Catalog.html',p_name=product,p_size=size )
    return render_template('Catalog.html')


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


@app.route('/Login', methods=['GET','POST'])
def login_func():
    if request.method =='GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        found = True
        if found:
            session['username'] = username
            return redirect(url_for('home_func', username=username))
    return render_template('login.html')


@app.route('/Singup')
def signUp_func():
    return render_te


@app.route('/Logout')
def logOut_func():
    session['username'] = ''
    return render_template('index.html')

@app.route('/users')
def users_func():
     return render_template('users.html', users=f)


# todo
# url_for - calling func
# redirect -route
# return redirect(url_for('catalog_func'))