from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers

from main.models import Experience, Skill
from main.forms import SkillForm


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


def get_skills_json(request):
    category_query = request.GET.get("category", "").strip()
    skills = Skill.objects.all()
    if category_query:
        skills = skills.filter(category__icontains=category_query)
    skills_json = serializers.serialize("json", skills)
    return HttpResponse(skills_json, content_type="application/json")


def show_skills(request):
    json_response = get_skills_json(request)
    skills = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    skills = [skill.object for skill in skills]
    category_query = request.GET.get("category", "").strip()

    context = {
        "name": "Zidane Ahdina Putra",
        "skill_list": skills,
        "category_query": category_query,
    }
    return render(request, "skills.html", context)


def create_skill(request):
    form = SkillForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Keahlian berhasil ditambahkan!")
        return redirect("main:show_skills")

    context = {
        "name": "Zidane Ahdina Putra",
        "form": form,
    }
    return render(request, "skills_form.html", context)


def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    if request.method == "POST":
        skill.delete()
        messages.success(request, "Keahlian berhasil dihapus!")
    return redirect("main:show_skills")


def show_xml(request):
    data = Skill.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Skill.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Skill.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Skill.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")