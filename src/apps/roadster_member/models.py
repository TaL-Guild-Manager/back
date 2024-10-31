from django.db import models

# Create your models here.
class RoadsterMember(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    roadster = models.ForeignKey('roadster.Roadster', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_activate = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        """Define the name of the table"""
        db_table = 'roadster_member'
        verbose_name_plural = 'roadster_members'

    def __str__(self):
        status = "Inactive"
        if self.is_activate:
            status = "Active"

        return f"{self.id} [{self.roadster.label}] {self.member.username} ({status})"