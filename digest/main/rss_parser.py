import feedparser
from .models import *


def pull_feed(user_id, posts_limit=5):
    user = User.objects.get(user_id=user_id)
    categories = [item.name for item in user.topics.all()]
    feeds = [sub for sub in user.subscriptions.all()]
    posts = []
    for f in feeds:
        feed = feedparser.parse(f.link)
        counter = 0
        for i in range(len(feed)):
            if feed['entries'][i].category in categories:
                posts.append({
                    'title': feed['entries'][i].title,
                    'description': feed['entries'][i].summary,
                    'link': feed['entries'][i].link,
                    'category': feed['entries'][i].category,
                    'subscription': f
                })
                counter += 1
            if counter == posts_limit:
                break
    d = Digest.objects.create(user=user)
    for post in posts:
        p = Post.objects.create(title=post['title'], description=post['description'],
                                link=post['link'], category=Topic.objects.get(name=post['category']),
                                subscription=post['subscription'])
        d.posts.add(p)
    data = {post.post_id: post.description for post in d.posts.all()}
    return {"data": data}