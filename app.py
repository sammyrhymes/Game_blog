from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Database Initialization
conn = sqlite3.connect('blog.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, author TEXT, date TEXT)')


# Route for Creating New Article
@app.route('/create', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        date = request.form['date']

        # Insert new article into the database
        conn = sqlite3.connect('blog.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO articles (title, content, author, date) VALUES (?, ?, ?, ?)',
                    (title, content, author, date))
        conn.commit()
        cur.close()

        return redirect(url_for('confirmation'))

    return render_template('create.html')

# Confirmation Page
@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


@app.route('/article/<id>')
def view_article(id):
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM articles where id = ?', id)
    article = cur.fetchone()
    cur.close()
    return render_template('view_article.html',article=article, id=id)

# Home Page - Displaying Articles
@app.route('/')
def home():
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM articles')
    articles = cur.fetchall()
    cur.close()
    return render_template('home.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
