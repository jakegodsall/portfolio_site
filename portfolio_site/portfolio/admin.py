from django.contrib import admin
from .models import Skill, Project

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Skill, SkillAdmin)
admin.site.register(Project)
