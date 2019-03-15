from django.contrib import admin
from .models import User, Post, Comment, Post_rating, Comment_answer, Comment_rating

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Post_rating)
admin.site.register(Comment_answer)
admin.site.register(Comment_rating)
