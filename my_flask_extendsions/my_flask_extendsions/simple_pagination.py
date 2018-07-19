"""http://flask.pocoo.org/snippets/44/
Unless you are using JavaScript to dynamically load more contents pagination is a 
neat concept to structure many items of information 
into multiple pages. The idea is that if you have 100 items you show 20 
per page and have 5 pages in total then.
"""

from math import ceil


class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num


"""
URLs and Views
So how do you declare URLs and views when using Pagination? 
The Werkzeug routing system which Flask use supports this nicely 
with route level defaults. 
You specify a “default” for page 1 for the bare URL and provide an integer wildcard 
for other pages:
"""                







