from flask import Flask, render_template, request

app = Flask(__name__)

students = []


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        usn = request.form["usn"]
        platform = request.form["platform"]
        problems = int(request.form["problems"])
        score = float(request.form["score"])

        if score >= 80:
            performance = "Excellent"
        elif score >= 60:
            performance = "Good"
        elif score >= 40:
            performance = "Average"
        else:
            performance = "Needs Improvement"

        student = {
            "name": name,
            "usn": usn,
            "platform": platform,
            "problems": problems,
            "score": score,
            "performance": performance
        }

        students.append(student)

    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)