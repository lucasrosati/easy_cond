from django.db import models

class CamerasProfile(models.Model):
    numero= models.CharField(max_length=2)
    area = models.CharField(max_length=50)  
    url = models.CharField(max_length=500)    

    class Meta:
        db_table = 'registro_cameras'
