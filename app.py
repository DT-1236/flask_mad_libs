from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['Secret_Key'] = "oh-so-secret"

# debug = DebugToolbarExtension(app)


@app.route('/')
def homepage():
    '''Renders a homepage'''

    return render_template('formpage.html', prompts=story.prompts)


@app.route('/story', methods=["POST"])
def story_page():
    '''Renders a story after filling a form out'''

    answers = request.form

    return render_template(
        'storypage.html', story_template=story.generate(answers))
