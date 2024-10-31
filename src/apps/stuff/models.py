from django.db import models

class Stuff(models.Model):
    label = models.CharField(max_length=255, null=False)
    is_raid_loot = models.BooleanField(null=True, blank=True, default=True)
    loot_type = models.ForeignKey('loot_type.LootType', on_delete=models.CASCADE)
    boss = models.ForeignKey('boss.Boss', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_activate = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        """Define the name of the table"""
        db_table = 'stuff'
        verbose_name_plural = 'stuffs'

    def __str__(self):
        status = "Inactive"
        if self.is_activate:
            status = "Active"

        return f"{self.id} [{self.loot_type.label}] {self.label} ({status})"
