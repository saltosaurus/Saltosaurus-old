from flask import render_template
from app import app
from models import Article, Comment


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    latest_article_list = Article.query.order_by(Article.pub_date)[:3]
    comments_list = Comment.query.order_by(Comment.id) # Linear search is gross
    
    return render_template("index.html", latest_article_list=latest_article_list, comments_list=comments_list)

@app.route('/articles')
@app.route('/articles.html')
def articles():
    latest_article_list = Article.query.order_by(Article.pub_date)[:10]
    comments_list = Comment.query.order_by(Comment.id)
    
    return render_template('articles.html', latest_article_list=latest_article_list, comments_list=comments_list)

