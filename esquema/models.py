from django.db import models

# Create your models here.
class  userdate ( models.Model ) :

    names=models.CharField('Names',max_length=25)
    surname=models.CharField('Surname',max_length=25)
    surname2=models.CharField('Surname',max_length=25)
    Doc=models.CharField('Document', max_length=15)
    birthday=models.DateTimeField('Birth Date')
    pub_date=models.DateTimeField('Date published')

    def nombrecompleto(self):
        cadena="{0} {1}, {2}"
        return cadena.format(self.names,self.surname,self.surname2)
    def __str__(self):

        return self.nombrecompleto()


class vacuna(models.Model):
    user=models.ForeignKey(userdate, on_delete=models.CASCADE)
    vaccinate=models.CharField(max_length=50,null=True,blank=True)
    td=(('',''),('R','Recien Nacido'),('U','Unica'),('P','Primera',),('S','Segunda'),('T','Tercera'),
        ('A','Anual'),('PR','Primer Refuerzo'),('SR','Segundo Refuerzo'))
    dose=models.CharField(max_length=2,choices=td,default='')

    def __str__(self):
        return self.vaccinate
class frequently(models.Model):
    disease_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.disease_text
