from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Render Postgres database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://vrijwilligers_aanmeldingen_user:YkMEUgISy42WVnotoVBfW04E73rIdJHF@dpg-d6o1lrua2pns73fsl1ag-a/vrijwilligers_aanmeldingen"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Database tabel
class Vrijwilliger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefoon = db.Column(db.String(50), nullable=True)
    motivatie = db.Column(db.Text, nullable=True)


# Maak tabel automatisch
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/vrijwilligers", methods=["GET", "POST"])
def vrijwilligers():
    if request.method == "POST":
        naam = request.form.get("naam", "").strip()
        email = request.form.get("email", "").strip()
        telefoon = request.form.get("telefoon", "").strip()
        motivatie = request.form.get("motivatie", "").strip()

        if naam and email:
            nieuwe_vrijwilliger = Vrijwilliger(
                naam=naam,
                email=email,
                telefoon=telefoon,
                motivatie=motivatie
            )

            db.session.add(nieuwe_vrijwilliger)
            db.session.commit()

        return redirect(url_for("vrijwilligers"))

    return render_template("vrijwilligers.html")


if __name__ == "__main__":
    app.run(debug=True)
