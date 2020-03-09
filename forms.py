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