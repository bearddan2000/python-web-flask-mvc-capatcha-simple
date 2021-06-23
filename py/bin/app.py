from flask import Flask, render_template, request
import string
import random
from PIL import Image, ImageDraw, ImageFont

# Create Flask's `app` object
app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)

def id_generator(size=5, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

@app.route('/', methods=['GET'])
def getCapatcha():
    return render_template(
    "index.html",
    capatcha=id_generator()
    )

@app.route('/', methods=['POST'])
def postCapatcha():
    info = request.form
    provided = info.get('provided', '')
    guess = info.get('guess', '')
    return render_template(
    "index.html",
    msg='Match is %s' % provided == guess,
    capatcha=id_generator()
    )

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
