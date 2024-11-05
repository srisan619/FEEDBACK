from django import forms 

class ReviewForm(forms.Form):
    username = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "Your name should not be empty",
        "max_length": "Please enter the shorter name"
    })
    review_text = forms.CharField(label="Your feedback", max_length=200, widget=forms.Textarea)
    rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)
    # captcha_answer = forms.IntegerField(label="2 + 2", label_suffix=" =")