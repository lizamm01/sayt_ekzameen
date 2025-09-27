from django.shortcuts import render, redirect
from .models import Profile, Project, Technology, SocialLink
from .models import ContactMessage
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    profile = Profile.objects.first()
    projects = Project.objects.filter(selected=True)
    technologies = Technology.objects.all()
    social_links = SocialLink.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect("index")

    context = {
        "profile": profile,
        "projects": projects,
        "technologies": technologies,
        "social_links": social_links,
    }
    return render(request, "index.html", context)




#email student teacher
