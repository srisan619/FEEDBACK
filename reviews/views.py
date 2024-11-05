from django.shortcuts import render, HttpResponseRedirect
from .forms import ReviewForm

# Create your views here.
def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/thank-you')
    form = ReviewForm()
    return render(request, "reviews/review.html",{
        "form": form
    })
    # if request.method == "POST":
    #     username = request.POST["username"]
    #     print(username)
    #     return HttpResponseRedirect('/thank-you')
    # else:
    #     return render(request, "reviews/review.html")
    
def thank_you(request):
    return render(request, "reviews/thank_you.html") 