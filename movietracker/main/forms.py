from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField('search_text', validators=[DataRequired()])
    submit = SubmitField('search')


class ReviewForm(FlaskForm):
    review = StringField('review_text', validators=[DataRequired()], render_kw={'style': 'width: 80%; font-size:2.5vh;'})
    post_review = SubmitField('post')

