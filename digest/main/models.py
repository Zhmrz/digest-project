from django.db import models


class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=50)
    link = models.CharField('link', max_length=50)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField('name', max_length=50)

    def __str__(self):
        return self.name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=50)
    subscriptions = models.ManyToManyField(Subscription)
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.name


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.TextField('title')
    link = models.CharField('link', max_length=150)
    description = models.TextField('description')
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    category = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " - " + self.category.name


class Digest(models.Model):
    digest_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)