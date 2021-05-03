from django.db import models
class  Medicine(models.Model):
    name = models.CharField(max_length=200, blank=True,null=True)
    company = models.CharField(max_length=200, blank=True,null=True)
    exp_date = models.DateField()
    price = models.FloatField(default='0', null=True, blank=True)
    quantity = models.IntegerField()
    reorder_level=models.IntegerField(default='0',blank=True,null=True)
    sell_quantity=models.IntegerField(default='0',blank=True,null=True)
    purchase_quantity=models.IntegerField(default='0',blank=True,null=True)
    Last_updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    timestamp= models.DateTimeField(auto_now_add=True, auto_now=False)
    near_exp_date=models.DateField(blank=True,null=True)
    activate=models.BooleanField(default=False,blank=True,null=True)
    def __str__(self):
        return self.name + ' ' + str(self.quantity)
class  MedicineHistory(models.Model):
    name = models.CharField(max_length=200, blank=True,null=True)
    company = models.CharField(max_length=200, blank=True,null=True)
    exp_date = models.DateField()
    price = models.FloatField(default='0', null=True, blank=True)
    quantity = models.IntegerField()
    reorder_level=models.IntegerField(default='0',blank=True,null=True)
    sell_quantity=models.IntegerField(default='0',blank=True,null=True)
    purchase_quantity=models.IntegerField(default='0',blank=True,null=True)
    Last_updated=models.DateTimeField(auto_now_add=False,auto_now=False,null=True)
    timestamp= models.DateTimeField(auto_now_add=False, auto_now=False,null=True)
    activate=models.BooleanField(default=False)



class  Sales(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    Sales_date = models.DateField(blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    amount=models.FloatField(blank=True,null=True)


