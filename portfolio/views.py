import os

from django.conf import settings
from django.shortcuts import render, redirect
from .models import Project, Skill
from .forms import ContactForm

from django.core.mail import send_mail


# View to handle displaying the portfolio page
def portfolio(request):
    # POST REQUEST FOR FORM
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Name: {name}\nEmail: {email}\n\n{message}"

            send_mail(
                subject,
                full_message,
                email,
                [settings.RECIPIENT_EMAIL]
            )

            return redirect('confirmation')
        else:
            print("FORM DATA IS NOT VALID")
    else:
        form = ContactForm()

    # GET REQUESTS

    # Get the skill ID from the query parameters for filtering projects
    skill_id = request.GET.get('skill')
    # Filter projects by the selected skill if provided, otherwise get all projects
    if skill_id:
        projects = Project.objects.filter(skills__id=skill_id)
    else:
        projects = Project.objects.all()

    # Get all skills to display in skills section
    skills = Skill.objects.all()

    # Render the portfolio page with projects, skills, and the contact form
    return render(request, 'portfolio/index.html', {
        'skills': skills,
        'projects': projects,
        'contact_form': form
    })


def confirmation(request):
    return render(request, 'portfolio/confirmation.html')