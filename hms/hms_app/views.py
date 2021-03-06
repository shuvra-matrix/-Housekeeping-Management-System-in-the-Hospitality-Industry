from django.utils import timezone
import pytz
from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from hms_app.models import Admin, Food_type, Housekeeper, Room_floor, Room, Room_details, Housekeeper_details, Housekeeper_room_visit, Staff, Food_quentity, Food_drinks, Food_type, Room_service, Food_order_list, Customer_complaints, Daily_activities, Housekeeping_daily_activity, Staff_type, Monthly_roster
from random import randint
from hms_app.mail import mail



def time():
    IST = pytz.timezone('Asia/Kolkata')
    datetime_ist = datetime.now(IST)
    return datetime_ist.strftime('%A, %b %Y %I:%M %p ')


def time_snd():
    IST = pytz.timezone('Asia/Kolkata')
    datetime_ist = datetime.now(IST)
    return datetime_ist.strftime('%Y%m%d')


def time_tnd():
    IST = pytz.timezone('Asia/Kolkata')
    datetime_ist = datetime.now(IST)
    return datetime_ist.strftime('%Y-%m-%d')





def login(request):
    if request.session.has_key('login'):
        return redirect("/")
    else:
        if request.method == "POST":
            message = ""
            if request.POST.get("user_type") == "Admin":
                user_email = request.POST.get("user_email")
                user_password = request.POST.get("password")
                user_count = Admin.objects.filter(admin_email=user_email).count()
                if user_count > 0:
                    user_details = Admin.objects.get(admin_email=user_email)
                    if user_password == user_details.admin_password :
                        request.session['login'] = "login"
                        request.session['id'] = user_details.id
                        request.session['admin_id'] = user_details.id
                        request.session['name'] = user_details.admin_name
                        return redirect("/")
                    else:
                        message = "Invalid Credentials"
                        my_dict ={
                            "message":message,
                        }
                        return render(request, "other/login.html",context=my_dict)
                else:
                    message = "Invalid Credentials"
                    my_dict = {
                        "message": message,
                    }
                    return render(request, "other/login.html", context=my_dict)
                
                
                
            if request.POST.get("user_type") == "Staff":
                user_email = request.POST.get("user_email")
                user_password = request.POST.get("password")
                user_count = Staff.objects.filter(staff_email=user_email).count()
                if user_count > 0:
                    user_details = Staff.objects.get(staff_email=user_email)
                    if user_password == user_details.staff_password:
                        request.session['id'] = user_details.id
                        request.session['name'] = user_details.staff_name
                        request.session['staff_type'] = user_details.staff_type.staff_type
                        if user_details.staff_type.staff_type == "Executive Housekeeper" or user_details.staff_type.staff_type == "Deputy Housekeeper":
                            request.session['login'] = "login"
                            request.session['admin_id'] = "admin_id"
                        elif user_details.staff_type.staff_type == "Control desk supervisor":
                            request.session['login'] = "login"
                        else:
                            message = "Invalid Credentials"
                            my_dict = {
                                "message": message,
                            }
                            return render(request, "other/login.html", context=my_dict)
                            
                        return redirect("/")
                    else:
                        message = "Invalid Credentials"
                        my_dict = {
                            "message": message,
                        }
                        return render(request, "other/login.html", context=my_dict)
                else:
                    message = "Invalid Credentials"
                    my_dict = {
                        "message": message,
                    }
                    return render(request, "other/login.html", context=my_dict)
                
                
            if request.POST.get("user_type") == "Housekeeper":
                user_email = request.POST.get("user_email")
                user_password = request.POST.get("password")
                user_count = Housekeeper.objects.filter(housekeeper_email=user_email).count()
                if user_count > 0:
                    user_details = Housekeeper.objects.get(housekeeper_email=user_email)
                    if user_password == user_details.housekeeper_password:
                        request.session['login'] = "login"
                        request.session['housekeeper_id'] = user_details.id
                        request.session['housekeepr_name'] = user_details.housekeeper_name
                        return redirect("/index")
                    else:
                        message = "Invalid Credentials"
                        my_dict = {
                            "message": message,
                        }
                        return render(request, "other/login.html", context=my_dict)
                else:
                    message = "Invalid Credentials"
                    my_dict = {
                        "message": message,
                    }
                    return render(request, "other/login.html", context=my_dict)
                
                
                
                
        return render(request, "other/login.html")

def logout(requests):
    if requests.session.has_key('login'):
        try:
            for key in list(requests.session.keys()):
                del requests.session[key]
            return render(requests, 'other/login.html')
        except:
            pass
    else:
        return render(requests, 'other/login.html')


