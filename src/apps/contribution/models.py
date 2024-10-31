from django.db import models

class Contribution(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    start = models.IntegerField(null=True, blank=True, default=0)
    end = models.IntegerField(null=True, blank=True, default=0)
    contribution_start = models.DateField()
    contribution_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_activate = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        """Define the name of the table"""
        db_table = 'contribution'
        verbose_name_plural = 'contributions'

    def __str__(self):
        status = "Inactive"
        if self.is_activate:
            status = "Active"

        return f"{self.id} [{self.contribution_start} - {self.contribution_end}] {self.member.username} ({status})"
