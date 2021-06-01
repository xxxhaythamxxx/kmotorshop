from django.db import models
from django.db.models.deletion import CASCADE
from smart_selects.db_fields import ChainedManyToManyField

# Create your models here.
class car(models.Model):
    car_manufacturer=models.CharField(max_length=20, verbose_name="Manufacturer")    #Ejemplo: Audi
    car_model=models.CharField(max_length=100, verbose_name="Model", unique=True)           #Ejemplo: 100 C1 Coupe (817)
    car_from=models.DateField(verbose_name="From")      #Ejemplo: 11/2015
    car_to=models.DateField(verbose_name="To")          #Ejemplo: 11/2018
    transmission=models.CharField(max_length=10)        #Ejemplo: ATM, MTM (Automatic, Manual)

    def __str__(self):
        return '%s %s, (%s / %s)' %(self.car_manufacturer, self.car_model, self.car_from.year, self.car_to.year)

class engine(models.Model):
    car_engine_info=models.ManyToManyField(car)
    engine_l=models.CharField(max_length=10, verbose_name="Litre")             #Ejemplo: 1.8 D
    engine_ide=models.CharField(max_length=80, verbose_name="Code")          #Ejemplo: 1GRFE
    engine_type=models.CharField(max_length=15, verbose_name="Type")         #Ejemplo: Diesel, Petrol
    engine_cylinder=models.IntegerField(verbose_name="Cylinder (ccm)")               #Ejemplo: 1588 ccm
    engine_pistons=models.IntegerField(verbose_name="Pistons")                #Ejemplo: 4 pistons
    engine_power_kw=models.IntegerField(verbose_name="Power (kW)")               #Ejemplo: 63 kw
    engine_power_hp=models.IntegerField(verbose_name="Power (hp)")               #Ejemplo: 85 hp

    def __str__(self):
        return '%s %s %s %s ccm/%s pistons %s kW/%s hp' %(self.engine_ide, self.engine_l, self.engine_type, self.engine_cylinder, self.engine_pistons, self.engine_power_kw, self.engine_power_hp)
    

class category(models.Model):
    category=models.CharField(max_length=40, verbose_name="Category")     #Ejemplo: Filter

    def __str__(self):
        return '%s' %(self.category)

class spare(models.Model):
    car_info=models.ManyToManyField(car,blank=True,null=True)
    engine_info=ChainedManyToManyField(
        engine,
        chained_field="car_info",
        chained_model_field="car_engine_info",blank=True,null=True)
    spare_category = models.ForeignKey(category,on_delete=CASCADE,null=True)
    spare_spare = models.ManyToManyField("self",blank=True,null=True)
    
    spare_photo=models.ImageField(upload_to="spares", verbose_name="Photo",blank=True,null=True)                           #Será ImageField()
    spare_code=models.CharField(max_length=15, verbose_name="Code", unique=True)          #Ejemplo: 50013073
    spare_brand=models.CharField(max_length=20, verbose_name="Brand")         #Ejemplo: KOLBENSCMIDT
    spare_name=models.CharField(max_length=20, verbose_name="Name")          #Ejemplo: Oil filter
    shape=models.CharField(max_length=20, verbose_name="Shape",blank=True,null=True)             #Ejemplo: Rectangular
    long=models.FloatField(verbose_name="Long",blank=True,null=True)
    wide=models.FloatField(verbose_name="Wide",blank=True,null=True)
    high=models.FloatField(verbose_name="High",blank=True,null=True)
    diameter=models.FloatField(verbose_name="Diameter",blank=True,null=True)
    radio=models.FloatField(verbose_name="Radio",blank=True,null=True)

    def __str__(self):
        return '%s %s %s' %(self.spare_code, self.spare_brand, self.spare_name)