def index(requests):



    if requests.session.has_key('login'):
        total_room = Room.objects.all().count()
        cleaned = Room_details.objects.filter(room_inspect_status="Inspected").count()
        dirty = Room_details.objects.filter(room_inspect_status="Dirty").count()
        out_of_serviced = Room_details.objects.filter(room_status="Out-of-Service").count()
        out_of_order = Room_details.objects.filter(room_status="Out-of-Order").count()
        available_room = Room_details.objects.filter(room_occupancy="Vacant").count()
        not_available_room = Room_details.objects.filter(room_occupancy="Occupied").count()
        housekeeper = Housekeeper_details.objects.filter(housekeeper_status="Available").count()
        name = requests.session.get("name").title()
        if requests.session.has_key("staff_type"):
            staff_type = requests.session.get("staff_type")
        else:
            staff_type = "staff_type"
        my_dict={
            "staff_type":staff_type,
            "total_room": total_room,
            "cleaned": cleaned,
            "dirty": dirty,
            "name":name,
            "out_of_serviced": out_of_serviced,
            "out_of_order": out_of_order,
            "available_room": available_room,
            "not_available_room": not_available_room,
            "housekeeper": housekeeper,
        }
        
        return render(requests , 'admins/index.html',context=my_dict)
    else:
        return render(requests, 'other/login.html')

def room_status(requests):
    if requests.session.has_key('login'):
        room_data = Room_details.objects.all()
        
        my_dict = { 
                    "time" : time(),           
                    "room_data": room_data,                     
                }
        return render(requests, 'admins/room_status.html', context=my_dict)
    else:
        return render(requests, 'other/login.html')

def room_manage(request):
    if request.session.has_key('login'):
        if request.method == "POST":
            room_data_id = request.POST.get('room_data_id')
            room_data = Room_details.objects.all().filter(id=room_data_id)
            Housekeeper_data = Housekeeper_details.objects.all().filter(housekeeper_status='Available')
            my_dict = {
                "room_data": room_data,
                "Housekeeper_data": Housekeeper_data,
            }
            return render(request, 'admins/room_manage.html',context=my_dict)
        return redirect("/room_status")
    else:
        return render(request, 'other/login.html')

    
def room_update(request):
    if request.method == "POST":
        room_id = request.POST.get("room_id")
        room_inspection = request.POST.get("room_inspected")
        room_note = request.POST.get("room_note")
        room_status = request.POST.get("room_status")
        housekeeper_id = request.POST.get("housekeeper_id")
        updated_by = request.session.get("name")
        update_data = Room_details.objects.filter(room_id=room_id).update(room_inspect_status=room_inspection, room_notes=room_note, room_housekeeper=housekeeper_id, room_status=room_status,room_updated_by=updated_by,room_updated_time=time())
        update_housekeeper_data = Housekeeper_details.objects.filter(housekeeper_id=housekeeper_id).update(housekeeper_status="Occupied")
        housekeepr_data = Housekeeper.objects.get(id=housekeeper_id)
        room_data = Room.objects.get(room_id=room_id)
        
        create_housekeeper_room = Housekeeper_room_visit.objects.create(housekeeper_id=housekeepr_data,room_id=room_data)
        return redirect("/room_status")


def housekeepers_manage(request):
    if request.session.has_key('login'):
        housekeeper = Housekeeper_details.objects.all()
        my_dict = {
            "time": time(),
            "housekeeper":housekeeper,
        }
        return render(request, "admins/housekeeper.html",context=my_dict)
    else:
        return render(request, 'other/login.html')


def add_housekeeper(request):
    if request.session.has_key('login'):
        if request.method =="POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            contact_number = request.POST.get('number')
            housekeeper_id = request.POST.get('id')
            password = randint(123654, 986545)
            position = "Housekeeper"
            insert_value = Housekeeper.objects.create(housekeeper_name=name,housekeeper_email=email,housekeeper_mobile=contact_number,housekeeper_id=housekeeper_id,housekeeper_password=password)
            get_value = Housekeeper.objects.get(housekeeper_id=housekeeper_id)
            insert_new_value = Housekeeper_details.objects.create(housekeeper_id=get_value,housekeeper_status="Available")
            emails = mail(email,password,name,position)
            if emails == "0":
                message = "Housekeeper Add Successfully"
                return render(request, 'admins/housekeeper.html', {'message': message})
            elif emails == "1":
                message = "Invalid Email Address"
                return render(request, 'admins/housekeeper.html', {'message': message})

        return render(request, "admins/add_housekeeper.html")
    else:
        return render(request, 'other/login.html')


def housekeeper_details(request):
    if request.session.has_key('login'):
        if request.method == "POST":
            housekeeper_id = request.POST.get("housekeeper_id")
            housekeeper_data = Housekeeper.objects.all().filter(id=housekeeper_id)
            housekeeper_room_data = Housekeeper_room_visit.objects.all().order_by("id").filter(housekeeper_id=housekeeper_id)[0:1]
            housekeeper_room_data_count = Housekeeper_room_visit.objects.all().filter(housekeeper_id=housekeeper_id).count()
            if housekeeper_room_data_count > 0:
                my_dict = {
                    "housekeeper_data": housekeeper_data,
                    "housekeeper_room_data": housekeeper_room_data,
                }
            else:
                my_dict = {
                    "housekeeper_data": housekeeper_data,
                }
                
            return render(request, "admins/housekeeper_details.html",context=my_dict)
        return redirect("/housekeepers")
    else:
        return render(request, 'other/login.html')
    
