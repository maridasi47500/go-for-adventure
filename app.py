from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,email,password,phone,country_id) values (:username,:email,:password,:phone,:country_id)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','email','password','phone','country_id']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','email','password','phone','country_id']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','email','password','phone','country_id']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into city (name,country_id) values (:name,:country_id)",hey)
        user = query_db('select * from city')

        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)

@app.route("/add_one_sport", methods=["GET","POST"])
def add_one_sport():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into sport (name) values (:name)",hey)
        user = query_db('select * from sport')

        return render_template("sportform.html", sports=user, one_user=one_user, the_title="add new sport")


    user = query_db('select * from sport')
    one_user = query_db("select * from sport limit 1", one=True)
    return render_template("sportform.html", sports=user, one_user=one_user, the_title="add new sport")

@app.route("/add_one_musicalinstrument", methods=["GET","POST"])
def add_one_musicalinstrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musicalinstrument (name) values (:name)",hey)
        user = query_db('select * from musicalinstrument')

        return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")


    user = query_db('select * from musicalinstrument')
    one_user = query_db("select * from musicalinstrument limit 1", one=True)
    return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")

@app.route("/add_one_job", methods=["GET","POST"])
def add_one_job():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into job (name) values (:name)",hey)
        user = query_db('select * from job')

        return render_template("jobform.html", jobs=user, one_user=one_user, the_title="add new job")


    user = query_db('select * from job')
    one_user = query_db("select * from job limit 1", one=True)
    return render_template("jobform.html", jobs=user, one_user=one_user, the_title="add new job")

@app.route("/add_one_destination", methods=["GET","POST"])
def add_one_destination():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslescity= query_db("select * from city")

        touslesadventure= query_db("select * from adventure")

        one_user = query_db("insert into destination (user_id,city_id,adventure_id) values (:user_id,:city_id,:adventure_id)",hey)
        user = query_db('select * from destination')

        return render_template("destinationform.html", destinations=user, one_user=one_user, the_title="add new destination", touslesuser=touslesuser, touslescity=touslescity, touslesadventure=touslesadventure)


    touslesuser= query_db("select * from user")

    touslescity= query_db("select * from city")

    touslesadventure= query_db("select * from adventure")

    user = query_db('select * from destination')
    one_user = query_db("select * from destination limit 1", one=True)
    return render_template("destinationform.html", destinations=user, one_user=one_user, the_title="add new destination", touslesuser=touslesuser, touslescity=touslescity, touslesadventure=touslesadventure)

@app.route("/add_one_usersport", methods=["GET","POST"])
def add_one_usersport():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslessport= query_db("select * from sport")

        touslesadventure= query_db("select * from adventure")

        one_user = query_db("insert into usersport (user_id,sport_id,adventure_id) values (:user_id,:sport_id,:adventure_id)",hey)
        user = query_db('select * from usersport')

        return render_template("usersportform.html", usersports=user, one_user=one_user, the_title="add new usersport", touslesuser=touslesuser, touslessport=touslessport, touslesadventure=touslesadventure)


    touslesuser= query_db("select * from user")

    touslessport= query_db("select * from sport")

    touslesadventure= query_db("select * from adventure")

    user = query_db('select * from usersport')
    one_user = query_db("select * from usersport limit 1", one=True)
    return render_template("usersportform.html", usersports=user, one_user=one_user, the_title="add new usersport", touslesuser=touslesuser, touslessport=touslessport, touslesadventure=touslesadventure)

@app.route("/add_one_userjob", methods=["GET","POST"])
def add_one_userjob():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesjob= query_db("select * from job")

        touslesadventure= query_db("select * from adventure")

        one_user = query_db("insert into userjob (user_id,job_id,adventure_id) values (:user_id,:job_id,:adventure_id)",hey)
        user = query_db('select * from userjob')

        return render_template("userjobform.html", userjobs=user, one_user=one_user, the_title="add new userjob", touslesuser=touslesuser, touslesjob=touslesjob, touslesadventure=touslesadventure)


    touslesuser= query_db("select * from user")

    touslesjob= query_db("select * from job")

    touslesadventure= query_db("select * from adventure")

    user = query_db('select * from userjob')
    one_user = query_db("select * from userjob limit 1", one=True)
    return render_template("userjobform.html", userjobs=user, one_user=one_user, the_title="add new userjob", touslesuser=touslesuser, touslesjob=touslesjob, touslesadventure=touslesadventure)

@app.route("/add_one_usermusicalinstrument", methods=["GET","POST"])
def add_one_usermusicalinstrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesmusicalinstrument= query_db("select * from musicalinstrument")

        touslesadventure= query_db("select * from adventure")

        one_user = query_db("insert into usermusicalinstrument (user_id,musicalinstrument_id,adventure_id) values (:user_id,:musicalinstrument_id,:adventure_id)",hey)
        user = query_db('select * from usermusicalinstrument')

        return render_template("usermusicalinstrumentform.html", usermusicalinstruments=user, one_user=one_user, the_title="add new usermusicalinstrument", touslesuser=touslesuser, touslesmusicalinstrument=touslesmusicalinstrument, touslesadventure=touslesadventure)


    touslesuser= query_db("select * from user")

    touslesmusicalinstrument= query_db("select * from musicalinstrument")

    touslesadventure= query_db("select * from adventure")

    user = query_db('select * from usermusicalinstrument')
    one_user = query_db("select * from usermusicalinstrument limit 1", one=True)
    return render_template("usermusicalinstrumentform.html", usermusicalinstruments=user, one_user=one_user, the_title="add new usermusicalinstrument", touslesuser=touslesuser, touslesmusicalinstrument=touslesmusicalinstrument, touslesadventure=touslesadventure)

@app.route("/add_one_adventure", methods=["GET","POST"])
def add_one_adventure():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        one_user = query_db("insert into adventure (title,description,pic) values (:title,:description,:pic)",hey)
        user = query_db('select * from adventure')

        return render_template("adventureform.html", adventures=user, one_user=one_user, the_title="add new adventure")


    user = query_db('select * from adventure')
    one_user = query_db("select * from adventure limit 1", one=True)
    return render_template("adventureform.html", adventures=user, one_user=one_user, the_title="add new adventure")

