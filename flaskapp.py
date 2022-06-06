from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def index():
    t = requests.get('https://thingspeak.com/channels/1759197/fields/1/last.txt')
    h = requests.get('https://thingspeak.com/channels/1759197/fields/2/last.txt')
    temp_c_in = t.text
    hum_c_in = h.text
    return render_template("index.html", temp=temp_c_in, hum=hum_c_in)

if __name__ == "__main__":
    app.run(host='0.0.0.0')