def housekeeper_update(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('number')
        housekeeper_id = request.POST.get('house_id')
        update_data = Housekeeper.objects.filter(id=id).update(housekeeper_name=name,housekeeper_email=email,housekeeper_id=housekeeper_id,housekeeper_mobile=contact_number)
        return redirect("/housekeepers")
        
         
def housekeeper_delete(request):
    if request.method == "POST":
        id = request.POST.get("housekeeper_id")
        print(id)
        delete_housekeeper = Housekeeper.objects.filter(id=id).delete()
        return redirect("/housekeepers")


def rooms_and_floor(request):
    if request.session.has_key('admin_id'):
        room_data = Room.objects.all()
        floor_data = Room_floor.objects.all()
        my_dict = {
            "time": time(),
            "room_data": room_data,
            "floor_data": floor_data,
        }
        
        return render(request, "admins/rooms_and_floor.html",context=my_dict)
    else:
        return render(request, 'other/login.html')
    

def add_room_floor(request):
    if request.session.has_key('admin_id'):
        if request.method == "POST":
            if request.POST.get("room") == "room":
                floor_details = Room_floor.objects.all()
                my_dict = {
                    "room_floor_data":floor_details,
                }
                return render(request, "admins/add_room_floor.html",context=my_dict)
            elif request.POST.get("add_room") == "add_room":
                floor_id = request.POST.get("floor_id")
                room_name = request.POST.get("room_name")
                room_type = request.POST.get("room_type")
                floor_details = Room_floor.objects.get(floor_id=floor_id)
                create_room = Room.objects.create(floor_id=floor_details,room_name=room_name)
                admin_data = Admin.objects.get(id="3")
                create_room_data = Room_details.objects.create(room_id=create_room,room_type=room_type,room_updated_by=admin_data)
                return redirect("/rooms_and_floor")
            elif request.POST.get("floor") == "floor":
                floor = "floor"
                my_dict = {
                    "floor" : floor,
                }
                return render(request, "admins/add_room_floor.html",context=my_dict)
            elif request.POST.get("add_floor") == "add_floor":
                floor_name = request.POST.get("floor_name")
                crete_floor = Room_floor.objects.create(floor_name=floor_name)
                return redirect("/rooms_and_floor")
            elif request.POST.get("update_floor") == "update_floor":
                floor_id = request.POST.get("floor_id")
                floor_details = Room_floor.objects.all().filter(floor_id=floor_id)
                my_dict = {
                    "floor_update_id" : floor_details
                }
                return render(request, "admins/add_room_floor.html", context=my_dict)
                
            elif request.POST.get("floor_data_update") == "floor_data_update":
                print("update")
                floor_id = request.POST.get("floor_id")
                floor_name = request.POST.get("floor_name")
                update = Room_floor.objects.filter(floor_id=floor_id).update(floor_name=floor_name) 
                return redirect("/rooms_and_floor")
            
            elif request.POST.get("delete_floor") == "delete_floor":
                floor_id = request.POST.get("floor_id")
                delete_floor = Room_floor.objects.filter(floor_id=floor_id).delete()
                return redirect("/rooms_and_floor")
            elif request.POST.get("update_room") == "update_room":
                room_id = request.POST.get("room_id")
                room_data = Room.objects.all().filter(room_id=room_id)
                floor_details = Room_floor.objects.all()
                room_details = Room_details.objects.all().filter(room_id=room_id)
                my_dict = {
                    "room_floor_data_update": floor_details,
                    "room_data_update" : room_data,
                    "room_details":room_details,
                }
                return render(request, "admins/add_room_floor.html", context=my_dict)
            elif request.POST.get("update_room_data") == "update_room_data":
                room_id = request.POST.get("room_id")
                floor_id = request.POST.get("floor_id")
                floor_details = Room_floor.objects.get(floor_id=floor_id)
                room_name = request.POST.get("room_name")
                room_type = request.POST.get("room_type")
                update_room_data = Room.objects.filter(room_id=room_id).update(floor_id=floor_details,room_name=room_name)
                update_room_status = Room_details.objects.filter(room_id=room_id).update(room_type=room_type)
                return redirect("/rooms_and_floor")
            elif request.POST.get("delete_room") == "delete_room":
                room_id = request.POST.get("room_id")
                delete_room = Room.objects.filter(room_id=room_id).delete()
                return redirect("/rooms_and_floor")
        return redirect("/rooms_and_floor")
    else:
        return render(request, 'other/login.html')
    




def Staff_types(request):
    staff_type = Staff_type.objects.all()
    
    my_dict = {
        "staff_type":staff_type,
        "time":time,
    }
    
    if request.method == "POST":
        if request.POST.get("add_staff") == "add_staff":
            return render(request, "admins/add_staff_type.html")
        
        elif request.POST.get("staff_type_added") == "staff_type_added":
            staff_type = request.POST.get("staff_type")
            create_staff_type = Staff_type.objects.create(staff_type=staff_type)
            return redirect("/management/staff_type")
        elif request.POST.get("update_staff_type") == "update_staff_type":
            staff_type_id = request.POST.get("staff_type_id")
            staff_type_details = Staff_type.objects.all().filter(id=staff_type_id)
            
            my_dict = {"staff_type_details":staff_type_details}
            return render(request, "admins/update_staff_type.html", context=my_dict)

        elif request.POST.get("staff_type_updated") == "staff_type_updated":
            staff_type_id = request.POST.get("staff_type_id")
            staff_type = request.POST.get("staff_type")
            update_data = Staff_type.objects.filter(id=staff_type_id).update(staff_type=staff_type)
            return redirect("/management/staff_type")
            
        elif request.POST.get("delete_staff_type") == "delete_staff_type":
            staff_type_id = request.POST.get("staff_type_id")
            print(staff_type_id)
            update_data = Staff_type.objects.filter(id=staff_type_id).delete()
            return redirect("/management/staff_type")
    
    return render(request, "admins/staff_type.html", context=my_dict)


            
def staff(request):
    if request.session.has_key('admin_id'):
        staff_details = Staff.objects.all()
        my_dict = {
            "time" : time(), 
            "staff_details": staff_details,
        }
        return render(request, "admins/staff.html",context=my_dict)
    else:
        return render(request, 'other/login.html')
    
    
def add_staff(request):
    if request.session.has_key('admin_id'):
        if request.method == "POST":
            if request.POST.get("add_staff") == "add_staff":
                staff_type = Staff_type.objects.all()
                my_dict = {"staff_type":staff_type}
                return render(request, "admins/add_staff.html",context=my_dict)
            elif request.POST.get("staff_added") == "staff_added":
                name = request.POST.get('name')
                email = request.POST.get('email')
                contact_number = request.POST.get('number')
                staff_id = request.POST.get('id')
                staff_type_id = request.POST.get("staff_type_id")
                staff_type_details = Staff_type.objects.get(id=staff_type_id)
                password = randint(123654, 986545)
                add_staff = Staff.objects.create(staff_name=name,staff_email=email,staff_id=staff_id,staff_mobile=contact_number,staff_password=password,staff_type= staff_type_details)
                if staff_type_details.staff_type == "Executive Housekeeper" or staff_type_details.staff_type == "Deputy Housekeeper" or staff_type_details.staff_type == "Control desk supervisor":
                    emails = mail(email, password, name, staff_type_details.staff_type)
                return redirect("/staff")
        
    else:
        return render(request, 'other/login.html')
    

def edit_staff(request):
    if request.session.has_key('admin_id'):
        if request.method == "POST":
            if request.POST.get("update_staff") == "update_staff":
                staff_id = request.POST.get("staff_id")
                staff_type = Staff_type.objects.all()
                staff_details = Staff.objects.all().filter(id=staff_id)
                my_dict = {
                    "staff_type": staff_type,
                    "staff_details":staff_details,
                }
                return render(request, "admins/update_staff.html",context=my_dict)
                
                pass
            elif request.POST.get("staff_delete") == "staff_delete":
                id = request.POST.get("staff_id")
                delete_staff = Staff.objects.filter(id=id).delete()
                return redirect("/staff")
        
            elif request.POST.get("staff_updated") == "staff_updated":
                id = request.POST.get("staff_id")
                name = request.POST.get('name')
                email = request.POST.get('email')
                staff_type_id = request.POST.get("staff_type_id")
                staff_type_details = Staff_type.objects.get(id=staff_type_id)
                contact_number = request.POST.get('number')
                staff_id = request.POST.get('id')
                update_staff = Staff.objects.filter(id=id).update(staff_name=name,staff_email=email,staff_mobile=contact_number,staff_id=staff_id,staff_type=staff_type_details)
                return redirect("/staff")
        return redirect("/staff")
    else:
        return render(request, 'other/login.html')


def food(request):
    if request.session.has_key('admin_id'):
        food_type = Food_type.objects.all()
        food_drinks = Food_drinks.objects.all()
        food_quentity = Food_quentity.objects.all()
        my_dict = {
            "time" : time(), 
            "food_type":food_type,
            "food_drinks":food_drinks,
            "food_quentity":food_quentity,
        }
        return render(request,"admins/food.html",context=my_dict)
    else:
        return render(request, 'other/login.html')


def add_food(request):
    if request.session.has_key('admin_id'):
        if request.method == "POST":
            if request.POST.get("add_food_type") == "add_food_type":
                add_food_type = "add_food_type"
                my_dict = {
                    "add_food_type": add_food_type,
                }
                return render(request,"admins/add_food.html",context=my_dict)
            elif request.POST.get("added_food_type") == "added_food_type":
                food_type = request.POST.get("food_types")
                create_food_type = Food_type.objects.create(food_type=food_type)
                return redirect("/food")
            
            elif request.POST.get("add_food") == "add_food":
                food_type = Food_type.objects.all()
                my_dict = {
                    "pass_food_type" : food_type,
                }
                return render(request,"admins/add_food.html",context=my_dict)

            elif request.POST.get("added_food") == "added_food":
                food_type_id = request.POST.get("food_types_id")
                food_name = request.POST.get("food_name")
                food_types_object = Food_type.objects.get(id=food_type_id)
                create_food = Food_drinks.objects.create(food_type=food_types_object,food_name=food_name)
                return redirect("/food")


            elif request.POST.get("add_quentity") == "add_quentity":
                food_type = Food_type.objects.all()
                my_dict = {
                    "pass_quentity_food_type" : food_type,
                }
                return render(request,"admins/add_food.html",context=my_dict)
            
            elif request.POST.get("added_quentity") == "added_quentity":
                food_type_id = request.POST.get("food_types_id")
                quentity = request.POST.get("quentity")
                food_types_object = Food_type.objects.get(id=food_type_id)
                create_food = Food_quentity.objects.create(food_type=food_types_object,quentity=quentity)
                return redirect("/food")

            elif request.POST.get("update_food_type") == "update_food_type":
                food_type_id = request.POST.get("food_type_id")
                food_types = Food_type.objects.all().filter(id=food_type_id)
                all_food_type = Food_type.objects.all()
                my_dict ={
                    "updates_food_type" : food_types,
                    "all_food_type" : all_food_type,
                }
                return render(request,"admins/add_food.html",context=my_dict)
                
            elif request.POST.get("updated_food_type") == "updated_food_type":
                food_type_id = request.POST.get("food_type_id")
                food_type = request.POST.get("food_type")
                update_food_type = Food_type.objects.filter(id=food_type_id).update(food_type=food_type)
                return redirect("/food")

            elif request.POST.get("delete_food_type") == "delete_food_type":
                food_type_id = request.POST.get("food_type_id")
                delete_food_type = Food_type.objects.filter(id=food_type_id).delete()
                return redirect("/food")
            elif request.POST.get("update_food") == "update_food":
                food_id = request.POST.get("food_id")
                food_details = Food_drinks.objects.all().filter(id=food_id)
                food_types = Food_type.objects.all()
                my_dict = {
                    "food_details" : food_details,
                    "all_food_types" : food_types,
                }
                return render(request,"admins/add_food.html",context=my_dict)
            elif request.POST.get("updated_food") == "updated_food":
                food_id = request.POST.get("food_id")
                food_name = request.POST.get("food_name")
                food_types_object = Food_type.objects.get(id=food_id)
                upadte_food_data = Food_drinks.objects.filter(id=food_id).update(food_name=food_name,food_type=food_types_object)
                return redirect("/food")
            elif request.POST.get("delete_food") == "delete_food":
                food_id = request.POST.get("food_id")
                delete_data = Food_drinks.objects.filter(id=food_id).delete()
                return redirect("/food")
            elif request.POST.get("update_quentity") == "update_quentity":
                quentity_id = request.POST.get("quentity_id")
                quentity_data = Food_quentity.objects.all().filter(id=quentity_id)
                food_type_data = Food_type.objects.all()
                my_dict = {
                    "quentity_data": quentity_data,
                    "food_type_data" : food_type_data,
                }
                return render(request, "admins/add_food.html", context=my_dict)

            elif request.POST.get("updated_quentity") == "added_quentity":
                quentity_id = request.POST.get("quentity_id")
                quentity = request.POST.get("quentity")
                food_type_id = request.POST.get("food_type")
                food_types_object = Food_type.objects.get(id=food_type_id)
                update_data = Food_quentity.objects.filter(id=quentity_id).update(food_type=food_types_object,quentity=quentity)
                return redirect("/food")
            elif request.POST.get("delete_quentity") == "delete_quentity":
                quentity_id = request.POST.get("quentity_id")
                delete_quentity = Food_quentity.objects.filter(id=quentity_id).delete()
                return redirect("/food")
        return redirect("/food")
    else:
        return render(request, 'other/login.html')





def room_service(request):
    if request.session.has_key('login'):
        food_type = Food_type.objects.all()
        room_details = Room.objects.all()
        if request.method == "POST":
            if request.POST.get("food_types") == "food_types":
                del request.session['initial']
                request.session["second_initial"] = "second_initial"
                room_id = request.POST.get("room_id")
                room_details = Room.objects.all().filter(room_id=room_id)
                request.session["room_id"] = room_id
                food_type_id = request.POST.get("food_type")
                food_type_details = Food_type.objects.all().filter(id=food_type_id)
                select_food = Food_drinks.objects.all().filter(food_type=food_type_id)
                request.session['food_type_id'] = food_type_id
                for i in food_type_details:
                    request.session['food_type_name'] = i.food_type
                if request.session.has_key('room_id'):
                    room_id = request.session.get("room_id")
                    list_data = Food_order_list.objects.all().filter(
                        room=room_id).filter(show_list="yes")
                else:
                    list_data = None
                my_dicts = {
                    "list_data": list_data,
                    "room_details": room_details,
                    "select_food":select_food,
                    "food_type_details": food_type_details,
                    "time": time(),
                }
                return render(request, "admins/add_room_service.html", context=my_dicts)
        
            elif request.POST.get("foods") == "foods":
                del request.session["second_initial"]
                food_id = request.POST.get("food")
                request.session['food_drinks_id'] = food_id
                room_id = request.session.get("room_id")
                room_details = Room.objects.all().filter(room_id=room_id)
                food_type_id = request.session.get("food_type_id")
                food_details = Food_drinks.objects.all().filter(id=food_id)
                food_type_details = Food_type.objects.all().filter(id=food_type_id)
                for i in food_type_details:
                    food_quentity_details = Food_quentity.objects.all().filter(food_type=i.id)
                
                    request.session['foods'] = "foods"
                    request.session['third_initial'] = "third_initial"
                    if request.session.has_key('room_id'):
                        room_id = request.session.get("room_id")
                        list_data = Food_order_list.objects.all().filter(
                            room=room_id).filter(show_list="yes")
                    else:
                        list_data = None
                    dicts = {
                        "list_data": list_data,
                        "room_details": room_details,
                        "food_type_details":food_type_details,
                        "food_details": food_details,
                        "food_quentity_details": food_quentity_details,
                        "time": time(),
                        
                    }

                    return render(request, "admins/add_room_service.html", context=dicts)
                
            elif request.POST.get("food_quentity") == "food_quentity":
                food_quentity_id = request.POST.get("foods_quentity")
                request.session['quantity'] = food_quentity_id
                room_id = request.session.get("room_id")
                food_type_id = request.session.get('food_type_id') 
                food_id = request.session.get('food_drinks_id')
                room_details = Room.objects.get(room_id=room_id)
                food_details = Food_drinks.objects.get(id=food_id)
                food_quentiry = Food_quentity.objects.get(id=food_quentity_id)
                create_data = Food_order_list.objects.create(room=room_details,food_name=food_details,quentity=food_quentiry)
                
                return redirect("/room_service")
            
            elif request.POST.get("delete_list") == "delete_list":
                list_id = request.POST.get("list_id")
                delete_list = Food_order_list.objects.filter(id=list_id).delete()
                return redirect("/room_service")
            
        if request.session.has_key('room_id'):
            room_id = request.session.get("room_id")
            list_data = Food_order_list.objects.all().filter(room=room_id).filter(show_list="yes")
        else:
            list_data = None

        my_dict = {
            "list_data": list_data,
            "room_details": room_details,
            "food_type": food_type,
            "time": time(),
        }
    
        request.session['initial'] = "initial"
        request.session['second_initial'] = "second_initial"
        request.session['third_initial'] = "third_initial"
        request.session['show'] = "show"
        return render(request,"admins/add_room_service.html",context=my_dict)
    else:
        return render(request, 'other/login.html')



def place_order(request):
   
    if request.session.has_key('login'):
        room_id = request.session.get("room_id")
        list_data = Food_order_list.objects.all().filter(room=room_id)
        
        for i in list_data:
            food_id = request.session.get('food_drinks_id')
            room_details = Room.objects.get(room_id=room_id)
            updated_by = request.session.get("name")
            if request.session.get("show") == "show":
                create_data = Room_service.objects.create(
                    room_id=room_details, food_list_id= i , order_taken_by=updated_by, time=time(),show_details="yes")
            else:
                create_data = Room_service.objects.create(
                    room_id=room_details, food_list_id=i, order_taken_by=updated_by, time=time(), show_details="no")
            request.session['show'] = "not_show"
            update_list = Food_order_list.objects.filter(id=i.id).update(show_list="no")
            
            
        del request.session["quantity"]
        del request.session["food_type_id"]
        del request.session["food_drinks_id"]
        del request.session["room_id"]
        del request.session['show']
        return redirect("/room_service")
    else:
        return render(request, 'other/login.html')

def view_room_service(request):
    if request.session.has_key('login'):
        room_service = Room_service.objects.all().filter(show_details="yes")
        my_dict = {
            "room_service": room_service,
            "time":time,
        }
        if request.method == "POST":
            if request.POST.get("back") == "back":
                pass
            else:
                room_id = request.POST.get("room_id")
                food_list = Room_service.objects.all().filter(
                    room_id=room_id).filter(order_status="Under-Cooking")
                my_dict = {
                    "food_list": food_list,
                }
                return render(request, "admins/view_ordered_food.html", context=my_dict)
            
            
            
        
        return render(request, "admins/view_room_service.html", context=my_dict)
    else:
        return render(request, 'other/login.html')



def complaint(request):
    if request.session.has_key('login'):
        complaint = Customer_complaints.objects.all()
        my_dict = {
            "complaint":complaint,
            "time":time(),
        }
        
        if request.method == "POST":
            if request.POST.get("add_complaint") == "add_complaint":
                room_details = Room.objects.all()
                my_dict = {
                    "room_details":room_details,
                }
                
                return render(request, "admins/add_complaint.html", context=my_dict)
                
            elif request.POST.get("com_add") == "com_add":
                room_id = request.POST.get("room_id")
                room_details = Room.objects.get(room_id=room_id)
                
                customer_name = request.POST.get("customer_name")
                complaint = request.POST.get("complaint")
                updated_by = request.session.get("name")
                create_complaints = Customer_complaints.objects.create(room_id=room_details,complaints=complaint,complaints_by=customer_name,complaints_taken_by=updated_by,time=time())
                return redirect("/other_service/customer_complaint")
                
            elif request.POST.get("complaint_update") == "complaint_update":
                complaint_id = request.POST.get("complaint_id")
                complaints_details = Customer_complaints.objects.all().filter(id=complaint_id)
            
                my_dict = {
                    "complaints_details": complaints_details,
                
                }
                return render(request, "admins/update_complaints.html", context=my_dict)
            elif request.POST.get("com_up") == "com_up":
                com_id = request.POST.get("com_id")
                com_status = request.POST.get("com_status")
                update_com = Customer_complaints.objects.filter(
                    id=com_id).update(status=com_status)
                
                return redirect("/other_service/customer_complaint")
                
        
        return render(request, "admins/complaint.html" , context=my_dict)
    else:
        return render(request, 'other/login.html')


def dealy_activities(request):
    if request.session.has_key('admin_id'):
        dealy_activities = Daily_activities.objects.all()
        my_dict = {
            "time": time(),
            "dealy_activities": dealy_activities,
        }
        
        if request.method == "POST":
            if request.POST.get("add_activity") == "add_activity":
                return render(request, "admins/add_activity.html")
            
            if request.POST.get("activity_added") == "activity_added":
                activity = request.POST.get("activity")
                activity_create = Daily_activities.objects.create(activity=activity)
                return redirect("/other_service/daily_activities")
            
            if request.POST.get("up_activity") == "up_activity":
                activity_id = request.POST.get("activity_id")
                activity_details = Daily_activities.objects.all().filter(id=activity_id)
                my_dict = {
                    "dealy_activities": activity_details,
                }
                return render(request, "admins/update_activity.html", context=my_dict)
            if request.POST.get("activity_updated") == "activity_updated":
                activity_id = request.POST.get("activity_id")
                activity = request.POST.get("activity")
                update_activity = Daily_activities.objects.filter(id=activity_id).update(activity=activity)
                return redirect("/other_service/daily_activities")
            if request.POST.get("delete_activity") == "delete_activity":
                activity_id = request.POST.get("activity_id")
                update_activity = Daily_activities.objects.filter(id=activity_id).delete()
                return redirect("/other_service/daily_activities")
        
        return render(request, "admins/daily_activities.html" , context=my_dict)

    else:
        return render(request, 'other/login.html')


def housekeeping_daily_activity(request):
    if request.session.has_key('login'):
        activity = Daily_activities.objects.exclude(time=time_snd())
        activity_count = Daily_activities.objects.exclude(time=time_snd()).count()
        if activity_count == 0:
            activity = "All Activity Done For Today"
            my_dict = {
                "time": time(),
                "dealy": activity,
                
            }
        else:
            my_dict = {
                "time": time(),
                "dealy_activities": activity,

            }
        
        if request.method == "POST":
            if request.POST.get("submit_activity") == "submit_activity":
                activity_id = request.POST.get("activity_id")
                update_activity = Daily_activities.objects.filter(
                    id=activity_id).update(time=time_snd())
                activity_details = Daily_activities.objects.get(id=activity_id)
                create_housekeeper_activity = Housekeeping_daily_activity.objects.create(activity=activity_details,time=time_snd())
                return redirect("/housekeeping_daily_activity")
                
                
        return render(request, "admins/housekeeping_daily_activity.html", context=my_dict)
    else:
        return render(request, 'other/login.html')


def monthly_roster(request):
    if request.session.has_key('login'):
        if request.method == "POST":
            if request.POST.get("add_monthly_roster") == "add_monthly_roster":
                staff_type = Staff_type.objects.all()
                request.session["first"] = "first"
                my_dict = {
                    "staff_type": staff_type,
                }
                return render(request, "admins/add_monthly_roster.html",  context=my_dict)
            
            if request.POST.get("staff_type") == "staff_type":
                del request.session["first"]
                request.session["second"] = "second"
                staff_type_id = request.POST.get("staff_type_id")
                print(staff_type_id)
                staff_type = Staff_type.objects.all().filter(id=staff_type_id)
                print(staff_type)
                for i in staff_type:
                    staff_name_details = Staff.objects.all().filter(staff_type=i)
                
                my_dict = {
                    "time": time_tnd(),
                    "staff_type": staff_type,
                    "staff_name_details": staff_name_details,
                }
                return render(request, "admins/add_monthly_roster.html",  context=my_dict)
            
            if request.POST.get("all_submit") == "all_submit":
                del request.session["second"]
                staff_type_id = request.POST.get("staff_type_id")
                staf_name_id = request.POST.get("staf_name_id")
                date_from = request.POST.get("date_from")
                date_to = request.POST.get("date_to")
                time_from = request.POST.get("time_from")
                time_to = request.POST.get("tome_to")
                
                staf_type_details = Staff_type.objects.get(id=staff_type_id)
                staff_details = Staff.objects.get(id=staf_name_id)
                updated_by = request.session.get("name")
                create_monthly_roster = Monthly_roster.objects.create(
                    staff_type=staf_type_details, staff_name=staff_details, date_from=date_from, date_to=date_to, time_from=time_from, time_to=time_to, update_time=time(), update_by=updated_by)
                return redirect("/other_service/monthly_roster")
            if request.POST.get("update_monthly_roster") == "update_monthly_roster":
                roster_id = request.POST.get("id")
                monthly_roster = Monthly_roster.objects.all().filter(id=roster_id)
                my_dict = {
                    "monthly_roster": monthly_roster,
                }
                return render(request, "admins/update_monthly_roster.html", context=my_dict)
            if request.POST.get("staff_up") == "staff_up":
                roster_id = request.POST.get("id")
                date_from = request.POST.get("date_from")
                date_to = request.POST.get("date_to")
                time_from = request.POST.get("time_from")
                time_to = request.POST.get("tome_to")
                updated_by = request.session.get("name")
                monthly_roster = Monthly_roster.objects.filter(id=roster_id).update(date_from=date_from,date_to=date_to,time_from=time_from,time_to=time_to,update_by=updated_by,update_time=time())
                return redirect("/other_service/monthly_roster")
            
            if request.POST.get("delete_monthly_roster") == "delete_monthly_roster":
                roster_id = request.POST.get("id")
                monthly_roster = Monthly_roster.objects.filter(id=roster_id).delete()
                return redirect("/other_service/monthly_roster")
            
        monthly_roster = Monthly_roster.objects.all()
        my_dict = {
            "monthly_roster":monthly_roster,
            "time":time(),
        }

        return render(request, "admins/monthly_roster.html", context=my_dict)
    else:
        return render(request, 'other/login.html')


def housekeeper_index(request):
    if request.session.has_key('login'):
        if request.method != "POST":
            user_id = request.session.get('housekeeper_id')
            user_name = request.session.get('housekeepr_name')
            housekeeper = Housekeeper.objects.get(id=user_id)
            housekeeper_room_visit = Housekeeper_room_visit.objects.all().filter(
                housekeeper_id=housekeeper).order_by("-id")[0:1]
            for i in housekeeper_room_visit:
                room_details = Room_details.objects.all().filter(room_id=i.room_id)
                room_details_count =  Room_details.objects.all().filter(room_id=i.room_id).count()

                if room_details_count > 0 :
                    my_dict = {
                        "name": user_name,
                        "housekeeper_room_visit": room_details,
                    }
                    return render(request, "housekeeper/index.html",context= my_dict)

            my_dict = {
                        "name": user_name,
                    }
        if request.method == "POST":
            if request.POST.get("room") == "room":
                room_id = request.POST.get("room_data_id")
                user_id = request.session.get('housekeeper_id')
                housekeeper = Housekeeper.objects.get(id=user_id)
                housekeeper_room_visit = Housekeeper_room_visit.objects.all().filter(
                housekeeper_id=housekeeper).order_by("-id")[0:1]
                for i in housekeeper_room_visit:
                    room_details = Room_details.objects.all().filter(room_id=i.room_id)
                room_details = Room_details.objects.all().filter(room_id=i.room_id)
                my_dict = {
                    "time":time(),
                    "room_details": room_details,
                }

                return render(request, "housekeeper/update_room_data.html", context=my_dict)

            if request.POST.get("update_data") == "update_data":
                room_details_id = request.POST.get("room_details_id")
                room_id = request.POST.get("room_id")
                room_inspected = request.POST.get("room_inspected")
                housekeeper_note = request.POST.get("housekeeper_note")
                user_id = request.session.get('housekeeper_id')
                user_name = request.session.get('housekeepr_name')
                housekeeper = Housekeeper.objects.get(id=user_id)
                update_room_details = Room_details.objects.filter(id=room_details_id).update(room_inspect_status=room_inspected,room_housekeeper_note=housekeeper_note,room_updated_by=user_name,room_updated_time=time())
                update_houkeeing_status = Housekeeper_details.objects.filter(
                    housekeeper_id=housekeeper).update(housekeeper_status="Available")
                return redirect("/index")

        return render(request, "housekeeper/index.html",context= my_dict)
    else:
        return render(request, 'other/login.html')