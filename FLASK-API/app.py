from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    #get data from URL
    
    apikey = ""
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto" + "?apikey=" + apikey)

    #transform to JSON format (simmilar to nested dictionary)
    data = response.json()

    #access front_default
    img = data["sprites"]["front_default"]
    img2 = data["sprites"]["other"]["official-artwork"]["front_shiny"]


    return render_template("index.html", poke_src = img, poke_src2 = img2)


if __name__ == "__main__":
    app.run()