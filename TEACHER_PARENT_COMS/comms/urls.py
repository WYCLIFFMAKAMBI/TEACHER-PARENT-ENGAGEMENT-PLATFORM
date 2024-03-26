from django.urls import path
from .views import *

from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name='homepage'),
    path('teacher/register/', teacher_register, name='teacher_register'),
    path('dashboard-admin/register/', admin_register, name='admin_register'),
    path('parent/register/', parent_register, name='parent_register'),
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/parent/', parent_dashboard, name='parent_dashboard'),
    path('dashboard/teacher/', teacher_dashboard, name='teacher_dashboard'),
    #events
    path('dashboard/event/',create_events, name='event'),
    path('dashboard/event/delete/<int:id>',delete_even, name='delete_event'),
    path('dashboard/event/edit/<int:id>',edit_events, name='edit_event'),
    path('dashboard/event/list/',event_list, name='list_event'),
    path('login', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # Student-related URLs
    path('create/student/', create_student, name='create_student'),
    path('update/student/<int:student_id>/', update_student, name='update_student'),
    path('delete/student/<int:id>/', delete_student, name='delete_student'),

    path('student/list/', student_list, name='student_list'),

    # Subject-related URLs
    path('create/subject/', create_subject, name='create_subject'),
    path('update/subject/<int:subject_id>/', update_subject, name='update_subject'),
    path('delete/subject/<int:subject_id>/', delete_subject, name='delete_subject'),
    path('subject/list/', subject_list, name='subject_list'),

    # Result-related URLs
    path('create/result/', create_result, name='create_result'),
    path('update/result/<int:result_id>/', update_result, name='update_result'),
    path('delete/result/<int:result_id>/', delete_result, name='delete_result'),
    path('result/list/', result_list, name='result_list'),

    # Attendance-related URLs
    path('create/attendance/', create_attendance, name='create_attendance'),
    path('update/attendance/<int:attendance_id>/', update_attendance, name='update_attendance'),
    path('delete/attendance/<int:id>/', delete_attendance, name='delete_attendance'),
    path('attendance/list/', attendance_list, name='attendance_list'),

    path('parent/results',parent_result_list,name='student_result'),
     path('parent/assign',parent_asign_list,name='student_assign'),

    path('assn/list/', assignment_list, name='assignment_list'),
    path('create/assn/', assignment_create, name='assignment_create'),
    path('ass/<int:pk>/update/', assignment_update, name='update_assignment'),
    path('ass/<int:pk>/delete/', assignment_delete, name='delete_assignment'),

     path('conference/', conferencing_list, name='conferencing_list'),
    path('conferencing/<int:pk>/', conferencing_detail, name='conferencing_detail'),
    path('conferencing/create/', conferencing_create, name='conferencing_create'),
    path('conferencing/<int:pk>/update/', conferencing_update, name='conferencing_update'),
    path('conferencing/<int:pk>/delete/', conferencing_delete, name='conferencing_delete'),

    path('profile/<int:pk>/', studentprofile_detail, name='profile_detail'),
    path('profile/create/', studentprofile_create, name='profile_create'),
    path('profile/<int:pk>/update/', studentprofile_update, name='profile_update'),
    path('profile/<int:pk>/delete/', studentprofile_delete, name='profile_delete'),
    path('profiles/', studentprofile_list, name='profile_list'),
]




    