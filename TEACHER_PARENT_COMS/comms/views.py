from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *

def homepage(request):
    even=events.objects.all()
    return render(request,'home/homepage.html',{"events":even})

@login_required
def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role='teacher'
            user.save()
              # Replace 'home' with the desired URL after registration
            return redirect("admin_dashboard")
    else:
        form = TeacherRegistrationForm()
    return render(request, 'admindashboard/teacher_register.html', {'form': form})


@login_required
def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role='admin'
            user.save()  # Replace 'home' with the desired URL after registration
            return redirect("admin_dashboard")
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin_registration.html', {'form': form})


@login_required
def parent_register(request):
    if request.method == 'POST':
        form = ParentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role='parent'
            user.save()
            login(request, user)
            return redirect('admin_dashboard')  # Replace 'home' with the desired URL after registration
    else:
        form = ParentRegistrationForm()
    return render(request, 'admindashboard/parent_registration.htm', {'form': form})



def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'admin':
                    return redirect('admin_dashboard')  # Replace with your admin dashboard URL
                elif user.role == 'teacher':
                    return redirect('teacher_dashboard')  # Replace with your teacher dashboard URL
                elif user.role == 'parent':
                    return redirect('parent_dashboard')  # Replace with your parent dashboard URL
                else:
                    return redirect('home')  # Replace with your default dashboard URL
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')    
def admin_dashboard(request):
    even=events.objects.all()
    return render(request,'admindashboard/admin_dashboard.html',{'events':even})

def parent_dashboard(request):
    even=events.objects.all()
    return render(request,'parent_dash/parent_dashboard.html',{'events':even})

def teacher_dashboard(request):
    even=events.objects.all()
    return render(request,'teacher_dash/teacher_dashboard.html',{'events':even})

def create_events(request):
    if request.method=="POST":
        event=EventForm(request.POST,request.FILES)
        if event.is_valid():
            event.save()
            return redirect('admin_dashboard')
    else:
       event=EventForm()
    return render(request,'admindashboard/event.html',{'form':event})  
           
def edit_events(request,id):
    even=events.objects.get(id=id)
    if request.method=="POST":
        event=EventForm(request.POST,request.FILES)
        if event.is_valid():
            event.save()
            return redirect('admin_dashboard')
    else:
       event=EventForm(instance=even)
    return render(request,'admindashboard/event.html',{'form':event})             

def event_list(request):
    even=events.objects.all()
    return render(request,'event_list.html',{'events':even})
def delete_even(request,id):
    even=events.objects.get(id=id)
    even.delete()
    return redirect('list_event')


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Replace 'student_list' with the URL for listing students
    else:
        form = StudentForm()

    return render(request, 'teacher_dash/create_student.html', {'form': form})

def update_student(request, student_id):
    instance = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Replace 'student_list' with the URL for listing students
    else:
        form = StudentForm(instance=instance)

    return render(request, 'teacher_dash/create_student.html', {'form': form, 'student': instance})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'teacher_dash/student_list.html', {'students': students})

def delete_student(request,id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect("student_list")

# Similar views for Subject, Result, and Attendance

# Subject views
def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')  # Replace 'subject_list' with the URL for listing subjects
    else:
        form = SubjectForm()

    return render(request, 'admindashboard/create_subject.html', {'form': form})

def update_subject(request, subject_id):
    instance = get_object_or_404(Subject, id=subject_id)
    
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('subject_list')  # Replace 'subject_list' with the URL for listing subjects
    else:
        form = SubjectForm(instance=instance)

    return render(request, 'admindashboard/create_subject.html', {'form': form, 'subject': instance})

def delete_subject(request, subject_id):
    instance = get_object_or_404(Subject, id=subject_id)
    instance.delete()
    return redirect('subject_list')

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'admindashboard/subject_list.html', {'subjects': subjects})

# Result views
def create_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result_list')  # Replace 'result_list' with the URL for listing results
    else:
        form = ResultForm()

    return render(request, 'teacher_dash/create_result.html', {'form': form})

def update_result(request, result_id):
    instance = get_object_or_404(Result, id=result_id)
    
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('result_list')  # Replace 'result_list' with the URL for listing results
    else:
        form = ResultForm(instance=instance)

    return render(request, 'teacher_dash/create_result.html', {'form': form, 'result': instance})

