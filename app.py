from django.contrib.sites import requests
from flask import Flask, redirect,render_template, url_for, request, session , jsonify
from interact_with_DB import interact_db
import requests, random


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

# -----About------#
@app.route('/about')
def about_func():  # return about page
    return render_template('about.html')

# -----Catalog------#
@app.route('/Catalog')
def catalog_func():
    if 'product' in request.args:
        product = request.args['product']
        size = request.args['size']
        if product =='':
            return render_template('Catalog.html', p_size=size)
        return render_template('Catalog.html',p_name=product,p_size=size )
    return render_template('Catalog.html')

# -----assignment 8------#
@app.route('/assignment8')
def ass_func():
    name = 'Tomer'
    # dictionary
    profile = {'dictionary 1': 'Test1', 'dictionary 2': 'Test2'}
    # list
    degrees = ['BSc', 'MSc', 'PHD']
    # tuple
    hobbies = ('art', 'surf', 'music', 'drive')
    university = 'BGU'
    second_name = 'Tom'
    return render_template('assignment8.html', name=name, second_name=second_name,
                           uni=university, profile=profile, degrees=degrees, hobbies=hobbies)



# -----assignment 9------#
@app.route('/assignment9', methods=['GET', 'POST'])
def ass9_func():
    username = ''
    Users = [
        {'id': 1, 'email': "omer_adam@gmail.com", 'firstname': "Omer", 'lastname': "Adam"},
        {'id': 2, 'email': "Davidblue@gmail.com", 'firstname': "David", 'lastname': "Blue"},
        {'id': 3, 'email': "AviBen@gmail.com", 'firstname': "Avi", 'lastname': "Ben"},
        {'id': 4, 'email': "mokeeD@gmail.com", 'firstname': "Mok", 'lastname': "di"},
        {'id': 5, 'email': "GuyAman@gmail.com", 'firstname': "Guy", 'lastname': "Aman"},
        {'id': 6, 'email': "Dennislloyd@gmail.com", 'firstname': "Dennis", 'lastname': "lloyd"}
    ]
    firstname = ''
    if request.method == 'GET':
        if 'firstname' in request.args:
            firstname = request.args['firstname']
    elif request.method == 'POST':
        if 'username' in request.form:
            username = request.form['username']
            session['LoggedIn'] = True
            session['username'] = username
        else:
            session['LoggedIn'] = False
            session['username'] = ''
            username = ''
    return render_template('Assignment9.html', Users=Users, username=username, firstname=firstname,
                           request_method=request.method)

# -----assignment 11------#

@app.route('/assignment11/users')
def json_users_func():
    query = "select * from users"
    users_query = interact_db(query=query, query_type='fetch')
    json_users = jsonify(users_query)
    return json_users

def get_user(id_num):
    user = requests.get(f' https://reqres.in/api/users/{id_num}')
    user = user.json()
    return user


@app.route('/assignment11/outer_source', methods=['GET', 'POST'])
def assignment11_outsource():
    if request.method == 'POST':
        id_num = request.form['id']
        user = get_user(id_num)
        return render_template('assignment11_out.html', user=user)
    return render_template('assignment11_out.html')


# -----assignment 12------#
@app.route('/assignment12')
def ass12_func():
    return render_template('assignment12.html')


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


# -----Sign up------#
@app.route('/Singup')
def signUp_func():
    return render_template('Singup.html')
# -----Log out------#
@app.route('/Logout')
def logOut_func():
    session['username'] = ''
    return render_template('index.html')

# -----Users class------#
@app.route('/users')
def users_func():
    query='select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('users.html', users=users)

@app.route('/insert_user',methods=['post'])
def insert_user_func():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password  = request.form['password']

    query = "insert into users(first_name,last_name,email,password) values ('%s','%s','%s','%s');" % (first_name,last_name,email,password);
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


from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

if __name__ == '__main__':
    app.run(debug=True)
# todo
# url_for - calling func
# redirect -route
# return redirect(url_for('catalog_func'))