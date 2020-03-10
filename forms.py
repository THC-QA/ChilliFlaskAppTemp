from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length
class recipe_form(FlaskForm):
    recipe_name = StringField('Recipe Name',
        validators = [
            DataRequired(),
            Length(min=4, max=50)
            ]
        )
    recipe_method = StringField('Recipe Instructions',
        validators = [
            DataRequired(),
            Length(min=10, max=10000)
            ]
        )
    submit = SubmitField("Post Recipe")
class ingredient_form(FlaskForm):
    ingredient_name = StringField("Ingredient Name",
        validators = [
            DataRequired(),
            Length(min=4, max=50)
            ]
        )
    ingredient_type = SelectField(u"Ingredient Type",
        choices = [
            ("Chilli", "Chilli"),
            ("Vegetable", "Vegetable"),
            ("Fruit", "Fruit"),
            ("Herb", "Herb"),
            ("Spice", "Spice"),
            ("Liquid", "Liquid")
        ])
    submit = SubmitField("Post Ingredient")
class update_form(FlaskForm):
    def __init__(self,r_names, i_names):
        self.r_names = r_names
        self.i_names = i_names
    table_selection = SelectField(u"Select a Table",
        choices = [
            ("RECIPES", "recipes"),
            ("INGREDIENTS", "ingredients"),
        ])
    if table_selection == "recipes":
        name = SelectField(u"Select a Recipe", choices=[]
        for names in self.r_names:
            choices.append((names, str(names))))
        new_name = StringField('New Name',
        validators = [
            DataRequired(),
            Length(min=4, max=50)
            ]
        )
    elif table_selection == "ingredients":
        name = SelectField(u"Select an Ingredient", choices=[]
        for names in self.i_names:
            choices.append((names, str(names))))
        new_name = StringField("Ingredient Name",
        validators = [
            DataRequired(),
            Length(min=4, max=50)
            ]
        )
    submit = SubmitField("Update Records")