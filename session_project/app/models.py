from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Profile → OneToOne → User
class Profile(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    full_name = models.CharField(max_length=20)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profiles/')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)

    def __str__(self):
        return self.full_name


# Category → OneToMany → Product
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

# Tag → ManyToMany → Product
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Product → ManyToOne → Category
# Product → ManyToMany → Tag
# Product → ManyToOne → User (Seller)
# Product → ManyToMany → Cart
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tags = models.ManyToManyField(Tag, related_name='products')


    def __str__(self):
        return self.name


# Cart → OneToOne → User
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# Cart → ManyToMany → Product (through CartItem)
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)



# Order → ManyToOne → User
# Order → ManyToMany → Product (through OrderItem)    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)

# OrderItem → ManyToOne → Order
# OrderItem → ManyToOne → Product
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


