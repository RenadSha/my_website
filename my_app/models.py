from django.db import models
import re
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    # Opties voor projecttype
    PROJECT_TYPES = [
        ('academic', 'Academic Project'),
        ('client', 'Client Project'),
        ('personal', 'Personal Project'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.ManyToManyField('Tag', related_name="projects")
    type = models.CharField(max_length=20, choices=PROJECT_TYPES, default='personal')  # Type van het project
    link = models.URLField(blank=True, null=True)  # Optionele link naar het project
    video_url = models.URLField(blank=True, null=True)  # Optionele YouTube-video

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def poster_image(self):
        return self.images.filter(is_poster=True).first()

    def embed_video(self):
        """Converteert een YouTube-link (normaal of Shorts) naar een embed-link"""
        if self.video_url:
            # Zoek naar een normale YouTube-video of een Shorts-link
            match = re.search(r"(?:v=|/shorts/)([^&/?]+)", self.video_url)
            if match:
                return f"https://www.youtube.com/embed/{match.group(1)}"
        return None

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="project_images/")
    is_poster = models.BooleanField(default=False) 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.project.name} {'(Poster)' if self.is_poster else ''}"
    
    

