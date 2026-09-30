from django.urls import path
from main.views import (
    register,
    login_user,
    logout_user,
    show_main,
    show_experience,
    create_experience,
    update_experience,
    delete_experience,
    get_experience_json,
    star_experience,
    create_experience_ajax,
    show_skills,
    create_skill,
    delete_skill,
    get_skills_json,
    show_xml,
    show_json,
    show_xml_by_id,
    show_json_by_id,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("experience/<uuid:id>/edit/", update_experience, name="update_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),

    path("skills/", show_skills, name="show_skills"),
    path("skills/add/", create_skill, name="create_skill"),
    path("skills/<uuid:skill_id>/delete/", delete_skill, name="delete_skill"),
    path("api/skills/", get_skills_json, name="get_skills_json"),
    path("experience/<uuid:id>/star/", star_experience, name="star_experience"),

    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<uuid:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<uuid:id>/", show_json_by_id, name="show_json_by_id"),
]