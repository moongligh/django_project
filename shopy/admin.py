from django.contrib import admin

# --- [추가 import 부분] --- #
from .models import Community, QNA, TipNknowhow, Comment
admin.site.register(Community)
admin.site.register(QNA)
admin.site.register(TipNknowhow)
admin.site.register(Comment)
