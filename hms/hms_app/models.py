from django.db import models

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
    room_type = models.CharField(max_length=15)
    room_status = models.CharField(max_length=15)
    room_reservation_info = models.CharField(max_length=20)
    room_occupancy = models.CharField(max_length=15)
    room_status = models.CharField(max_length=15)
    room_notes = models.CharField(max_length=250)
    room_inspect_status = models.CharField(max_length=20, null=True)
    room_housekeeper = models.ForeignKey(Housekeeper, on_delete=models.CASCADE)
    room_updated_by = models.ForeignKey(Admin, on_delete=models.CASCADE)
    room_updated_time = models.DateTimeField(auto_now_add=True, null=True)
    
class Housekeeper_details(models.Model):
    id = models.AutoField(primary_key=True)
    housekeeper_id = models.ForeignKey(Housekeeper, on_delete=models.CASCADE)
    housekeeper_status = models.CharField(max_length=20)

class Housekeeper_room_visit(models.Model):
    id = models.AutoField(primary_key=True)
    housekeeper_id = models.ForeignKey(Housekeeper, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    
    
        
