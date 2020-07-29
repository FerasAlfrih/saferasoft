from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, NewJob
from django.views import View
from .models import Job, Profile
from django.contrib.auth.models import User


class UsersV(View):


    @staticmethod
    def register(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})


    @login_required
    def profile(request):
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, 'users/profile.html', context)

    @login_required
    def newJob(request):        
        if request.method == 'POST':
            # form=NewJob(request.POST, instance=request.user)
            # if form.is_valid():
            #     form.save() 
            user=request.user   
            user=User.objects.get(username=user.username)
            job = request.POST['job']
            startDate = request.POST['startDate']
            deadline = request.POST['deadline']
            salary = request.POST['salary']
            withdrawal = request.POST['withdrawal']
            details = request.POST['details']
            jb = Job(user=user,
                    job=job,
                    startDate=startDate,
                    deadline=deadline,
                    salary=salary,
                    withdrawal=withdrawal,
                    details=details,
                )
            
            jb.save()
            return redirect('jobs') 

        else:
            form=NewJob(request.POST, instance=request.user)
            

        context={
        'form':form
        }
        return render(request, 'users/newJob.html', context)

    @login_required
    def jobs(request):
        if request.method=='POST':
            user=request.user
            take = request.POST['job']
            take =Job.objects.get(id=take)

            usr = Profile.objects.get(user=user)
            usr.jobAs = take
            usr.save()
            take.is_available = False 
            take.save()

            
        job= Job.objects.filter(is_available=True)
        context={
            'jobs':job,
        }
        return render(request, 'users/Jobs.html', context)

    @login_required
    def administrator(request):
        
        context={
            'jobs' : Job.objects.all(),
            'users' : User.objects.all(),
            'profiles' : Profile.objects.all(),
        }
        return render(request,'users/administrator.html', context)