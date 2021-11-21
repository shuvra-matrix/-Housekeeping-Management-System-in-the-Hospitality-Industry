from django.contrib import admin
from hms_app.models import Admin,Housekeeper,Room_floor,Room,Room_details,Housekeeper_details,Housekeeper_room_visit
# Register your models here.
admin.site.register(Admin),
admin.site.register(Housekeeper),
admin.site.register(Room_floor),
admin.site.register(Room),
admin.site.register(Room_details),
admin.site.register(Housekeeper_details),
admin.site.register(Housekeeper_room_visit),
