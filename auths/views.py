from django.shortcuts import render
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
# Create your views here.


@csrf_exempt
def signup(request):

    if request.method == 'POST':

        name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password = request.POST.get('password')

        if not all([name,last_name,email,age,password]):

            messages.warning(request,'All field are required')

        if CustomUser.objects.filter(email = email).exists():

            messages.error(request,"User with this email Already exist")

        # Create new User

        try:

            new_user = CustomUser.objects.create(

                first_name = name,
                last_name = last_name,
                email = email,
                age = age,
                password = make_password(password)


            )

            # Config User_name

            new_user.username = f'{name} {last_name}'
            new_user.save()

            # authentication

            new_user = authenticate(request,username = new_user.username,email = email,password=password)

            #Login new_user
            
            if new_user is not None:

                login(request,new_user)
                messages.success(request,'Success Login')

        
        except Exception as e:

            messages.error(request,str(e))

    
    return render(request,'signup.html')


@csrf_exempt
def signin(request):

    if request.user.is_authenticated:

        messages.warning(request,'You are already LoggedIn')

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        try:

            CustomUser.objects.get(emaill =email)
            user = authenticate(request,email=email,password=password)

            if user is not None:

                login(request,user)
                messages.success("You are LoggedIn")

        
        except:

            messages.error(request,'User with this email does not exist')

    
    return render(request,'signin.html')



@csrf_exempt
def logout(request):

    logout(request)
    messages.success(request,'Success logout')



class CustomPasswordResetView(auth_views.PasswordResetView):

    template_name = 'auths/password_reset_form.html'
    email_template_name = 'auths/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')


class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):

    template_name = 'auths/password_reset_done.html'



class CustomPasswordResetConfirm(auth_views.PasswordResetConfirmView):

    template_name = 'auths/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')



class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):

    template_name = 'auths/password_reset_complete.html'



class CustomPasswordChange(auth_views.PasswordChangeView):

    template_name = 'auths/password_change_form.html'
    success_url = reverse_lazy('password_change_done')



class CustomPasswordChangeDoneView(auth_views.PasswordChangeDoneView):

    template_name = 'auths/password_change_done.html'