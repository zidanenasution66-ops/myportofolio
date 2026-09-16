from django.forms import ModelForm, Textarea, TextInput
from main.models import Skill


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            "category",
            "description",
        ]
        labels = {
            "category": "Kategori Keahlian",
            "description": "Deskripsi Keahlian",
        }
        widgets = {
            "category": TextInput(
                attrs={
                    "placeholder": "Contoh: Programming, Web Development, atau Mobile Legends",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsikan keahlian atau pengalamanku...",
                    "rows": 3,
                }
            ),
        }
        