from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("https://www.zeffy.com/en-US/ticketing/hart-county-humane-society-inc-memberships")
    # return render_template('home.html')

if __name__ == "__main__":
  app.run()
