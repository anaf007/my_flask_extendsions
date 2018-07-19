"""Generating Feeds with Flask
Atom is an easy way to let other people subscribe to changes on your website. For example people can subscribe to the recent additions of content on your website.

Assuming you already have a way to access that information (database query for most recent blog posts for example) generating an Atom feed is easy as pie.

All you need is the AtomFeed class from the Werkzeug contrib package (this is there for you in any Flask application). Just create a view function like this:

url:http://flask.pocoo.org/snippets/10/
"""

from urlparse import urljoin
from flask import request
from werkzeug.contrib.atom import AtomFeed

from my_flask_extendsions.public.models import Article


def make_external(url):
    return urljoin(request.url_root, url)


@app.route('/recent.atom')
def recent_feed():
    feed = AtomFeed('Recent Articles',
                    feed_url=request.url, url=request.url_root)
    articles = Article.query.order_by(Article.pub_date.desc()) \
                      .limit(15).all()
    for article in articles:
        feed.add(article.title, unicode(article.rendered_text),
                 content_type='html',
                 author=article.author_name,
                 url=make_external(article.url),
                 updated=article.last_update,
                 published=article.published)
    return feed.get_response()

"""
<link href="{{ url_for('recent_feed') }}"
      rel="alternate"
      title="Recent Changes" 
      type="application/atom+xml">

"""