from django.contrib import admin
from .models import Skill, Project


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_for_skills_section')
    search_fields = ('name',)


admin.site.register(Skill, SkillAdmin)
admin.site.register(Project)