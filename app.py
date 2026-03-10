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
    telefoon = db.Column(db.String(50))
    motivatie = db.Column(db.Text)


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

        print("POST ontvangen")
        print("Naam:", naam)
        print("Email:", email)
        print("Telefoon:", telefoon)
        print("Motivatie:", motivatie)

        try:
            if naam and email:
                nieuwe_vrijwilliger = Vrijwilliger(
                    naam=naam,
                    email=email,
                    telefoon=telefoon,
                    motivatie=motivatie
                )

                db.session.add(nieuwe_vrijwilliger)
                db.session.commit()

                print("OPGESLAGEN IN DATABASE")

        except Exception as e:
            db.session.rollback()
            print("DATABASE FOUT:", e)

        return redirect(url_for("vrijwilligers"))

    return render_template("vrijwilligers.html")


# Test route om database te controleren
@app.route("/test-insert")
def test_insert():
    try:
        test = Vrijwilliger(
            naam="Test Naam",
            email="test@test.nl",
            telefoon="0612345678",
            motivatie="Test motivatie"
        )

        db.session.add(test)
        db.session.commit()

        return "Test opgeslagen in database!"
    except Exception as e:
        db.session.rollback()
        return f"Database fout: {e}"


if __name__ == "__main__":
    app.run(debug=True)
