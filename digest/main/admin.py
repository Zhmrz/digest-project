from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Subscription)
admin.site.register(Post)
admin.site.register(Digest)
admin.site.register(Topic)