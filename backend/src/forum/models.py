from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/%Y/%m/%D/")
    post_state = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)


class Post_rating(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
    )


class Comment_answer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    comment = models.OneToOneField(
        Comment,
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=300)


class Comment_rating(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    comment = models.OneToOneField(
        Comment,
        on_delete=models.CASCADE,
    )
    comment = models.OneToOneField(
        Comment_answer,
        on_delete=models.CASCADE,
    )
