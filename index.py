from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import os
import openAiSandbox

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

bootstrap = Bootstrap5(app)

csrf = CSRFProtect(app)

class BookForm(FlaskForm):
    book1 = StringField('Book 1:',
                       validators=[DataRequired(), Length(4, 64)]
                       )
    book2 = StringField('Book 2:',
                        validators=[DataRequired(), Length(4, 64)]
                        )
    book3 = StringField('Book 3:',
                        validators=[DataRequired(), Length(4, 64)]
                        )
    book4 = StringField('Book 4:',
                        validators=[DataRequired(), Length(4, 64)]
                        )
    book5 = StringField('Book 5:',
                        validators=[DataRequired(), Length(4, 64)]
                        )
    submit = SubmitField('Submit')

system_message = f"""
    The user has read a few books recently and wants to discover \ 
    new books to read next.
    You need to suggest a list of books for the user \ 
    that are similar or related to the style and theme of the books \ 
    they have recently read.
    Output the list of books in bulleted items, describing the title \ 
    of the book, the authors and a very brief (one sentence long) description \
    of why you chose each specific book.
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    form = BookForm()
    names = []

    if form.validate_on_submit():
        names = [form.book1.data,
                 form.book2.data,
                 form.book3.data,
                 form.book4.data,
                 form.book5.data]
        completion = openAiSandbox.get_completion(
            [
                {"role": "system",
                "content": system_message},
                {"role": "assistant",
                 "content": f"""
                    The user has recently read these 5 books: \
                    {form.book1.data},
                    {form.book2.data},
                    {form.book3.data},
                    {form.book3.data},
                    {form.book4.data},
                """
                },
                {"role": "user",
                "content": "List 10 books I'd like to read next" },
            ]
        )
        return render_template('results.html', completion=completion)
    return render_template('index.html', form=form, message="")
