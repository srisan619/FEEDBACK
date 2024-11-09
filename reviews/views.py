from django.shortcuts import render, HttpResponseRedirect
from .forms import ReviewForm
# from .models import Review

# Create your views here.
def review(request):
    if request.method == "POST":
        #update review data
        # update_data = Review.objects.all(pk=1)
        # form = ReviewForm(request.POST, instance=update_date)
        #save new review data
        form = ReviewForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # review = Review(username=form.cleaned_data['username'], review_text=form.cleaned_data['review_text'], rating=form.cleaned_data['rating'])
            # review.save()
            form.save()
            return HttpResponseRedirect('/thank-you')
    else:
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