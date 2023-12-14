from flask import Flask, render_template, request
import smtplib
import random
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def sendOtp():
    global otp
    otp = random.randint(99999,1000000)
    email = "suja71449@gmail.com"
    receiver_email = request.form['email']
    subject = "OTP Verification"
    message = str(otp)+" is your verification code."
    text = f"Subject: {subject}\n\n{message}"
    server = smtplib. SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login (email, "dlnhwaurwfbsgrfm")
    server.sendmail(email, receiver_email, text)
    return render_template("verify.html")

@app.route("/verify",methods=["POST"])
def verify():
    otp_from_user = int(request.form['code'])
    print("this from user"+str(otp_from_user)+"and this is actual otp"+str(otp))
    if otp==otp_from_user:
        return render_template("landing.html")
    else:
        return render_template("error.html")



if __name__=="__main__":
    app.run(debug=True)