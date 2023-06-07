from flask import Flask, render_template

app = Flask(__name__)

# Sample article data
articles = [
    {
        'title': 'Game Review 1',
        'summary': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    },
    {
        'title': 'Game Review 2',
        'summary': 'Nulla ultricies nulla id risus tristique sollicitudin.',
    },
    {
        'title': 'Game Review 3',
        'summary': 'Praesent vitae metus vitae est lobortis vulputate.',
    }
]

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
