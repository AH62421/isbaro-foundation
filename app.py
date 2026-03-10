from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/vrijwilligers", methods=["GET","POST"])
def vrijwilligers():

    if request.method == "POST":

        voornaam = request.form["voornaam"]
        achternaam = request.form["achternaam"]
        telefoon = request.form["telefoon"]
        motivatie = request.form["motivatie"]

        print("Nieuwe vrijwilliger:")
        print(voornaam, achternaam)
        print(telefoon)
        from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/vrijwilligers", methods=["GET","POST"])
def vrijwilligers():

    if request.method == "POST":

        voornaam = request.form["voornaam"]
        achternaam = request.form["achternaam"]
        telefoon = request.form["telefoon"]
        motivatie = request.form["motivatie"]

        with open("namen.txt", "a", encoding="utf-8") as file:
            file.write(f"Voornaam: {voornaam}\n")
            file.write(f"Achternaam: {achternaam}\n")
            file.write(f"Telefoon: {telefoon}\n")
            file.write(f"Motivatie: {motivatie}\n")
            file.write("-----\n")

        return redirect(url_for("vrijwilligers"))

    return render_template("vrijwilligers.html")


if __name__ == "__main__":
    app.run(debug=True)
