from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Booked_turf, Contact, Manager_Requests, Turf, Users

# Create your views here.
def get_user(request):
    try:
        email = request.COOKIES['email']        
        user = Users.objects.get(email = email)
        return user
    except:
        return False
    
def bookturf(request):
    user = get_user(request)
    if request.method == 'POST':
        slot = request.POST.get('slot')
        price = int(request.POST.get('price'))
        location =request.POST.get('location')
        turf_name = request.POST.get('turf_name')
        turf = Turf.objects.get(turf_name = turf_name)
        if Booked_turf.objects.filter(turf_name = turf_name).exists():
            return render(request,"b_failed.html")
        booked_turf = Booked_turf.objects.create(email = user.email,turf_name=turf_name,slot = slot,price=price,location =location,contact = int(turf.contact))
        booked_turf.save()
        return render(request,"b_success.html")
    return redirect(home)

def login(request):
    user = get_user(request)
    if user:
        return redirect(home)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')


        if email =='':
            login_status = 'Email field cannot be empty'
            return render(request,'login.html',{'login_status':login_status})
        if password =='':
            login_status = 'Pasword field cannot be empty'
            return render(request,'login.html',{'login_status':login_status})
        print(email,password)
        if Users.objects.filter(email = email,password = password).exists():
            response = redirect(home)
            response.set_cookie('email',email)
            return response
        
        else:
            login_status = 'user not found'
            return render(request,'login.html',{'login_status':login_status})
    return render(request,'login.html')

def logout(request):
    user = get_user(request)
    response = redirect(home)
    response.delete_cookie('email')
    return response
def manage(request):
    user = get_user(request)
    if request.method == 'POST':
        request =  Manager_Requests.objects.create(user = user)
        request.save()
        user.manager_status = 'Pending'
        user.save()
        return redirect(profile)
    if user:
        turfs = Turf.objects.filter(user_email = user.email)
        return render(request,"manage.html",{'turfs':turfs})
    else:
        return redirect(login)
def add_turf(request):
    user = get_user(request)
    if user:
        if request.method == 'POST':

            user_email = request.POST.get('user_email')
            turf_name = request.POST.get('turf_name')
            if turf_name:
                pass
            else:
                print('failed turf name')
                return redirect(add_turf)
            location = request.POST.get('location')
            if location:
                pass
            else:
                print('failed location')
                return redirect(add_turf)
            price = request.POST.get('price')
            if price:
                pass
            else:
                print('failed price')
                return redirect(add_turf)
            
            image = request.FILES.get('image')
            if image:
                pass
            else:
                print('failed image')
                return redirect(add_turf)
            
            description = request.POST.get('description')
            if description:
                pass
            else:
                print('failed description')
                return redirect(add_turf)
            start = request.POST.get('start')
            if start:
                pass
            else:
                print('failed start')
                return redirect(add_turf)
            end = request.POST.get('end')
            if end:
                pass
            else:
                print('failed end')
                return redirect(add_turf)
            turf_size = request.POST.get('turf_size')
            if turf_size:
                pass
            else:
                print('failed size')
                return redirect(add_turf)
            contact = request.POST.get('contact')
            if contact:
                pass
            else:
                print('failed contact')
                return redirect(add_turf)
            
            print('done')
            new_turf = Turf.objects.create(turf_name = turf_name,location=location,price=price,turf_image= image,description=description,start='10:2',end='10:4',turf_size=turf_size,contact=contact,user_email=user_email)
            new_turf.save()

            return HttpResponse('saved')
        return render(request, 'add_turf.html',{'user':user})
    else:
        return redirect(login)
def index(request):
    user = get_user(request)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        available_turf = Turf.objects.all()
        users = Users.objects.all()
        for user in users:
            print(user.email,email)
            if user.email == email:
                if user.password == password:
                    return render(request,'home.html',{'user':user,'turf':available_turf})
                login_status = "wrong password"
                break
            login_status = 'email does not exist'
        return render(request,'index.html',{'login_status':login_status})
    return render(request,'index.html',{'login_status':False})

def home(request):
    user = get_user(request)
    dict_turf={
        'turf': Turf.objects.all(),
        'user':user
    }
    return render(request,'home.html',dict_turf)
    
