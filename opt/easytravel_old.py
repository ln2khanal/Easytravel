from travel import Travel
import settings
import flask

app = flask.Flask(__name__)
app.secret_key = settings.secret_key    
app.add_url_rule("/",view_func=Travel.as_view("easytravel"),methods=["POST","GET"])
app.run(debug=True,host="0.0.0.0",port=5055)
