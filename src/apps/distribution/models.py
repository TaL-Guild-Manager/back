from django.db import models

class Distribution(models.Model):
    loot = models.ForeignKey('loot.Loot', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_activate = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        """Define the name of the table"""
        db_table = 'distribution'
        verbose_name_plural = 'distributions'

    def __str__(self):
        status = "Inactive"
        if self.is_activate:
            status = "Active"

        return f"{self.id} {self.loot.label} ({status})"
