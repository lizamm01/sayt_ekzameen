from django.db import models

class Profile(models.Model):
    fullname = models.CharField(max_length=200)
    profession = models.CharField(max_length=100, default="Backend")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    about = models.TextField()
    experience = models.CharField(max_length=50, default="0 yil")
    resume = models.FileField(upload_to="resumes/", null=True, blank=True)

    def __str__(self):
        return self.fullname


class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    platform = models.CharField(max_length=50)   # masalan: Telegram, Instagram
    url = models.URLField()

    def __str__(self):
        return self.platform


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
