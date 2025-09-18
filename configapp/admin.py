from django.contrib import admin
from .models import Profile, Technology, Project, SocialLink, ContactMessage

admin.site.register(Profile)
admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(SocialLink)
admin.site.register(ContactMessage)
