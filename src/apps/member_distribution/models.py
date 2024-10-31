from django.db import models

class MemberDistribution(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    distribution = models.ForeignKey('distribution.Distribution', on_delete=models.CASCADE)
    is_needed = models.BooleanField(null=True, blank=True, default=True)
    contribution_bonus = models.IntegerField(null=True, blank=True, default=0)
    active_bonus = models.IntegerField(null=True, blank=True, default=0)
    discord_bonus = models.IntegerField(null=True, blank=True, default=0)
    total_bonus = models.IntegerField(null=True, blank=True, default=0)
    dice_result = models.IntegerField(null=True, blank=True)
    total_result = models.IntegerField(null=True, blank=True)
    has_looted = models.BooleanField(null=True, blank=True, default=False)
    date_loot = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_activate = models.BooleanField(null=True, blank=True, default=True)

    class Meta:
        """Define the name of the table"""
        db_table = 'member_distribution'
        verbose_name_plural = 'member_distributions'

    def __str__(self):
        status = "Inactive"
        if self.is_activate:
            status = "Active"

        return f"{self.id} [{self.distribution.loot.label}] {self.member.username} ({status})"
