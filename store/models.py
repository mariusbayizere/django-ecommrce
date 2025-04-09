from django.db import models

# Create your models here.
class Collection(models.Model):
    Tittle = models.CharField(max_length=255)
    #cicle depancency Relationship  is happen when one class has depanding the another class twice at single time (means having mutple Relationship at one time in the signle class)
    # to implement this Relationship is Optional means this kind Relationship is not necessary
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')


    def __str__(self) -> str:
        return self.Tittle


    class Meta:
        ordering = ['Tittle']



class Promation(models.Model):
    Description = models.CharField(max_length=255)
    Discount = models.FloatField()


    def __str__(self) -> str:
        # return self.Description + '  '+ str(self.Discount)
        return f"{self.Description}       {self.Discount}"

    class Meta:
        ordering = ['Discount']


class Product(models.Model):
    Title = models.CharField(max_length=255)
    Description  = models.TextField()
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Inventory = models.IntegerField()
    Last_update = models.DateTimeField(auto_now=True)
    # ONE TO MANY RELATIONSHIP BETWEEN PRODUCT AND COLLECTION
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    promation = models.ManyToManyField(Promation, related_name='products')

    def __str__(self) -> str:
        return self.Title + '  ' + str(self.Price) + '  ' + str(self.Inventory) + '  ' + str(self.collection) + '  ' + str(self.promation)
    class Meta:
        ordering = ['Title']


class Customer(models.Model):

    DEFAULY_COUNTRY_Rw = 'RW'
    DEFAULY_COUNTRY_FR = 'FR'
    DEFAULY_COUNTRY_EN = 'EN'
    DEFAULY_COUNTRY_IT = 'IT'
    DEFAULY_COUNTRY_US = 'US'
    DEFAULY_COUNTRY_GR = 'GR'

    COUNTRY_CHOICE = [
        (DEFAULY_COUNTRY_Rw, 'Rwanda'),
        (DEFAULY_COUNTRY_FR, 'France'),
        (DEFAULY_COUNTRY_EN,'USA'),
        (DEFAULY_COUNTRY_IT,'Italy'),
        (DEFAULY_COUNTRY_US,'England'),
        (DEFAULY_COUNTRY_GR,'Germany')
    ]

    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=50, unique=True)
    Phone = models.CharField(max_length=15)
    Birth_date = models.DateField(null=True)
    Address = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Country = models.CharField(max_length=2, choices=COUNTRY_CHOICE, default=DEFAULY_COUNTRY_Rw)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.First_name + '  ' + self.Last_name + '  ' + self.Email + '  ' + self.Phone + '  ' + self.Address + '  ' + self.City + '  ' + self.Country
    class Meta:
        ordering = ['First_name']


class Order(models.Model):

    PENDING = 'P'
    COMPLETED = 'C'
    FAILED = 'F'

    PAYMENT_STATUS = [
        (PENDING,'Pending'),
        (COMPLETED,'Complete'),
        (FAILED,'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True),
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.placed_at) + '  ' + str(self.payment_status) + '  ' + str(self.customer)

class ordersItems(models.Model):
    Quantity = models.PositiveSmallIntegerField()
    Unity_price = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return str(self.Quantity) + '  ' + str(self.Unity_price) + '  ' + str(self.order) + '  ' + str(self.product)
    class Meta:
        ordering = ['Quantity']


class Address(models.Model):
    # street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    #one to one Relationship
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

    #one to one Relationship
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.city + '  ' + str(self.customer)
    class Meta:
        ordering = ['city']


class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.created)
    class Meta:
        ordering = ['created']

class CartItem(models.Model):
    Quantity = models.PositiveSmallIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self) -> str:
        # return str(self.Quantity) + '  ' + str(self.product) + '  ' + str(self.cart)
        return self.product
    class Meta:
        ordering = ['Quantity']