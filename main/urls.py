from django.urls import path
from main.views import (
    show_main,
    show_experience,
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
    path("experience/", show_experience, name="show_experience"),
    path("skills/", show_skills, name="show_skills"),
    
    path("skills/add/", create_skill, name="create_skill"),
    path("skills/<int:skill_id>/delete/", delete_skill, name="delete_skill"),
    
    path("api/skills/", get_skills_json, name="get_skills_json"),
    
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<int:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<int:id>/", show_json_by_id, name="show_json_by_id"),
]