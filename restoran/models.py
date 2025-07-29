from django.db import models
from django_resized import ResizedImageField

class Main(models.Model):
    image=ResizedImageField(upload_to='main/Y%/%m')
    description=models.TextField()

    def __str__(self):
        return f'{self.image}'
    
    class Meta:
        db_table='main'
        verbose_name='main'
        verbose_name_plural='main'




class About(models.Model):
    first_pic=ResizedImageField(upload_to='about/%Y/%m')
    second_pic=ResizedImageField(upload_to='about/%Y/%m')
    third_pic=ResizedImageField(upload_to='about/%Y/%m')
    fourth_pic=ResizedImageField(upload_to='about/%Y/%m')
    description=models.TextField()
    experience=models.PositiveIntegerField()
    masterchefs=models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_pic}'
    
    class Meta:
        db_table='about'
        verbose_name='about'
        verbose_name_plural='about'




class Home_Service(models.Model):
    service_theme=models.CharField(max_length=256)
    service_description=models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.service_theme}'
    
    class Meta:
        db_table='home_service'
        verbose_name='home service'
        verbose_name_plural='home services'




class Order(models.Model):
    people=models.PositiveIntegerField()

    def __str__(self):
        return f'{self.people}'
    
    class Meta:
        db_table='people number'
        verbose_name='people number'
        verbose_name_plural='people numbers'




class Book_Online(models.Model):
    full_name=models.CharField(max_length=256)
    email=models.EmailField()
    date=models.DateTimeField(null=True)
    special_request=models.TextField()
    people=models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.full_name}'
    
    class Meta:
        db_table='book online'
        verbose_name='book online'
        verbose_name_plural='booking online'




class Ourteam(models.Model):
    full_name=models.CharField(max_length=256)
    designation=models.CharField(max_length=256)
    pic=ResizedImageField(upload_to='ourteam/%Y/%m')
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.full_name}'
    
    class Meta:
        db_table='ourteam'
        verbose_name='ourteam'
        verbose_name_plural='ourteams'




class Clients(models.Model):
    client_name=models.CharField(max_length=256)
    profession=models.CharField(max_length=256)
    client_pic=ResizedImageField(upload_to='client_pics/%Y/%m')
    comment=models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.client_name}'
    
    class Meta:
        db_table='client'
        verbose_name='client'
        verbose_name_plural='clients'




class Contact_Email(models.Model):
    book_email=models.EmailField()
    general_email=models.EmailField()
    technical_email=models.EmailField()

    def __str__(self):
        return f'{self.book_email}'
    
    class Meta:
        db_table='contact_email'
        verbose_name='contact email'
        verbose_name_plural='contact emails'




class Contact(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField()
    subject=models.CharField(max_length=256)
    message=models.TextField()

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        db_table='contact'
        verbose_name='contact'
        verbose_name_plural='contacts'




class Category(models.Model):
    name=models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        db_table='category'
        verbose_name='category'
        verbose_name_plural='categories'




class Dishes(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=256)
    description=models.CharField(max_length=350)
    image=ResizedImageField(upload_to='dishes/%Y/%m')
    price=models.PositiveIntegerField()
    

    def __str__(self):
        return f'{self.category}'
    
    class Meta:
        db_table='dish'
        verbose_name='dish'
        verbose_name_plural='dishes'




class Footer(models.Model):
    street=models.CharField(max_length=256)
    number=models.CharField(max_length=256)
    email=models.EmailField()
    start_and_end_days=models.CharField(max_length=256)
    time_1=models.CharField(max_length=256)
    time_sunday=models.CharField(max_length=256)
    newsletter_description=models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.street}'
    
    class Meta:
        db_table='footer'
        verbose_name='footer'
        verbose_name_plural='footers'



  
# Create your models here.
