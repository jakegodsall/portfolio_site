from django.shortcuts import render
from .models import Project, Skill


# View to handle displaying the portfolio page
def portfolio(request):
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