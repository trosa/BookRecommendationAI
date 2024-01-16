from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from flask_cors import CORS
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import os
import openAiSandbox

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

CORS(app, resources={r'/*': {'origins': '*'}})

bootstrap = Bootstrap5(app)

system_message = f"""
    The user has read a few books recently and wants to discover \ 
    new books to read next.
    You need to suggest a list of books for the user \ 
    that are similar or related to the style and theme of the books \ 
    they have recently read.
    Output the list in JSON format, describing the title \ 
    of the book, the authors and a very brief (one sentence long) description \
    of why you chose each specific book.
"""

@app.route('/books2', methods=['POST'])
def book_recoms2():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    response_object['books'] = 'Book Recommended!'
    return jsonify(response_object)

@app.route('/books', methods=['POST'])
def book_recoms():
    post_data = request.get_json()
    books_read = post_data['books']
    #print(post_data)
    completion = openAiSandbox.get_completion(
        [
            {"role": "system",
            "content": system_message},
            {"role": "assistant",
             "content": f"""
                The user has recently read these 5 books: \
                {books_read[0]},
                {books_read[1]},
                {books_read[2]},
                {books_read[3]},
                {books_read[4]},
            """
            },
            {"role": "user",
            "content": "List 10 books I'd like to read next" },
        ]
    )
    return completion
