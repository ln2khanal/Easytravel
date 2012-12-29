from flask import Flask, render_template, request
from travel import compute
app = Flask(__name__)


@app.route('/travel',methods=["POST"])
def add_numbers():
    """Compute the shortest path which is traffic jam free too..."""
    a = request.form.get('a')#, 0, type=str)
    b = request.form.get('b')#, 0, type=str)
    print "a="+a+"b="+b
    return (compute(a, b))



@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)