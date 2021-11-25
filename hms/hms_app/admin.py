from django.contrib import admin
from hms_app.models import Admin, Housekeeper, Room_floor, Room, Room_details, Housekeeper_details, Housekeeper_room_visit, Staff, Food_type, Food_drinks, Food_quentity, Room_service, Food_order_list, Customer_complaints, Daily_activities, Housekeeping_daily_activity,Staff_type
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
admin.site.register(Customer_complaints),
admin.site.register(Daily_activities),
admin.site.register(Housekeeping_daily_activity),
admin.site.register(Staff_type),

