from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
import requests
import os
from dice import Dice
from forms import DiceForm, SpellForm, MonsterForm, ClassForm


dnd_api_url = "https://www.dnd5eapi.co"
dice_bag = {"d20": 20, "d12": 12, "d10": 10, "d8": 8, "d6": 6, "d4": 4}


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = os.urandom(26)


@app.route("/", methods=["POST", "GET"])
def roll():

    dice_roller = DiceForm()
    spell_book = SpellForm()
    if request.method == "POST":
        die = dice_roller.d.data or 20
        rolls = dice_roller.rolls.data or 0

        try:
            die = int(die)
            rolls = int(rolls)
        except ValueError:
            flash("Pick an actual number")
        else:
            die = Dice(die)
            rolls = die.dice_roll(rolls)
            total = rolls[1]
            each = [str(x) for x in rolls[0]]
            highest = max(rolls[0])
            lowest = min(rolls[0])
            return render_template("dice-roller.html",
                                   dice_roller=dice_roller,
                                   rolls=rolls,
                                   each=each,
                                   total=total,
                                   max=highest,
                                   min=lowest)
    return render_template("dice-roller.html", dice_roller=dice_roller)


@app.route("/spells", methods=["POST", "GET"])
def spells():
    spell_book = SpellForm()
    if request.method == "POST":
        spell = spell_book.select.data
        spell = requests.get(f"{dnd_api_url}/api/spells/{spell}").json()
        # for x in spell.items():
        #     flash(x)

        return render_template("spell-book.html",
                               spell_book=spell_book,
                               spell=spell)
    return render_template("spell-book.html", spell_book=spell_book)


@app.route("/monsters", methods=["POST", "GET"])
def monsters():
    monster_list = MonsterForm()
    if request.method == "POST":
        monster = monster_list.select.data
        monster = requests.get(f"{dnd_api_url}/api/monsters/{monster}").json()
        # for x in monster.items():
        #     flash(x)

        return render_template("monsters.html",
                               monster_list=monster_list,
                               monster=monster)
    return render_template("monsters.html", monster_list=monster_list)


@app.route("/classes", methods=["POST", "GET"])
def classes():
    classes_list = ClassForm()
    if request.method == "POST":
        classes = classes_list.select.data
        classes = requests.get(f"{dnd_api_url}/api/classes/{classes}").json()
        for x in classes.items():
            flash(x)
        return render_template("classes.html",
                               classes_list=classes_list,
                               classes=classes)
    return render_template("classes.html", classes_list=classes_list)


if __name__ == '__main__':
    app.run(debug=True)


