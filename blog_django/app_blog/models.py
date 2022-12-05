from django.db import models

# Create your models here.
class TextComment(models.Model):
    '''
    Primer modelo creado para test
    '''
    auto_incremental_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 100)
    creador = models.CharField(max_length=100)
    post = models.CharField(max_length = 200,null=True)
    date_creacion = models.DateField(blank=True,null=True)
    
    PENGUIN = 'PNG'
    ATLAS = 'ATL'
    ATHENEO = 'ATH'
    
    editorial_options = [
        (PENGUIN, 'Penguin'),
        (ATLAS, 'Atlas'),
        (ATHENEO, 'Atheneo')]

    editorial = models.CharField(
        max_length = 3,
        choices = editorial_options,
        default = ATLAS
    )

    image_view = models.ImageField(upload_to = 'images/', blank = True)

    def __str__(self):
        return f'ID: {self.auto_incremental_id} - {self.date_creacion}: Nombre:{self.nombre}\nPOST:{self.post}\nBy:{self.creador}'