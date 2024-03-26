from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from .models import  *

class TeacherRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    tsc_no = forms.CharField(max_length=20)  
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'tsc_no', 'email', 'password1', 'password2']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'teacher'
        if commit:
            user.save()
            Teacher.objects.create(user=user, tsc_no=self.cleaned_data['tsc_no'])
        return user

class AdminRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True  # Set the user as a staff member
        user.is_superuser = True  # Set the user as a superuser
        if commit:
            user.save()
        return user
     
class ParentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    student_name=forms.CharField(max_length=30)
    class Meta:
        model = CustomUser  # Corrected from 'models' to 'model'
        fields = ['username', 'first_name', 'last_name','student_name', 'email', 'password1', 'password2']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'parent'
        if commit:
            user.save()
            Parent.objects.create(user=user, student_name=self.cleaned_data['student_name'])
        return user    

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )

class EventForm(forms.ModelForm):
     class Meta:
         model=events
         fields='__all__'   

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'admission_no', 'session', 'student_class']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'session', 'student_class']

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'subject', 'marks', 'grade']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'is_present']

class SessionForm(forms.ModelForm):
    class Meta:
        models=Session
        fields="__all__"        
class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignments
        fields = ['subject', 'title', 'content']        

class ConferencingForm(forms.ModelForm):
    class Meta:
        model=Conferencing 
        fields='__all__'
        widget={
            'date':AdminTimeWidget(),
            'time':AdminDateWidget(),
        }

class StudentprofileForm(forms.ModelForm):
    class Meta:
        model = Studentprofile
        fields = ['student_name', 'image', 'discipline', 'actions', 'achievement']