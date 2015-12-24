from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

# Create your views here.
from .forms import ContactForm, SignUpForm

from .models import SignUp


def home(request):
    title = 'Sign Up Now'
    # if request.user.is_authenticated():
    #     title = "My Title %s" %request.user
    if request.method == "POST":
        print request.POST
    #add a form
    #form = SignUpForm()
    form = SignUpForm(request.POST or None) #if thre is post data send it to the form or not

    context = {
        "title" : title,
        "form" : form
    }

    if form.is_valid():
        #form.save()
        instance = form.save(commit = True) #False prevents the form from saving
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        # if not instance.full_name:
        #     instance.full_name = "Wen"
        # instance.save()
        context = {
            "title": "Thank you"
        }
        #print instance.email
        #print instance.timestamp

    if request.user.is_authenticated() and request.user.is_staff:
        queryset = SignUp.objects.all().order_by('-timestamp')
        #queryset = SignUp.objects.all().order_by('-timestamp').filter(email__icontains = "gmail")
        print(SignUp.objects.all().order_by('-timestamp').filter(email__iexact = "abc@gmail.com").count())
        context = {
            "queryset": queryset

        }

    return render(request, "home.html", context)

def contact(request):
    title = "Contact us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.iteritem():
        #     print key, value
        email = form.cleaned_data.get("email")
        full_name = form.cleaned_data.get("full_name")
        message = form.cleaned_data.get("message")
        # print email, message, full_name
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'otheremail@email.com']
        contact_message = "%s: %s via %s" %(full_name,
                                            message,
                                            email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  [to_email],
                  fail_silently=False)
    context = {
        "form":form,
        "title":title,
    }
    return render(request, "forms.html", context)