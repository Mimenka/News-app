from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from models import News, Comment
from forms import NewsForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    news_list = News.query.order_by(News.pub_date.desc()).all()
    return render_template('index.html', news_list=news_list)

@main.route('/news/<int:news_id>')
def news_detail(news_id):
    news_item = News.query.get_or_404(news_id)
    comments = Comment.query.filter_by(news_id=news_id).order_by(Comment.pub_date.desc()).all()
    return render_template('post_detail.html', news_item=news_item, comments=comments)

@main.route('/add_comment/<int:news_id>', methods=['POST'])
def add_comment(news_id):
    news_item = News.query.get_or_404(news_id)
    comment_body = request.form.get('body')
    if comment_body:
        comment = Comment(news_id=news_id, body=comment_body)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('main.news_detail', news_id=news_id))

@main.route('/add_news', methods=['GET', 'POST'])
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        news = News(
            title=form.title.data,
            description=form.description.data,
            image_url=form.image_url.data
        )
        db.session.add(news)
        db.session.commit()
        flash('News added successfully!')
        return redirect(url_for('main.index'))
    return render_template('add_news.html', form=form)
@main.route('/delete_news/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    news = News.query.get_or_404(news_id)
    db.session.delete(news)
    db.session.commit()
    flash('News deleted successfully!')
    return jsonify({'message': 'News deleted'}), 200
