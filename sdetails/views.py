from django.shortcuts import render,redirect
from .models import course, student 
from .forms import studentform, CourseForm  
def index(request):  
    courses = course.objects.all()  
    return render(request, 'sdetails/index.html', {'courses': courses})  

def register_student(request):  
    if request.method == 'POST':  
        form = studentform(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('index')  
    else: 
        form = studentform()  
    return render(request, 'sdetails/register_student.html', {'form': form})

def register_course(request):  
    if request.method == 'POST':  
        form = CourseForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('index')  
    else:
        form = CourseForm()  
    return render(request, 'sdetails/register_course.html', {'form': form})  

def student_list(request, course_id):
    selected_course = course.objects.get(id=course_id)
    students = selected_course.students.all()

    return render(
        request,
        'sdetails/student_list.html',
        {
            'students': students,
            'course': selected_course
        }
    )