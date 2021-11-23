from django.contrib import admin
from hms_app.models import Admin, Housekeeper, Room_floor, Room, Room_details, Housekeeper_details, Housekeeper_room_visit, Staff, Food_type, Food_drinks, Food_quentity, Room_service,Food_order_list
# Register your models here.
admin.site.register(Admin),
admin.site.register(Housekeeper),
admin.site.register(Room_floor),
admin.site.register(Room),
admin.site.register(Room_details),
admin.site.register(Housekeeper_details),
admin.site.register(Housekeeper_room_visit),
admin.site.register(Staff),
admin.site.register(Room_service),
admin.site.register(Food_type),
admin.site.register(Food_drinks),
admin.site.register(Food_quentity),
admin.site.register(Food_order_list),
