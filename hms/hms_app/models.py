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


class Staff_type(models.Model):
    id = models.AutoField(primary_key=True)
    staff_type = models.CharField(max_length=50)


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.CharField(max_length=20)
    staff_name = models.CharField(max_length=30)
    staff_type = models.ForeignKey(Staff_type, on_delete=models.SET_NULL,null=True)
    staff_email = models.CharField(max_length=40)
    staff_password = models.CharField(max_length=30)
    staff_mobile = models.CharField(max_length=20, null=True)
    
class Room_floor(models.Model):
    floor_id = models.AutoField(primary_key=True)
    floor_name = models.CharField(max_length=20)
    
    
    
class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    floor_id = models.ForeignKey(Room_floor, on_delete=models.SET_NULL,null=True)
    room_name = models.CharField(max_length=30)
    
class Room_details(models.Model):
    id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL,null=True)
    room_type = models.CharField(max_length=20)
    room_status = models.CharField(max_length=20,default="Active")
    room_reservation_info = models.CharField(max_length=20,null=True)
    room_occupancy = models.CharField(max_length=20,default="Vacant")
    room_notes = models.CharField(max_length=250,null=True)
    room_housekeeper_note = models.CharField(max_length=255,null=True)
    room_inspect_status = models.CharField(max_length=20, default="Inspected")
    room_housekeeper = models.ForeignKey(Housekeeper, on_delete=models.SET_NULL,null=True)
    room_updated_by = models.CharField(max_length=50 ,null=True)
    room_updated_time = models.CharField(max_length=20, null=True)
    

class Housekeeper_room_visit(models.Model):
    id = models.AutoField(primary_key=True)
    housekeeper_id = models.ForeignKey(Housekeeper, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL,null=True)

    
class Housekeeper_details(models.Model):
    id = models.AutoField(primary_key=True)
    housekeeper_id = models.ForeignKey(Housekeeper, on_delete=models.CASCADE)
    housekeeper_status = models.CharField(max_length=20)

class Food_type(models.Model):
    id=models.AutoField(primary_key=True)
    food_type = models.CharField(max_length=10)

class Food_drinks(models.Model):
    id=models.AutoField(primary_key=True)
    food_type = models.ForeignKey(Food_type,on_delete=models.SET_NULL,null=True)
    food_name = models.CharField(max_length=20)

class Food_quentity(models.Model):
    id = models.AutoField(primary_key=True)
    food_type = models.ForeignKey(
        Food_type, on_delete=models.SET_NULL, null=True)
    quentity = models.CharField(max_length=20)


class Food_order_list(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    food_name = models.ForeignKey(
        Food_drinks, on_delete=models.SET_NULL, null=True)
    quentity = models.ForeignKey(
        Food_quentity, on_delete=models.SET_NULL, null=True)
    show_list = models.CharField(max_length=5, default="yes")

class Room_service(models.Model):
    id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    food_list_id = models.ForeignKey(
        Food_order_list, on_delete=models.SET_NULL, null=True)
    order_taken_by = models.CharField(max_length=50, null=True)
    order_status = models.CharField(max_length=20,default="Under-Cooking")
    time = models.CharField(max_length=20, null=True)
    show_details= models.CharField(max_length=5)

class Customer_complaints(models.Model):
    id = models.AutoField(primary_key=True)
    complaints = models.CharField(max_length=255)
    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    complaints_taken_by = models.CharField(max_length=50)
    complaints_by = models.CharField(max_length=50)
    time = models.CharField(max_length=20)
    status = models.CharField(max_length=20,default="Review")
     
class Daily_activities(models.Model):
    id = models.AutoField(primary_key=True)
    activity = models.CharField(max_length=50)
    time = models.CharField(max_length=10, default="00000000")
        
class Housekeeping_daily_activity(models.Model):
    id = models.AutoField(primary_key=True)
    activity = models.ForeignKey(
        Daily_activities, on_delete=models.SET_NULL, null=True)
    time = models.CharField(max_length=10, default="00000000")


class Monthly_roster(models.Model):
    id = models.AutoField(primary_key=True)
    staff_type = models.ForeignKey(Staff_type, on_delete=models.SET_NULL,null=True)
    staff_name = models.ForeignKey(Staff, on_delete=models.SET_NULL,null=True)
    date_from = models.CharField(max_length=15)
    date_to = models.CharField(max_length=15)
    time_from = models.CharField(max_length=15)
    time_to = models.CharField(max_length=15)
    update_time = models.CharField(max_length=15)
    update_by = models.CharField(max_length=25)
    
