from django.shortcuts import render, HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView

# Create your views here.
class ReviewView(CreateView):
    form_class = ReviewForm
    model = Review
    template_name = "reviews/review.html"
    success_url = "/thank-you"


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
 

'''
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()    
        return render(request, "reviews/review.html",{
            "form": form
        })
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request, "reviews/review.html",{
         "form": form
        })
    
'''

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
  

# class ThanksView(View):
#     def get(self, request):
#         return render(request, "reviews/thank_you.html") 

# def thank_you(request):
    # return render(request, "reviews/thank_you.html") 

class ThanksView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Review is created. Thank you!"
        return context
    

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data
    

class ShowReviewView(DetailView):
    template_name = "reviews/show_review.html"
    model = Review

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["review"] = Review.objects.get(pk=kwargs["id"])
    #     return context
    