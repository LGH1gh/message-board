from django.contrib import admin
from .models import User
from .models import Board
from .models import Agree
from .models import Comment
# Register your models here.
admin.site.register(User)
admin.site.register(Board)
admin.site.register(Agree)
admin.site.register(Comment)