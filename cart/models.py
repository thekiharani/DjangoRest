from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings

def create_serial(instance, initials):
    if instance.pk < 10:
        return f'{initials}-00{instance.pk}'
    elif instance.pk < 100:
        return f'{initials}-0{instance.pk}'
    else:
        return f'{initials}-{instance.pk}'
        

class Product(models.Model):
    '''The product table'''
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    qty = models.IntegerField()
    serial_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # Signal to update the serial number
@receiver(post_save, sender=Product)
def save_product(sender, instance, created, **kwargs):
    if created:
        instance.serial_number = create_serial(instance, 'PRD')
        instance.save()


class Project(models.Model):
    '''The Project table'''
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=15)
    description = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # Signal to update the serial number
@receiver(post_save, sender=Project)
def save_project(sender, instance, created, **kwargs):
    if created:
        instance.serial_number = create_serial(instance, 'PRJ')
        instance.save()



class Requisition(models.Model):
    '''The parent requisition schedule: holds common data like project, foreman, serial_number and the date scheduled'''
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    foreman= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serial_number

# Signal to update the serial number
@receiver(post_save, sender=Requisition)
def save_requisition(sender, instance, created, **kwargs):
    if created:
        instance.serial_number = create_serial(instance, 'RS')
        instance.save()

class RequisitionMeta(models.Model):
    '''Particulars of requisition: holds specific data on each product requested under parent requisition'''
    requisition = models.ForeignKey(Requisition, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    requisition_price = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField()
    ordered = models.BooleanField(default=False)
    expected_delivery_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['requisition', 'product']]

    def __str__(self):
        return self.requisition