from django.db import models

class MainMaterials(models.Model):
    options = (
        ('Nos', 'Nos'),
        ('Kms', 'Kms'),
        ('Mtr', 'Mtr'),
        ('Set', 'Set'),
        ('Per Kit', 'Per Kit'),
        ('Cmtrs', 'Cmtrs'),
        ('Job', 'Job'),
        ('Mtrs', 'Mtrs'),
        ('Ft','Ft')
    )
    particular = models.CharField(max_length=250, blank=False, null=False)
    unit = models.CharField(max_length=10, choices=options, default="Nos")
    material_rate = models.CharField(max_length=50, blank=False, null=False)
    labour_rate = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.particular
    