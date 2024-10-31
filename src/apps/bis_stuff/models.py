from django.db import models

class BiSStuff(models.Model):
    bis = models.ForeignKey('bis.BiS', on_delete=models.CASCADE)
    stuff = models.ForeignKey('stuff.Stuff', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_activate = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        """Define the name of the table"""
        db_table = 'best_in_slot_stuff'
        verbose_name_plural = 'best_in_slot_stuffs'

    def __str__(self):
        status = "Inactive"
        if self.is_activate:
            status = "Active"

        return f"{self.id} [{self.bis.member.username}] {self.stuff.label} ({status})"