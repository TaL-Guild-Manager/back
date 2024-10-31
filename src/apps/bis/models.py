from django.db import models

class BiS(models.Model):
    is_primary = models.BooleanField(null=True, blank=True, default=True)
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_activate = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        """Define the name of the table"""
        db_table = 'best_in_slot'
        verbose_name_plural = 'best_in_slots'

    def __str__(self):
        status = "Inactive"
        primary = "Primary"
        if self.is_activate:
            status = "Active"
        if not self.is_primary:
            primary = "Secondary"

        return f"{self.id} [{primary}] {self.member.username} ({status})"