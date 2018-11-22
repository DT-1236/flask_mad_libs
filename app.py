from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['Secret_Key'] = "oh-so-secret"

# debug = DebugToolbarExtension(app)
story = None


@app.route("/")
def homepage():
    """Displays page for selecting Madlib"""
    madlibs = [x.title for x in stories]
    return render_template("madlib_selector.html", madlibs=madlibs)


@app.route('/storybuilding')
def storybuilding():
    '''Renders a homepage'''
    title = request.args.get('madlib')
    global story
    story = next(x for x in stories if x.title == title)
    return render_template('formpage.html', prompts=story.prompts)


@app.route('/story', methods=["POST"])
def story_page():
    '''Renders a story after filling a form out'''

    answers = request.form

    return render_template(
        'storypage.html', story_template=story.generate(answers))
