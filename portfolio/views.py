import os

from django.conf import settings
from django.shortcuts import render, redirect
from .models import Project, Skill
from .forms import ContactForm

from django.core.mail import send_mail


# View to handle displaying the portfolio page
def portfolio(request):
    # POST REQUEST FOR EMAIL FORM
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            user_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Name: {name}\nEmail: {user_email}\n\n{message}"

            send_mail(
                subject,
                full_message,
                user_email,
                [settings.RECIPIENT_EMAIL],
                fail_silently=False
            )
            print("FORM DATA IS VALID")
            return redirect('confirmation')
        else:
            print("FORM DATA IS NOT VALID")
    else:
        form = ContactForm()

    # GET REQUESTS

    # Get all skills to display in skills section
    skills = Skill.objects.filter(is_for_skills_section=True)[:9]
    projects = Project.objects.all()

    # Render the portfolio page with projects, skills, and the contact form
    return render(request, 'portfolio/index.html', {
        'skills': skills,
        'projects': projects,
        'contact_form': form
    })


def about(request):
    if request.method == 'GET':
        return render(request, 'portfolio/about.html')


def confirmation(request):
    return render(request, 'portfolio/confirmation.html')