def delete_result(request, result_id):
    res = get_object_or_404(Result, id=result_id)
    res.delete()
    return redirect('result_list')

def result_list(request):
    results = Result.objects.all()
    return render(request, 'teacher_dash/result_list.html', {'results': results})

# Attendance views
def create_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')  # Replace 'attendance_list' with the URL for listing attendance
    else:
        form = AttendanceForm()

    return render(request, 'teacher_dash/create_attendance.html', {'form': form})

def update_attendance(request, attendance_id):
    instance = get_object_or_404(Attendance, id=attendance_id)
    
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')  # Replace 'attendance_list' with the URL for listing attendance
    else:
        form = AttendanceForm(instance=instance)

    return render(request, 'teacher_dash/create_attendance.html', {'form': form, 'attendance': instance})

def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'teacher_dash/attendance_list.html', {'attendance_records': attendance_records})

def delete_attendance(request,id):
    attend=Attendance.objects.get(id=id)
    attend.delete()
    return redirect('attendance_list')

def parent_result_list(request):
    user=request.user
    results = Result.objects.all()
    return render(request, 'parent_dash/result_list.html', {'results': results})

def assignment_list(request):
    assignments = Assignments.objects.all()
    return render(request, 'teacher_dash/assignment_list.html', {'assignments': assignments})

def assignment_create(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'teacher_dash/create_assignment.html', {'form': form})

def assignment_update(request, pk):
    assignment = get_object_or_404(Assignments, pk=pk)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'teacher_dash/create_assignment.html', {'form': form})

def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignments, pk=pk)
    
    assignment.delete()
    return redirect('assignment_list')

def parent_asign_list(request):
    assignments = Assignments.objects.all()
    return render(request, 'parent_dash/assignment_list.html', {'assignments': assignments})

def conferencing_list(request):
    conferencings = Conferencing.objects.all()
    return render(request, 'conferencing_list.html', {'conferencings': conferencings})

def conferencing_detail(request, pk):
    conferencing = get_object_or_404(Conferencing, pk=pk)
    return render(request, 'conferencing_detail.html', {'conferencing': conferencing})

def conferencing_create(request):
    if request.method == 'POST':
        form = ConferencingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conferencing_list')
    else:
        form = ConferencingForm()
    return render(request, 'conferencing_form.html', {'form': form})

def conferencing_update(request, pk):
    conferencing = get_object_or_404(Conferencing, pk=pk)
    if request.method == 'POST':
        form = ConferencingForm(request.POST, instance=conferencing)
        if form.is_valid():
            form.save()
            return redirect('conferencing_list')
    else:
        form = ConferencingForm(instance=conferencing)
    return render(request, 'conferencing_form.html', {'form': form})

def conferencing_delete(request, pk):
    conferencing = get_object_or_404(Conferencing, pk=pk)
    
    conferencing.delete()
    return redirect('conferencing_list')
  
   
def studentprofile_detail(request, pk):
    studentprofile = get_object_or_404(Studentprofile, pk=pk)
    return render(request, 'studentprofile_detail.html', {'studentprofile': studentprofile})

def studentprofile_create(request):
    if request.method == 'POST':
        form = StudentprofileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')  # Redirect to a page showing all profiles
    else:
        form = StudentprofileForm()
    return render(request, 'studentprofile_form.html', {'form': form})

def studentprofile_update(request, pk):
    studentprofile = get_object_or_404(Studentprofile, pk=pk)
    if request.method == 'POST':
        form = StudentprofileForm(request.POST, request.FILES, instance=studentprofile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', pk=pk)  # Redirect to the detail view of the updated profile
    else:
        form = StudentprofileForm(instance=studentprofile)
    return render(request, 'studentprofile_form.html', {'form': form})

def studentprofile_delete(request, pk):
    studentprofile = get_object_or_404(Studentprofile, pk=pk)
    if request.method == 'POST':
        studentprofile.delete()
        return redirect('profile_list')  # Redirect to a page showing all profiles
    return render(request, 'studentprofile_confirm_delete.html', {'studentprofile': studentprofile})

def studentprofile_list(request):
    studentprofiles = Studentprofile.objects.all()
    return render(request, 'studentprofile_list.html', {'studentprofiles': studentprofiles})   