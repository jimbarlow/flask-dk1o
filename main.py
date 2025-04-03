from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("https://www.zeffy.com/ticketing/30404bdc-37d5-43a4-97b8-735c23c8de3a")
    # return render_template('home.html')

if __name__ == "__main__":
  app.run()
