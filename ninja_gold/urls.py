from django.urls import path, include

urlpatterns = [
    path('', include('ninja_app.urls')),
]
