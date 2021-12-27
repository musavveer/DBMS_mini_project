from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
from flask_mail import Mail


# initializing for db connection
local_server=True
app = Flask(__name__)
app.secret_key='mit'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/virtual_classroom'
db=SQLAlchemy(app)

# getting user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# db tables
class ASSIGNMENT(db.Model):
    course_code=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    description=db.Column(db.String(100))
    deadline=db.Column(db.Integer)
    
class User(UserMixin,db.Model):
    name=db.Column(db.String(50))
    usn=db.Column(db.String(20),primary_key=True)
    #course=db.Column(db.String(10))
    #sem=db.Column(db.Integer)
    #dob=db.Column(db.Integer)
    email=db.Column(db.String(50))
    #password=db.Column(db.String(100))   

# endpoints
@app.route('/')
def main():
    return render_template('home page.html')

@app.route('/home')
def home():
    return render_template('index.html')    

@app.route('/course')
def course():
    return render_template('course.html')



@app.route('/course-material')
def course_material():
    return render_template('course_material.html')

@app.route('/academics')
def academics():
    return render_template('academics.html') 






@app.route('/student signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        name=request.form.get('name')
        usn=request.form.get('usn')
        #course=request.form.get('course')
        #sem=request.form.get('sem')
        #dob=request.form.get('dob')
        email=request.form.get('email')
        #password=request.form.get('password')
       # user=User.query.filter_by(email=email).first()
        #if user:
            #flash("Email Already Exist","warning")
           # return render_template('/student signup.html')
        #encpassword=generate_password_hash(password)

        new_user=db.engine.execute(f"INSERT INTO `user` ('name', 'usn', 'email') VALUES ('{name}', '{usn}','{email}')")

        
        flash("Signup Success Please Login","success")
        return render_template('student login.html')

    return render_template('student signup.html')





@app.route('/student login')
def s_login():
    return render_template('student login.html')    

app.run(debug=True)