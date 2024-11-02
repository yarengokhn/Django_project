from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe


# Create your models here.
class Category(models.Model):
    STATUS = (
    ('True','Evet'),
    ('False','Hayir'))
    
    title =models.CharField(max_length=30,verbose_name='Baslik')#admiin tarafinda baslik seklinde yazilacak
    keywords =models.CharField(blank=True,max_length=250,verbose_name='Anahtar Kelimeler')#bos birakilabilir.
    description =models.CharField(blank=True,max_length=250)
    image = models.ImageField(blank=True,upload_to='images/')

    status =models.CharField(max_length=10,choices=STATUS)
    slug = models.SlugField(null=False,unique=True) #muhakkak doldurulmasi gerektigi icin null False yaptik.
    parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)

    create_at =models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.title
    



class Product(models.Model):
    STATUS = (
    ('True','Evet'),
    ('False','Hayir'),)
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #many to one relation #on delete o satir silinirse baglanti olanlarin tümünü sil anlamina geliyor

    title =models.CharField(max_length=150)
    keywords =models.CharField(blank=True,max_length=255)#bos birakilabilir.
    description =models.CharField(blank=True,max_length=255)
    image = models.ImageField(blank=True,upload_to='images/')

    price = models.FloatField()
    amount = models.IntegerField(default=0)

    details = models.TextField()
    status =models.CharField(max_length=10,choices=STATUS,default='False')
    
    create_at =models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False,unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def image_tag(self):
        return mark_safe('<img src = "{}" width = "50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'
    
    #resim alanını HTML olarak göstermek için kullanılan bir fonksiyondur. image_tag fonksiyonu, bir HTML <img> etiketi oluşturur ve mark_safe() fonksiyonuyla bu HTML'yi "güvenli" hale getirir. Böylece Django, bu HTML kodunu olduğu gibi güvenle görüntüler ve değiştirmez.

    # admin tarafinda ürün düzenlerken ürün resminin görünmesi icin 
    def image_preview(self):
        if self.image:
            return format_html('<img src = "{}"'
                               'style ="width:300px;height:auto;" />', self.image.url)
        return '-'
    image_preview.short_description = 'Current Image '

    def __str__(self):
        return self.title
    
class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/{}')
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src = "{}" width = "50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'
    


    





    


