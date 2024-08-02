import os

from django.shortcuts import render
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
            message = form.cleaned_data['message']

            send_mail(
                f"Message sent from {name}",
                message,
                email,
                [os.getenv('CONTACT_EMAIL_ADDRESS')]
            )
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
    })