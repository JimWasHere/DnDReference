from flask_wtf import FlaskForm
from wtforms import IntegerField, FieldList, SubmitField, Label, SelectField, FormField
import requests

dnd_api_url = "https://www.dnd5eapi.co"


class DiceForm(FlaskForm):
    d = SelectField("Which die do you want to roll?", choices=[(20, "d20"),
                                                               (12, "d12"),
                                                               (10, "d10"),
                                                               (8, "d8"),
                                                               (6, "d6"),
                                                               (4, "d4")])
    rolls = IntegerField("How many rolls?")
    submit = SubmitField("Roll")


spell_list = [(0, 'Select')]
spells = requests.get(f"{dnd_api_url}/api/spells").json()["results"]
for spell in spells:
    spell_list.append((spell['index'], spell['name']))
# print(spell_list)


class SpellForm(FlaskForm):
    select = SelectField("Spells", choices=[spell_list][0])
    submit = SubmitField("Cast")



