from django.db import models

# Create your models here.


# Creating a 'Product' model
class Product(models.Model):
    product_id = models.IntegerField(default=0)
    product_name = models.CharField(max_length=300)
    qty = models.IntegerField(default=0)

    # Displaying product details
    def __str__(self):
        return str(self.product_id) + ", " + str(self.product_name) + ", " + str(self.qty)
