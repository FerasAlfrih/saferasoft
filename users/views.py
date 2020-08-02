from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, NewJob
from django.views.generic import View, UpdateView, ListView, FormView
from .models import Job, Profile
from django.contrib.auth.models import User
from django.utils import timezone


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
    def jobs(request, *args, **kwargs):
        if request.method=='POST':
            user=request.user
            take = request.POST['job']
            take =Job.objects.get(id=take)
            usr = Profile.objects.get(user=user)
            if usr.jobAs == None:
                usr.jobAs = take
                usr.save()
                take.is_available = False
                take.asTo = usr.user
                take.save()
            else:
                messages.warning(request,f'Finish your assigned job first!')

            
        job= Job.objects.filter(is_available=True).order_by('-startDate')
        context={
            'jobs':job,
        }
        return render(request, 'users/Jobs.html', context,*args, **kwargs )


   
    class job_details(UpdateView):
        model = Job
        fields = ['job', 'user']
        template = 'users/job_detail.html'
        def save(self, request):
            if request.method=='POST':
                user=request.user
                take = request.POST['job']
                take =Job.objects.get(id=take)
                usr = Profile.objects.get(user=user)
                if usr.jobAs == None:
                    usr.jobAs = take
                    usr.save()
                    take.is_available = False
                    take.asTo = usr.user
                    take.save()
                else:
                    messages.warning(request,f'Finish your assigned job first!')
    
            

    @login_required
    def administrator(request):        
        if request.method == 'POST':
            if request.POST.get('updateuser') == '':
                user=request.POST['user']
                user = User.objects.get(username=user)
                # print(request.POST['staff'])
                # print(request.POST['superuser'])                
                user.is_staff = request.POST.get('staff', '')== 'on' or False
                user.is_superuser = request.POST.get('superuser', '') == 'on' or False
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
                if request.POST.get('job'):
                    job = request.POST.get('job')
                    job = Job.objects.get(job=job)
                    job.is_complete = True
                    job.doneby = user.user.username
                    job.asTo=None
                    job.save()
            elif request.POST.get('cash') == '':
                user=request.POST['user']
                user = User.objects.get(username=user)
                user = Profile.objects.get(user=user)
                payment = request.POST.get('payment')
                payment = int(payment)
                newBalance = user.balance - payment
                user.balance =  newBalance
                user.save()
        profiles = Profile.objects.all()
        debt = 0
        for profile in profiles:
            blns=profile.balance
            debt+=blns

        today = timezone.now()
        context={
            'jobs' : Job.objects.all(),
            'users' : User.objects.all(),
            'profiles' : Profile.objects.all(),
            'today':today,
            'debt': debt,
        }
        return render(request,'users/administrator.html', context)