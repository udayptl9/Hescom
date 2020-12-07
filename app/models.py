from django.db import models


class MainMaterial(models.Model):
    options = (
        ('Nos', 'Nos'),
        ('Kms', 'Kms'),
        ('Mtr', 'Mtr'),
        ('Set', 'Set'),
        ('Per Kit', 'Per Kit'),
        ('Cmtrs', 'Cmtrs'),
        ('Job', 'Job'),
        ('Mtrs', 'Mtrs'),
        ('Ft', 'Ft')
    )
    particular = models.CharField(max_length=250, blank=False, null=False)
    unit = models.CharField(max_length=10, choices=options, default="Nos")
    material_rate = models.CharField(max_length=50, blank=False, null=False)
    labour_rate = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.particular


class Ltlinedomestic(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class Ltlineipset(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class ExtenHtLine(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class ExtenTransformerCenter(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class ExtenTransLtLine(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class SpunPOIHtLine(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class SpunPOITransformer(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class AdditionalDTCHtLine(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class AdditionalDTCTransformer(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class IpSet63KvaHtLine(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class IpSet63KvaTransformer(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class IpSet63KvaLtLine(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class IpSet100KvaHtLine(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class IpSet100KvaTransformer(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class IpSet100KvaLtLine(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class IpSet25KvaHtLine(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class IpSet25KvaTransformer(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class IpSet25KvaLtLine(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular


class LayoutRabit(models.Model):
    particular = models.ForeignKey(MainMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular.particular
