from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, NewJob
from django.views.generic import View, UpdateView, ListView, FormView
from .models import Job, Profile
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import authenticate, login

class UsersV(View):


    @staticmethod
    def register(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            
            if form.is_valid() :
                newUser = form.save()
                newUser = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
                login(request, newUser)
                
                username = form.cleaned_data.get('username')
                messages.success(request, f' welcome {username} Your account has been created! You can update your profile')
                return redirect('register2')
        else:
            form = UserRegisterForm()
            
        context={
        'form': form,
        
        }
        return render(request, 'users/register.html', context)
    
    @staticmethod
    def register2(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.method == 'POST':                
                pform = ProfileUpdateForm(request.POST,
                                        request.FILES,
                                        instance=request.user.profile)
                if  pform.is_valid():
                    
                    pform.save()
                    username = pform.cleaned_data.get('username')
                    messages.success(request, f'Welcome to our family!')
                    return redirect('base')
            else:                
                pform = ProfileUpdateForm()
            context={           
            'pform':pform,
            }
            return render(request, 'users/register2.html', context)
        else:
            return redirect('register')

    @login_required
    def profile(request):
        if request.method == 'POST':
            if request.POST.get('update') == '':                
                u_form = UserUpdateForm(request.POST, instance=request.user)
                p_form = ProfileUpdateForm(request.POST,
                                        request.FILES,
                                        instance=request.user.profile)
                if u_form.is_valid() and p_form.is_valid():
                    u_form.save()
                    p_form.save()
                    messages.success(request, f'Your account has been updated!')
                    return redirect('profile')
               
            if request.POST.get('staff') == '':
                user = request.user   
                user.profile.staff_requested = True
                user.save()
                u_form = UserUpdateForm(instance=request.user)
                p_form = ProfileUpdateForm(instance=request.user.profile)
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
    def jobs(request, *args, **kwargs):
        messages.success(request, f"these data are just dummy, the website is still under-Construction!")
        messages.success(request, f"please feel free to check it out, and we're gratefully waiting for your feedback")
        if request.method=='POST':
            if request.POST.get('staff') == '':
                user = request.user   
                user.profile.staff_requested = True
                user.save()
            elif request.POST.get('take') == '':
                user=request.user
                take = request.POST['job']
                take = Job.objects.get(id=take)
                usr = Profile.objects.get(user=user)
                if usr.jobAs == None:
                    usr.jobAs = take
                    usr.save()
                    take.is_available = False
                    take.asTo = usr.user
                    take.save()
                else:
                    messages.warning(request,f'Finish your assigned job first!')
            elif request.POST.get('delete') == '':
                job = request.POST['job']
                job = Job.objects.get(id=job).delete()


            
        job= Job.objects.filter(is_available=True).order_by('-startDate')
        context={
            'jobs':job,
        }
        return render(request, 'users/Jobs.html', context,*args, **kwargs )


    @login_required
    def job_details(request, pk, *args,  **kwargs): 
        messages.success(request, f"these data are just dummy, the website is still underconstruction!")
        messages.success(request, f"please feel free to check it out, and we're gratefully waiting for your feedback")       
        job = Job.objects.get(id=pk)

        if request.method=='POST':
            user=request.user
            if request.POST.get('take') == '':
                take = request.POST['job']
                take =Job.objects.get(id=take)
                pk = request.POST.get('pk')
                usr = Profile.objects.get(user=user)
                if usr.jobAs == None:
                    usr.jobAs = take
                    usr.save()
                    take.is_available = False
                    take.asTo = usr.user
                    take.save()
                    return redirect('jobs')
                else:
                    messages.warning(request,f'Finish your assigned job first!')
            elif request.POST.get('ready') == '':
                ready = request.POST['job']
                ready =Job.objects.get(id=ready)
                pk = request.POST.get('pk')
                usr = Profile.objects.get(user=user)
                ready.is_ready = True
                ready.save()
                return redirect('jobs')
            elif request.POST.get('delete') == '':
                job = request.POST['job']
                job = Job.objects.get(id=job).delete()
                return redirect('jobs')


        context={
            'job':job,
            'pk':pk,
        }
        return render(request, 'users/job_detail.html', context, *args, **kwargs)
    
            

    @login_required
    def administrator(request):
        if request.user.is_superuser:    
            if request.method == 'POST':
                if request.POST.get('updateuser') == '':
                    user=request.POST['user']
                    user = User.objects.get(username=user)           
                    user.is_staff = request.POST.get('staff', '')== 'on' or False
                    user.is_superuser = request.POST.get('superuser', '') == 'on' or False                    
                    user.save()
                elif request.POST.get('accept') == '':
                    user=request.POST['user'] 
                    user = User.objects.get(username=user) 
                    user.is_staff = request.POST.get('staff', '')== 'on' or False
                    user.is_superuser = request.POST.get('superuser', '') == 'on' or False 
                    user.profile.staff_requested = False
                    user.save()
                elif request.POST.get('deny') == '':
                    user=request.POST['user']  
                    user.profile.staff_requested = False
                    user.save()
                elif request.POST.get('charge') == '':
                    withdrawal=request.POST['withdrawal']
                    withdrawal = int(withdrawal)                
                    job =request.POST['job'] 
                    job = Job.objects.get(job=job)                 
                    user = Profile.objects.get(jobAs=job)
                    user = user.user                 
                    blc = User.objects.get(username=user)
                    blc.profile.balance -= withdrawal
                    blc.profile.jobAs = None
                    blc.save() 
                    job.is_available = True
                    job.asTo=None
                    job.save()
                elif request.POST.get('extend') == '': 
                    dt =request.POST['date']
                    job =request.POST['job'] 
                    job = Job.objects.get(job=job)  
                    job.deadline=dt
                    job.save()

                elif request.POST.get('pay') == '':
                    user=request.POST['user']
                    user = User.objects.get(username=user)
                    user = Profile.objects.get(user=user)
                    payment = request.POST.get('payment')
                    payment = int(payment)
                    newBalance = user.balance + payment
                    user.balance =  newBalance
                    user.jobAs = None
                    user.save()
                elif request.POST.get('cash') == '':
                    user=request.POST['user']
                    user = User.objects.get(username=user)
                    user = Profile.objects.get(user=user)
                    payment = request.POST.get('payment')
                    payment = int(payment)
                    newBalance = user.balance - payment
                    user.balance =  newBalance
                    user.save()
                elif request.POST.get('complete') == '':
                    user=request.POST['user']
                    user = User.objects.get(username=user)
                    user = Profile.objects.get(user=user)
                    completed = request.POST.get('job')
                    print('1', completed)
                    completed = Job.objects.get(job=completed)
                    print('2',completed)
                    payment = request.POST.get('payment')
                    payment = int(payment)
                    newBalance = user.balance + payment
                    user.balance =  newBalance
                    user.jobAs = None                    
                    user.save()
                    completed.is_ready=False
                    completed.is_complete = True
                    completed.doneby = completed.asTo.username 
                    completed.asTo = None                   
                    completed.save()


            profiles = Profile.objects.all()
            debt = 0
            for profile in profiles:
                blns=profile.balance
                debt+=blns * -1

            today = timezone.now()
            context={
                'jobs' : Job.objects.all(),
                'users' : User.objects.all(),
                'profiles' : Profile.objects.all(),
                'today':today,
                'debt': debt,
            }
            return render(request,'users/administrator.html', context)
        else:
            return render(request,'base.html')