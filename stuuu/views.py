from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .forms import StudentForm
from .models import Student


def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)  # Instantiate the form with POST data
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = StudentForm()  # Instantiate an empty form
    return render(request, 'registration/register.html', {'form': form})

def success(request):
    return render(request, 'registration/success.html')
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student_detail.html', {'student': student})
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
from django.contrib import messages

username="admin"
password="admin"
def admin_login(request):
    if request.method == 'POST':
        usrname = request.POST['username']
        pwd = request.POST['password']
        if usrname == username and pwd == password:
            return render(request, 'student_list.html', {'students': Student.objects.all()})
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('admin_login')
    else:
        return render(request, "admin_login.html")

    return render(request, 'admin_login.html')
