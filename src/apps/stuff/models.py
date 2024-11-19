from django.db import models

class Stuff(models.Model):
    label = models.CharField(max_length=255, null=True, blank=True)
    is_raid_loot = models.BooleanField(null=True, blank=True, default=True)
    loot = models.ForeignKey('loot.Loot', on_delete=models.CASCADE, null=True, blank=True)
    loot_type = models.ForeignKey('loot_type.LootType', on_delete=models.CASCADE, null=True, blank=True)
    boss = models.ForeignKey('boss.Boss', on_delete=models.CASCADE, null=True, blank=True)
    has_been_acquired = models.BooleanField(default=False, null=True, blank=True)
    acquired_at = models.DateField(default=None, null=True, blank=True)
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
