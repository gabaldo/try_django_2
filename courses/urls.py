from django.urls import path


from .views import (
    my_fbv,
    CourseView,
    CourseDetailView,
    CourseListView,
    MyListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    )

app_name = 'courses'
urlpatterns = [
    #path('', my_fbv, name='courses-list'),
    path('', CourseListView.as_view(), name='course-list'),
    path('my_list/', MyListView.as_view(), name='course-my_list'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    path('<int:id>', CourseDetailView.as_view(), name='course-detail'),
]