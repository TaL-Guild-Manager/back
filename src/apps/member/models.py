from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=255, null=False)
    added_at = models.DateField(null=True, blank=True)
    removed_at = models.DateField(null=True, blank=True)
    is_on_discord = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    is_pvp = models.BooleanField(default=False, null=True, blank=True)
    has_privilege = models.BooleanField(default=False, null=True, blank=True)
    grade = models.ForeignKey('grade.Grade', on_delete=models.CASCADE, null=True, blank=True)
    weapon = models.ForeignKey('weapon.Weapon', on_delete=models.CASCADE, null=True, blank=True)
    combat_type = models.ForeignKey('combat_type.CombatType', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_activate = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        """Define the name of the table"""
        db_table = 'member'
        verbose_name_plural = 'members'

    def __str__(self):
        status = []
        if self.is_activate:
            status.append("Active")
        if self.is_on_discord:
            status.append("On Discord")
        if self.is_pvp:
            status.append("PvP")
        elif not self.is_pvp:
            status.append("PvE")

        status_str = ", ".join(status) if status else "Inactive"
        return f"{self.id} {self.username} ({status_str})"
