import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from main.models import Experience, Skill
from main.forms import SkillForm, ExperienceForm


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Zidane Ahdina Putra",
        "form": form,
    }
    return render(request, "register.html", context)


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Zidane Ahdina Putra",
        "npm": "2506583953",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "only a boy who likes playing visual novel games, watching anime, and reading book. "
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def get_experience_json(request):
    experiences = Experience.objects.all().order_by("-started_at")
    experiences_json = serializers.serialize(
        "json", 
        experiences, 
        use_natural_foreign_keys=True,
        use_natural_primary_keys=True
    )
    return HttpResponse(experiences_json, content_type="application/json")


def show_experience(request):
    experience_list = Experience.objects.all().order_by("-started_at")
    user_is_editor = is_editor(request.user)

    context = {
        "name": "Zidane Ahdina Putra",
        "experience_list": experience_list,
        "is_editor": user_is_editor,
    }
    return render(request, "experience.html", context)


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Zidane Ahdina Putra",
        "form": form,
    }
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def update_experience(request, id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Zidane Ahdina Putra",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def delete_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
    return redirect("main:show_experience")


def get_skills_json(request):
    category_query = request.GET.get("category", "").strip()
    skills = Skill.objects.all()
    if category_query:
        skills = skills.filter(category__icontains=category_query)
    skills_json = serializers.serialize(
        "json", 
        skills, 
        use_natural_foreign_keys=True,
        use_natural_primary_keys=True
    )
    return HttpResponse(skills_json, content_type="application/json")


def show_skills(request):
    category_query = request.GET.get("category", "").strip()
    skills = Skill.objects.all()
    if category_query:
        skills = skills.filter(category__icontains=category_query)

    context = {
        "name": "Zidane Ahdina Putra",
        "skill_list": skills,
        "category_query": category_query,
    }
    return render(request, "skills.html", context)


@login_required(login_url="/login/")
def create_skill(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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


@login_required(login_url="/login/")
def delete_skill(request, skill_id):
    if not request.user.is_superuser:
        raise PermissionDenied

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
    return HttpResponse(
        serializers.serialize("json", data, use_natural_foreign_keys=True, use_natural_primary_keys=True), 
        content_type="application/json"
    )


def show_xml_by_id(request, id):
    data = Skill.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Skill.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", data, use_natural_foreign_keys=True, use_natural_primary_keys=True), 
        content_type="application/json"
    )


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Zidane Ahdina Putra",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


@login_required(login_url="/login/")
def star_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
            messages.info(request, "Star berhasil dihapus.")
        else:
            experience.starred_by.add(request.user)
            messages.success(request, "Pengalaman berhasil di-star!")
    return redirect("main:show_experience")

def is_editor(user):
    return user.is_authenticated and user.groups.filter(name='Editor').exists()