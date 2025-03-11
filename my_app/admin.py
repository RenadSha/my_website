from django.contrib import admin
from .models import Project, ProjectImage, Tag

class ProjectImageInline(admin.TabularInline):  # Gebruik `TabularInline` of `StackedInline`
    model = ProjectImage
    extra = 1  # Voegt één extra invoerveld toe bij het bewerken van een project
    fields = ('image', 'is_poster')  # Laat alleen deze velden zien in de admin

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name", "description")
    filter_horizontal = ("tags",)
    inlines = [ProjectImageInline]  # Hier voegen we de afbeeldingen toe

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "is_poster", "uploaded_at")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

