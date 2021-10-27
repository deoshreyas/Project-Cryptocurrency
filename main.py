from flask import Flask, render_template, request, redirect
import smtplib, ssl


def message(receiver_name, name, email, message):
    return f"""
      Hi {receiver_name}!

      This is an email from the Crypto website! These are the details of the sender:
      
      Name: {name}
      Email: {email}
      Message: {message}  
      """


def email_person(name, email, _message):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "bansalaarav2007@gmail.com"
    password = "lgtxnfriwjkbypnu"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)  # Secure the connection
        server.login(sender_email, password)

        server.sendmail(sender_email, "shreyasdeo.k50@gmail.com",
                        message("Shreyas", name, email, _message))
        server.sendmail(sender_email, "bansalaarav2007@gmail.com",
                        message("Aarav", name, email, _message))
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/explore/')
def explore():
    return render_template("explore.html")


@app.route('/contact-us/', methods=["GET", "POST"])
def contactus():
    if request.method == "POST":
        full_name = request.form.get("full-name")
        email = request.form.get("email")
        message = request.form.get("message")
        email_person(full_name, email, message)
        return redirect("/")
    return render_template("contact_us.html")


@app.route("/meet-the-team/")
def meet_the_team():
    return render_template("meet-the-team.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)
