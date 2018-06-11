from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form action="/rotate" method="post">
        <label>
            Rotate by:
            <input type="text" name="rot"/>
        </label>
        <textarea name="text">
        {0}
        </textarea>
        <input type="submit" value="Submit"/>
    </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    pass

@app.route("/")
def index():
    return form


app.run()