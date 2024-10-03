from django.contrib import admin

#importanto Topic criado em models
from app.models import Topic, Entry

# registra no site na page do admin o topic criado em models
admin.site.register(Topic)

admin.site.register(Entry)
