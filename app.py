import random

from flask import Flask, redirect,render_template, url_for, request, session
from interact_with_DB import interact_db
import requests


app = Flask(__name__)
app.secret_key = '123'


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
    profile = {'Dictionary key 1': 'Test1', 'Dictionary key 2': 'Test2'}
    # list
    degrees = ['BSc', 'MSc', 'PHD']
    # tupple
    hobbies = ('Art', 'Surf', 'Music', 'Drive')
    university = 'BGU'
    second_name = 'Tom'
    return render_template('assignment8.html', name=name , second_name=second_name,
                           uni=university, profile=profile, degrees=degrees, hobbies=hobbies)


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
    return render_template('Singup.html')


@app.route('/Logout')
def logOut_func():
    session['username'] = ''
    return render_template('index.html')

@app.route('/users')
def users_func():
    query='select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('users.html', users=users)

@app.route('/insert_user',methods=['post'])
def insert_user_func():
    name  = request.form['name']
    email  = request.form['email']
    password  = request.form['password']

    query = "insert into users(name,email,password) values ('%s','%s','%s');" % (name,email,password);
    interact_db(query=query, query_type='commit')

    return redirect('/users')


@app.route('/delete_user', methods=['post'])
def delete_func():
    user_id = request.form['id']
    query= "delete from users where id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/users')

@app.route('/request_frontend')
def request_frontend_func():
    return render_template('/request_frontend.html')


@app.route('/req_backend')
def req_backend_func():
    num=3
    if "number" in request.args:
        num=int (request.args['number'])
    pockemons=get_pockemons(num)
    return render_template('req_backend.html', pockemons=pockemons)

def get_pockemons(num):
    pokemons=[]
    for i in range(num):
        random_number=random.randint(1,100)
        res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_number}')
        #res = requests.get('https://pokeapi.co/api/v2/pokemon/%s' %random_number) #another way
        res=res.json()
        pokemons.append(res)

    return pokemons



if __name__ == '__main__':
    app.run(debug=True)
# todo
# url_for - calling func
# redirect -route
# return redirect(url_for('catalog_func'))