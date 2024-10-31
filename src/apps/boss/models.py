from django.db import models

class Boss(models.Model):
    label = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_activate = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        """Define the name of the table"""
        db_table = 'boss'
        verbose_name_plural = 'bosses'

    def __str__(self):
        status = "Inactive"
        if self.is_activate:
            status = "Active"

        return f"{self.id} {self.label} ({status})"