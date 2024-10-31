from django.db import models

class Loot(models.Model):
    label = models.CharField(max_length=255, null=False)
    boss = models.ForeignKey('boss.Boss', on_delete=models.CASCADE)
    loot_type = models.ForeignKey('loot_type.LootType', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_activate = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        """Define the name of the table"""
        db_table = 'loot'
        verbose_name_plural = 'loots'

    def __str__(self):
        status = "Inactive"
        if self.is_activate:
            status = "Active"

        return f"{self.id} [{self.boss.label}] {self.label} ({status})"
