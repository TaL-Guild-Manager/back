from django.db import models

# Create your models here.
class Roadster(models.Model):
    label = models.CharField(max_length=255, null=False)
    is_pvp = models.BooleanField(null=True, blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_activate = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        """Define the name of the table"""
        db_table = 'roadster'
        verbose_name_plural = 'roadsters'

    def __str__(self):
        status = []
        if self.is_activate:
            status.append("Active")
        if self.is_pvp:
            status.append("PvP")
        elif not self.is_pvp:
            status.append("PvE")

        status_str = ", ".join(status) if status else "Inactive"

        return f"{self.id} {self.label} ({status_str})"