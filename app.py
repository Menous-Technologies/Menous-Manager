from flask import *
from flask_session import Session
import requests

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# apiurl = "http://snehashishlaskar090.pythonanywhere.com/"
apiurl = "http://127.0.0.1:8000/"


def convertUserDataToJson(username):
    data = requests.get('{}sites?username={}'.format(apiurl, username)).json()

    return data
@app.route('/auth', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        user = None
        pw = None

        try:
            user = session['username']
            pw = session['password']
        except:
            pass

        if user == None and pw == None:

            usrname = request.form['username']
            psword = request.form['password']

            data = requests.get(apiurl).json()
            
            for i in data:
                print(usrname, psword)
                if i[0] == usrname and i[1] == psword:
                    session['username'] = usrname
                    session['password'] = psword
                    return redirect('/home')
        
            return render_template('login.html', error=True)

        else:
            return redirect('/home')

    else:
        user = None
        pw = None

        try:
            user = session['username']
            pw = session['password']
        except:
            pass

        if user == None and pw == None:


            return render_template('login.html')

        else:
            return redirect('/home')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['username'] = None
    session['password'] = None
    print(session['username'])
    print(session['password'])
    return redirect('/')

@app.route('/delete', methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        return redirect('/deleteusersure')
    else:
        return render_template('delete_account.html', sess=True)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = None
        pw = None

        try:
            user = session['username']
            pw = session['password']
        except:
            pass

        if user == None and pw == None:
            username = request.form['username']
            password = request.form['password']

            query = requests.post('{}createuser?username={}&password={}'.format(
                apiurl,username, password
            ))
            session['username'] = username
            session['password'] = password

            return redirect('/auth')

        else:
            return redirect('/home')

    else:
        user = None
        pw = None

        try:
            user = session['username']
            pw = session['password']
        except:
            pass

        if user != None and pw != None:
            return redirect('/home')
        else:
            return render_template('signup.html')       


# Snehashish Laskar
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'add' in request.form:
            name = request.form['addname']
            email = request.form['addemail']
            username =  request.form['addusername']
            password = request.form['addpass']

            query = requests.post('{}addsite?username={}&sitename={}&password={}&email={}&siteusrname={}'.format(
                apiurl,
                session['username'],
                name,
                password,
                email,
                username,
            ))
            return redirect('/home')
        
        elif 'del' in request.form:
            name = request.form['name']

            query = requests.delete('{}delsite?username={}&site={}'.format(
                apiurl,
                session['username'],
                name
            ))

            return redirect('/home')
    else:
        return render_template('home.html', sess = True, data = convertUserDataToJson(session['username']))


@app.route('/cookies', methods = ['GET', 'POST'])
def cook():
    return jsonify([session['username'], session['password']])
@app.route('/', methods = ['GET', 'POST'])
def main():

    user = None
    pw = None

    try:
        user = session['username']
        pw = session['password']
    except:
        pass

    if user != None and pw != None:
        return render_template('index.html', sess = True)
    else:
        return render_template('index.html', sess = False)

@app.route('/deleteusersure', methods=["GET", "POST"])
def deleteUser():

    req = requests.post(f"{apiurl}delete?username={session['username']}")
    print(req)
    return redirect('/logout')

# if __name__ == "__main__":
#     app.run(debug=True, host = "0.0.0.0", port=80)