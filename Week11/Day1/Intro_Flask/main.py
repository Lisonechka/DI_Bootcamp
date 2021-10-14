from flask import Flask, render_template, render_template_string

app = Flask(__name__)


# default-page
@app.route('/')
def home():
    return 'hello world'


@app.route('/<username>')
def index(username):
    html = '''
    <html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, {{firstname}} {{lastname}}!</h1>
    </body>
</html>'''

    html = render_template_string(html, firstname="Rick", lastname="Sanchez")

    return html


# about-page
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
