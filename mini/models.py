from django.db import models

# Create your models here.
class About(models.Model):
    name=models.CharField(max_length=50)
    job=models.CharField(max_length=60)
    subtitle=models.CharField(max_length=500)
    image=models.ImageField(upload_to= 'images/')
    from_adress=models.CharField(max_length=20)
    from_land=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    cv=models.FileField(upload_to='cv')

    def __str__(self):
        return self.name

SKILL_TYPE =(
    ('Coding','Coding'),
    ('Design','Design')
)

class Skills(models.Model):
    skill=models.CharField(max_length=50)
    percentage =models.IntegerField()
    type=models.CharField(max_length=50, choices= SKILL_TYPE)

    def __str__(self):
        return self.skill


class Education(models.Model):
    year=models.IntegerField()
    title=models.CharField(max_length=100)
    place=models.CharField(max_length=50)
    description=models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Experience(models.Model):
    year=models.IntegerField()
    title=models.CharField(max_length=100)
    place=models.CharField(max_length=50)
    description=models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Service(models.Model):
    
    icon=models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)

    def __strr__(self):
        return self.title


class Projects(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='proje/')
    tags=models.CharField(max_length=100)

    def __str__(self):
        return self.name