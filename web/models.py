from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now


# Create your models here.
Y = '1'
T = '2'
TJ = '0'

CHOICES = (
    (Y, 'Ya'),
    (T, 'Tidak'),
    (TJ, 'Tidak Jelas'),
)

AN = '0'
ANN = '1'
APS = '2'

AKTOR_CHOICES = (
        (AN, 'Aktor Negara'),
        (ANN, 'Aktor Non Negara'),
        (APS, 'Aktor Perusahaan Swasta'),
    )

class province(models.Model):
    PL = '0'
    MP = '1'
    TYPE_CHOICES = (
        (PL, 'Polygon'),
        (MP, 'MultiPolygon'),
    )
    nama = models.CharField(max_length=30)
    slug = models.SlugField(default='', editable=False, max_length=320)
    coordinate = models.TextField(blank=True, null=True)
    coordinate_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    province_id = models.PositiveIntegerField(unique=True)
    keterangan = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = ("Provinsi")
        verbose_name_plural = ("Provinsi")

    def save(self, *args, **kwargs):
        value = self.nama
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class distrcit_city(models.Model):
    nama = models.CharField(max_length=30)
    slug = models.SlugField(default='', editable=False, max_length=320)
    coordinate = models.TextField(blank=True, null=True)
    city_id = models.PositiveBigIntegerField(unique=True)
    Province = models.ForeignKey(province, on_delete=models.CASCADE)
    keterangan = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama + ' - '+ str(self.Province)

    class Meta:
        verbose_name = ("Kabupaten/Kota")
        verbose_name_plural = ("Kabupaten/Kota")

    def save(self, *args, **kwargs):
        value = self.nama
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class sub_district(models.Model):
    nama = models.CharField(max_length=30)
    slug = models.SlugField(default='', editable=False, max_length=320)
    coordinate = models.TextField(blank=True, null=True)
    subdistrict_id = models.PositiveBigIntegerField(unique=True)
    district = models.ForeignKey(distrcit_city, on_delete=models.CASCADE)
    keterangan = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama + ' - '+ str(self.district)

    class Meta:
        verbose_name = ("Sub District")
        verbose_name_plural = ("Sub District")

    def save(self, *args, **kwargs):
        value = self.nama
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    
class village(models.Model):
    nama = models.CharField(max_length=30)
    slug = models.SlugField(default='', editable=False, max_length=320)
    village_id = models.PositiveBigIntegerField(unique=True)
    sub_district = models.ForeignKey(sub_district, on_delete=models.CASCADE)
    keterangan = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama+' - '+str(self.sub_district)

    class Meta:
        verbose_name = ("Village")
        verbose_name_plural = ("Village")

    def save(self, *args, **kwargs):
        value = self.nama
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class incident(models.Model):
    
    incident_id = models.CharField(max_length=12)
    slug = models.SlugField(default='', editable=False, max_length=320)
 #   timestamp = models.DateTimeField(blank=True, null=True)
    area_district = models.ForeignKey(distrcit_city, on_delete=models.CASCADE, null=True, blank=True)
    area_subdistrict = models.ForeignKey(sub_district, on_delete=models.CASCADE, null=True, blank=True)
    area_village = models.ForeignKey(village, on_delete=models.CASCADE, null=True, blank=True)
    covid_rel = models.PositiveBigIntegerField(null=True, blank=True)
    num_death = models.PositiveBigIntegerField(null=True, blank=True)
    num_injured = models.PositiveBigIntegerField(null=True, blank=True)
    death_injured = models.PositiveBigIntegerField(null=True, blank=True)
    fem_death = models.PositiveBigIntegerField(null=True, blank=True)
    fem_injured = models.PositiveBigIntegerField(null=True, blank=True)
    child_death = models.PositiveBigIntegerField(null=True, blank=True)
    child_injured = models.PositiveBigIntegerField(null=True, blank=True)
    Infra_damage = models.PositiveBigIntegerField(null=True, blank=True)
    Infra_destroyed = models.PositiveBigIntegerField(null=True, blank=True)
    intervene = models.CharField(choices=CHOICES, max_length=2)
    source = models.URLField()
    related = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
 #   date_created = models.DateTimeField(auto_now_add=True)
 #  date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.incident_id

    class Meta:
        verbose_name = ("Incident")
        verbose_name_plural = ("Incidents")

    def save(self, *args, **kwargs):
        value = self.incident_id
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class actor_category(models.Model):
    nama = models.CharField(max_length=35)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.incident_id

    class Meta:
        verbose_name = ("Actor Category")
        verbose_name_plural = ("Actor Categories")

class incident_actor(models.Model):
    NUMBER_CHOICES = (
        (1, 1),
        (2, 2),
        
    )
    incident_events = models.ForeignKey(incident, on_delete=models.CASCADE)
    slug = models.SlugField(default='', editable=False, max_length=320)
    actor_no = models.CharField(max_length=1, choices=NUMBER_CHOICES, blank=True)
    actor = models.CharField(max_length=100)
    actor_category = models.CharField(max_length=2, choices=AKTOR_CHOICES)
    actor_vm = models.CharField(max_length=2, choices=CHOICES)
    actor_Total = models.IntegerField()
    keterangan = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.incident_events)

    class Meta:
        verbose_name = ("Incident Actor")
        verbose_name_plural = ("Incident Actors")

    def save(self, *args, **kwargs):
        value = str(self.incident_events)
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class violence_category(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = ("Violence Category")
        verbose_name_plural = ("Violence Categories")

class violence_form(models.Model):
    category = models.ForeignKey(violence_category, on_delete=models.CASCADE)
    event = models.ForeignKey(incident, on_delete=models.CASCADE)
    keterangan = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category)

    class Meta:
        verbose_name = ("Violence Form")
        verbose_name_plural = ("Violence Forms")

class Weapon_category(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = ("Weapon Category")
        verbose_name_plural = ("Weapon Categories")

class Weapon_form(models.Model):
    category = models.ForeignKey(Weapon_category, on_delete=models.CASCADE)
    event = models.ForeignKey(incident, on_delete=models.CASCADE)
    keterangan = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category)

    class Meta:
        verbose_name = ("Weapon Form")
        verbose_name_plural = ("Weapon Forms")

class Issue_category(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = ("Issue Category")
        verbose_name_plural = ("Issue Categories")

class Issue_Type(models.Model):
    category = models.ForeignKey(Issue_category, on_delete=models.CASCADE)
    event = models.ForeignKey(incident, on_delete=models.CASCADE)
    keterangan = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category)

    class Meta:
        verbose_name = ("Issue")
        verbose_name_plural = ("Issues")

class Intervene_actions(models.Model):
    actor_category = models.CharField(max_length=2, choices=AKTOR_CHOICES)
    actor = models.CharField(max_length=150)
    incident_event = models.ForeignKey(incident, on_delete=models.CASCADE)
    keterangan = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_actor_category_display

    class Meta:
        verbose_name = ("Intervene")
        verbose_name_plural = ("Intervene")