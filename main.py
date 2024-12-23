from flask import Flask, abort, render_template, request
from models import db, UserView

app = Flask(__name__)
app.config["PREFERRED_URL_SCHEME"] = "https"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///santaDB.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def reset_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

def generate_pairs(names):
    from random import shuffle

    receivers = names.copy()
    
    while any(giver == receiver for giver, receiver in zip(names, receivers)):
        shuffle(receivers)
    
    return list(zip(names, receivers))

def add_people(nameList):
    with app.app_context():

        users = {}
        for person in nameList:
            user = UserView(user=person)
            users[person] = user
            db.session.add(user)
        #to get the ID's
        db.session.commit()
        

        pairs = generate_pairs(nameList)
        for person, target in pairs:
            users[person].target_id = users[target].id
            
        db.session.commit()

def update_own_description(user, text):
    user.user_description = text
    db.session.add(user)
    db.session.commit()

@app.route("/")
def index():
    return render_template("overview.html", users=db.session.query(UserView))

@app.route("/<user_id>", methods=['GET', 'POST'])
def user_route(user_id):
    user = db.session.query(UserView).filter_by(id=user_id).first()
    if not user:
        abort(404)

    if request.method == "POST":
        text = request.form.get("description")
        update_own_description(user, text)

    return render_template("user.html", user=user)
    

@app.errorhandler(404)
def page_not_found(e):
     return "<h1 style='font-size: 10vh; color: red;'>Vale lingi panid, vaata uuesti</h1>", 404

if __name__ == '__main__':
    app.config['ENV'] = 'production'
    app.config['DEBUG'] = False
    app.run(host='0.0.0.0', port=8000) 
    #gunicorn --bind 0.0.0.0:8000 wsgi:app

    #reset_db()
    #testnames = ["Henrik", "Karl", "Rasmus", "Arne", "Art"]
    #add_people(testnames)