from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    id_user
    title
    text 
    image   
    post_state
    created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    id_user
    id_post
    text 
    created = models.DateTimeField(auto_now_add=True)

class Post_rating(models.Model):
    id_post
    id_user 

class Comment_rating(models.Model):
    id_user
    id_comment 
    id_answer

class Comment_answer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id_user
    id_comment
    text
