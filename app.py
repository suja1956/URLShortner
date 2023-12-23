from flask import Flask, render_template, request, redirect
import random
import string
app = Flask(__name__)
shortened_url = {}

def shortenUrl():
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(6))
    return short_url



@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        long_url = request.form["url"]
        short_url = shortenUrl()
        while short_url in shortened_url:
            short_url = shortenUrl()
        shortened_url[short_url] = long_url
        print(shortened_url)
        return f"Shortened URL: {request.url_root}tinyurl?url={short_url}"
    
    return render_template("index.html")


@app.route("/tinyurl")
def redirect_url():
    short_url = request.args.get('url')
    print(short_url)
    print(shortened_url)
    long_url = shortened_url.get(short_url)
    print(long_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL Not found : 404" 


if __name__=="__main__":
    app.run(debug=True)