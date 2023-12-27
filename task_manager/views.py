# task_manager/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import UserRegistration, Task1
global user


def registration_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not UserRegistration.objects.filter(email=email).exists():
            user = UserRegistration(email=email, password=password)
            user.save()
            messages.success(
                request, 'Registration successful! Please log in.')
            return redirect('login_page')
        else:
            messages.error(
                request, 'Email already exists. Please log in or use a different email.')
            return redirect('registration_page')

    return render(request, 'registration_page.html')


def login_page(request):
    print("Thaiyal")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        if UserRegistration.objects.filter(email=email, password=password).exists():
            print("ok")
            messages.success(
                request, 'Login successful! Welcome.')
            global use
            use = UserRegistration.objects.filter(
                email=email, password=password)
            print(use)
            for i in use:
                global u_id, u_name, tasks
                print(i.password)
                print(i.email)
                u_id = i.pk
                u_name = (i.email.split('@')[0]).upper()

            tasks = Task1.objects.filter(user_id=u_id)
            # print(tasks)
            return render(request, 'dashboard.html', {'username': u_name, 'id': u_id, 'tasks': tasks})
        else:
            messages.error(
                request, 'Invalid email or password. Please try again.')
            return redirect('login_page')

    return render(request, 'login_page.html')
    

def home_page(request):
    return render(request, 'base.html')


def dashboard(request):
    global tasks1
    # tasks1 = Task1.objects.filter(user_id=u_id).order_by('due_date')
    # u_id = request.session['u_id']
    # u_name = request.session['u_name']
    # Get the sorting option from query parameter
    sort_by = request.GET.get('sort_by')

    tasks1 = Task1.objects.filter(user_id=u_id)

    if sort_by == 'priority':
        tasks1 = tasks1.order_by('priority')
    elif sort_by == 'due_date':
        tasks1 = tasks1.order_by('due_date')
    search_query = request.GET.get('q')
    if search_query:
        tasks1 = tasks1.filter(
            Q(title__icontains=search_query) | Q(
                description__icontains=search_query)
        )
        return render(request, 'dashboard.html', {'username': u_name, 'tasks': tasks1})
    # tasks1 = Task1.objects.filter(user_id=u_id).order_by('due_date')
    if request.method == 'POST':
        tasks1 = Task1.objects.filter(user_id=u_id)
        print("Yes")
        # Get the form data from the request.POST dictionary

    return render(request, 'dashboard.html', {'username': u_name, 'tasks': tasks1})


def check(request):
    if request.method == 'POST':
        print("mohan")
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        is_completed = request.POST.get('is_completed', False)

        # Create the task with the current user as the user field
        tasks = Task1(
            user_id=u_id,
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            is_completed=is_completed
        )
        tasks.save()
        messages.success(request, 'Task created successfully!')
        tasks1 = Task1.objects.filter(user_id=u_id)
        return render(request, 'dashboard.html', {'tasks': tasks1, 'username': u_name})
    """"
    else:
        print("no")
     """


def update_task(request, pk):
    global tasks
    tasks = get_object_or_404(Task1, id=pk)

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        priority = request.POST['priority']
        is_completed = request.POST.get('is_completed', False)

        tasks.title = title
        tasks.description = description
        tasks.due_date = due_date
        tasks.priority = priority
        tasks.is_completed = is_completed
        tasks.save()
        tasks1 = Task1.objects.filter(user_id=u_id)
        return render(request, 'dashboard.html', {'tasks': tasks1, 'username': u_name})
    else:
        return render(request, 'update_task.html', {'tasks': tasks})


def delete_task(request, pk):
    global tasks1
    tasks = get_object_or_404(Task1, id=pk)
    if request.method == 'POST':
        tasks.delete()
        tasks1 = Task1.objects.filter(user_id=u_id)
        return render(request, 'dashboard.html', {'tasks': tasks1, 'username': u_name})
    return render(request, 'delete_task.html', {'tasks': tasks})


def logout_user(request):
    logout(request)
    return redirect('login_page')
