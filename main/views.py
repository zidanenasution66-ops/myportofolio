from django.shortcuts import render

from main.models import Experience, Skill


def show_main(request):
    context = {
        "name": "Zidane Ahdina Putra",
        "npm": "2506583953",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "only a boy who likes playing visual novel games, watching anime, and reading book. "
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Zidane Ahdina Putra",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skills(request):
    context = {
        "name": "Zidane Ahdina Putra",
        "skill_list": Skill.objects.all(),
    }
    return render(request, "skills.html", context)