def profile(request):
    user = get_user(request)
    if user:
        email= request.COOKIES['email']
        user= Users.objects.get(email  = email)
        booked_turf = Booked_turf.objects.filter(email = email)
        return render(request,'profile.html',{'user':user,'booked_turf':booked_turf})
    return redirect(login)
def delete(request,turf_name):
    user = get_user(request)
    # print(turf_name)
    myturf = Booked_turf.objects.filter(turf_name = turf_name).delete()
    # print(myturf.turf_name)
    
    return redirect(profile)

def contact(request):
    user = get_user(request)
    if request.method == 'POST':
        new_contact = Contact.objects.create(name = request.POST.get('name'),email = request.POST.get('email'),subject =request.POST.get('subject'),message = request.POST.get('message'))
        new_contact.save()
        return redirect(home)
    if user:
        return render(request,'contact.html',{'user':user})
    return redirect(login)

def register(request):
    user = get_user(request)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        psw_repeat = request.POST.get('psw-repeat')

        if name == '':
            user_status = 'name field cannot be empty'
            return render(request,'reg.html',{'user_status':user_status})
        if phone_no == '':
            user_status = 'phone number field cannot be empty'
            return render(request,'reg.html',{'user_status':user_status})
        if email == '':
            user_status = 'email field cannot be empty'
            return render(request,'reg.html',{'user_status':user_status})
        if psw == '':
            user_status = 'password field cannot be empty'
            return render(request,'reg.html',{'user_status':user_status})
        if psw_repeat == '':
            user_status = 'retry password field cannot be empty'
            return render(request,'reg.html',{'user_status':user_status})

        if psw != psw_repeat:
            user_status = "Password does not match"
            return render(request,'reg.html',{'user_status':user_status})

        users   = Users.objects.all()
        user_status = False
        for user in users:
            if user.email == email:
                user_status = 'Email already exist   '
                return render(request,'reg.html',{'user_status':user_status})
        if user_status is False:
            newuser = Users.objects.create(name = name,phone_no =phone_no,email = email,password=psw)
            newuser.save()
            print("user created")
            return render(request,'b_success.html')
        
    return render(request,'reg.html',{'user_status':False})

def book(request,id):
    user = get_user(request)
    if user:
        turf = Turf.objects.get(id=id)
        return render(request,'book.html',{'turf':turf,'user':user})
    return redirect(login)

def edit_turf(request,id):
    user = get_user(request)
    if user:
        if request.method == 'POST':

            user_email = request.POST.get('user_email')
            turf_name = request.POST.get('turf_name')
            if turf_name:
                pass
            else:
                print('failed turf name')
                return redirect(add_turf)
            location = request.POST.get('location')
            if location:
                pass
            else:
                print('failed location')
                return redirect(add_turf)
            price = request.POST.get('price')
            if price:
                pass
            else:
                print('failed price')
                return redirect(add_turf)
            
            image = request.FILES.get('image')
            if image:
                pass
            else:
                print('failed image')
                return redirect(add_turf)
            
            description = request.POST.get('description')
            if description:
                pass
            else:
                print('failed description')
                return redirect(add_turf)
            start = request.POST.get('start')
            if start:
                pass
            else:
                print('failed start')
                return redirect(add_turf)
            end = request.POST.get('end')
            if end:
                pass
            else:
                print('failed end')
                return redirect(add_turf)
            turf_size = request.POST.get('turf_size')
            if turf_size:
                pass
            else:
                print('failed size')
                return redirect(add_turf)
            contact = request.POST.get('contact')
            if contact:
                pass
            else:
                print('failed contact')
                return redirect(add_turf)
            
            print('done')
            new_turf = Turf.objects.get(id = id)
            new_turf.turf_name = turf_name
            new_turf.location=location
            new_turf.price=price
            new_turf.turf_image= image
            new_turf.description=description
            new_turf.start='10:2'
            new_turf.end='10:4'
            new_turf.turf_size=turf_size
            new_turf.contact=contact
            new_turf.user_email=user_email
            new_turf.save()
            return redirect(home)

    turf = Turf.objects.get(id=id)
    return render(request,'edit_turf.html',{'turf':turf})