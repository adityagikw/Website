from flask import Flask , render_template, request,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'
db=SQLAlchemy(app)

class user(db.Model):
    id=db.Column("user_id",db.Integer,primary_key=True)
    Roll_No=db.Column("Roll_No",db.String(100))
    Fullname=db.Column("Fullname",db.String(100))
    Email=db.Column("Email",db.String(100))
    Description=db.Column("Description",db.String(200))
    
def __init__(self,Roll_NO,Fullname,Email,Description):
    self.Roll_No=Roll_NO
    self.Fullname=Fullname
    self.Email=Email
    self.Description=Description
   

@app.route('/', methods =["GET", "POST"])
def mypage():
    if request.method == "POST":
        roll_no = request.form.get("rname")
        full_name = request.form.get("fname")
        email = request.form.get("ename")
        description = request.form.get("dname")
        a= user.query.filter_by(Roll_No=roll_no).first()
        if roll_no=="" or full_name=="":
            return render_template("no input.html")
        elif roll_no==a:
             return render_template("no input.html")
        else:
            usr=user(Roll_No=roll_no,Fullname=full_name,Email=email,Description=description)
            db.session.add(usr)
            db.session.commit()
    all_user=user.query.all()
    return render_template("index.html",all_user=all_user)
@app.route('/about', methods =["GET", "POST"])
def about():
    return render_template("about.html")    


if __name__=="__main__":
    with app.app_context():    
        db.create_all()
    app.run(debug=True)
