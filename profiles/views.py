from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.
# def store_file(file):
#     with open("tmp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/profiles.html"
    context_object_name = "profiles"

class CreateProfileView(CreateView):
    model = UserProfile
    template_name = "profiles/create_profile.html"
    fields = "__all__"
    success_url = "/profiles"

    # def get(self, request):
    #     form = ProfileForm()
    #     return render(request, "profiles/create_profile.html", {
    #         "form": form
    #     })

    # def post(self, request):
    #     create_form = ProfileForm(request.POST, request.FILES)
    #     # store_file(request.FILES["image"])
    #     if create_form.is_valid():
    #         profile = UserProfile(image=request.FILES["image"])
    #         profile.save()
    #         return HttpResponseRedirect("/profiles")            

    #     return render(request, "profiles/create_profile.html", {
    #         "form": create_form
    #     })
