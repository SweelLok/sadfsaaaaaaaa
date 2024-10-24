from flask import Flask, render_template
from static.baza import titles, pizzas

app = Flask(__name__)

@app.get("/")
def home_page():
    return render_template("index.html",
                          menu="Меню",
                          title="Oderman",
                          number="Номер телефону: +1 234 567 890")

@app.get("/menu/")
def menu_page():
    context = {
        "titles": titles,
        "back_button": "Повернутися на головну сторінку",
        "pizzas": pizzas
    }
    return render_template("menu.html", **context)


if __name__ == "__main__":
  app.run(port=5050, debug=True, )
