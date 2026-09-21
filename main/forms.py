from django.forms import ModelForm, Select, Textarea, TextInput, URLInput
from main.models import Experience, Skill


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


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "category",
            "description",
            "thumbnail",
            "ended_at",
        ]
        labels = {
            "title": "Judul Pengalaman",
            "category": "Kategori Pengalaman",
            "description": "Deskripsi Pengalaman",
            "thumbnail": "URL Gambar/Thumbnail",
            "ended_at": "Tanggal Selesai (Kosongkan jika masih berjalan)",
        }
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Product Manager RISTEK / Asisten Dosen DDP",
                    "maxlength": 255,
                }
            ),
            "category": Select(),
            "description": Textarea(
                attrs={
                    "placeholder": "Jelaskan peran dan pencapaianmu...",
                    "rows": 4,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://example.com/image.png",
                }
            ),
            "ended_at": TextInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }