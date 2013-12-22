from flask import render_template, request, Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

application = Flask(__name__, static_folder='static')
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://saltosaurus:WnIh2rnmd@saltosaurus.codvopu4ldja.us-west-2.rds.amazonaws.com:3306/db'
db = SQLAlchemy(application)

application.debug=True

# An article
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    contents = db.Column(db.Text)
    pub_date = db.Column(db.Date)
    comments = db.relationship('Comment', backref = 'article', lazy = 'dynamic')
    
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.pub_date = datetime.now()
    
    # Make sure if we view it as an object we get the article title
    def __repr__(self):
        return self.title
    
    # Checks if the article was written in the last week: returns True if it was
    def was_written_recently(self):
        return self.pub_date >= datetime.now() - datetime.timedelta(days=7)


# A comment on an article
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    contents = db.Column(db.Text)
    author = db.Column(db.String(80))
    pub_date = db.Column(db.DateTime)
    
    # If viewed as an object, show author of comment
    def __repr__(self):
        return self.author
    
    def __init__(self, author, contents, article_id):
        self.author = author
        self.contents = contents
        self.article_id = article_id
        self.pub_date = datetime.now()

@application.route('/')
@application.route('/index')
@application.route('/index.html')
def index():
    #latest_article_list = Article.query.order_by(Article.pub_date.desc()).all()
    return "Hello world!"
#return render_template("index.html", latest_article_list=latest_article_list)

@application.route('/articles')
@application.route('/articles.html')
def articles():
    latest_article_list = Article.query.order_by(Article.pub_date.desc()).all()
    num_articles = len(latest_article_list)
    latest_article_list = latest_article_list[:5]
    comments_list = Comment.query.order_by(Comment.id).all()
    return render_template('articles.html', latest_article_list=latest_article_list, comments_list=comments_list, num_articles=num_articles)

@application.route('/articles/<int:article_id>')
def article(article_id):
    article = Article.query.get_or_404(article_id)
    comments_list = Comment.query.order_by(Comment.id.desc()).filter_by(article_id=article_id).all()[:5]
    
    return render_template('article.html', article=article, comments_list=comments_list)

@application.route('/projects')
@application.route('/projects.html')
def projects():
    return render_template('projects.html')

@application.route('/faq')
@application.route('/faq.html')
def faq():
    return render_template('faq.html')

@application.route('/resume')
def resume():
    return render_template('resume.pdf')

@application.route('/newComment', methods=['POST'])
def newComment():
    articleID = request.form['article_id']
    author = request.form['author']
    contents = request.form['comment']
    comment = Comment(author, contents, articleID)
    db.session.add(comment)
    db.session.commit()
    return ""

if __name__ == "__main__":         
    application.run(host='0.0.0.0',debug=True)
