from django.db import models

class Blacklist(models.Model):
    username = models.CharField(max_length=255, null=False)
    previous_guild = models.CharField(max_length=255, null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_activate = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        """Define the name of the table"""
        db_table = 'blacklist'
        verbose_name_plural = 'blacklists'

    def __str__(self):
        status = "Inactive"
        if self.is_activate:
            status = "Active"

        return f"{self.id} [{self.previous_guild}] {self.username} ({status})"
