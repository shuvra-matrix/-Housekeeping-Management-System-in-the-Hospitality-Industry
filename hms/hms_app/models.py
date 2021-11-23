from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=100)
    admin_id = models.CharField(max_length=20)
    admin_email = models.CharField(max_length=40)
    admin_password = models.CharField(max_length=30)
    
class Housekeeper(models.Model):
    id = models.AutoField(primary_key=True)
    housekeeper_id = models.CharField(max_length=20)
    housekeeper_name = models.CharField(max_length=30)
    housekeeper_email = models.CharField(max_length=40)
    housekeeper_password = models.CharField(max_length=30)
    housekeeper_mobile = models.CharField(max_length=20,null=True)


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.CharField(max_length=20)
    staff_name = models.CharField(max_length=30)
    staff_email = models.CharField(max_length=40)
    staff_password = models.CharField(max_length=30)
    staff_mobile = models.CharField(max_length=20, null=True)
    
class Room_floor(models.Model):
    floor_id = models.AutoField(primary_key=True)
    floor_name = models.CharField(max_length=20)
    
    
    
class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    floor_id = models.ForeignKey(Room_floor, on_delete=models.CASCADE, related_name='floors_id')
    room_name = models.CharField(max_length=30)
    
class Room_details(models.Model):
    id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=20)
    room_status = models.CharField(max_length=20,default="Active")
    room_reservation_info = models.CharField(max_length=20,null=True)
    room_occupancy = models.CharField(max_length=20,default="Vacant")
    room_notes = models.CharField(max_length=250,null=True)
    room_inspect_status = models.CharField(max_length=20, default="Inspected")
    room_housekeeper = models.ForeignKey(Housekeeper, on_delete=models.DO_NOTHING,null=True)
    room_updated_by = models.ForeignKey(Admin, on_delete=models.DO_NOTHING,null=True)
    room_updated_time = models.DateTimeField(auto_now_add=True, null=True)
    

class Housekeeper_room_visit(models.Model):
    id = models.AutoField(primary_key=True)
    housekeeper_id = models.ForeignKey(Housekeeper, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)

    
class Housekeeper_details(models.Model):
    id = models.AutoField(primary_key=True)
    housekeeper_id = models.ForeignKey(Housekeeper, on_delete=models.CASCADE)
    housekeeper_status = models.CharField(max_length=20)

class Food_type(models.Model):
    id=models.AutoField(primary_key=True)
    food_type = models.CharField(max_length=10)

class Food_drinks(models.Model):
    id=models.AutoField(primary_key=True)
    food_type = models.ForeignKey(Food_type,on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)

class Food_quentity(models.Model):
    id = models.AutoField(primary_key=True)
    food_type = models.ForeignKey(Food_type,on_delete=CASCADE)
    quentity = models.CharField(max_length=20)

class Room_service(models.Model):
    id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(Room,on_delete=models.CASCADE)
    food_type = models.ForeignKey(Food_drinks,on_delete=models.DO_NOTHING)
    food_quentity = models.ForeignKey(Food_quentity,on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True, null=True)

class Food_order_list(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    food_name = models.ForeignKey(Food_drinks, on_delete=models.DO_NOTHING)
    quentity = models.ForeignKey(Food_quentity, on_delete=models.DO_NOTHING)
    
    
    
    
        
