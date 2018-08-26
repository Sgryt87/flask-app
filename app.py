from flask import Flask, request, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Author1',
        'title': 'title1',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae consectetur hic molestias? Ab blanditiis cupiditate debitis dicta doloribus eaque esse expedita laborum libero nam neque officia quo, saepe soluta, vero.',
        'date_posted': 'Jan 1, 2000'
    },

    {
        'author': 'Author2',
        'title': 'title2',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae consectetur hic molestias? Ab blanditiis cupiditate debitis dicta doloribus eaque esse expedita laborum libero nam neque officia quo, saepe soluta, vero.',
        'date_posted': 'Jan 2, 2002'
    }

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
