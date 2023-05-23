from django.urls import path
from .views import index, show, create ,edit, delete

urlpatterns = [
    path( '' , index , name='index' ),
    path( '<int:bid>/' , show , name='show' ),
    path( 'create/' , create , name='create' ),
    path( '<int:bid>/edit' , edit , name='update' ),
    path( '<int:bid>/destroy' , delete , name='destroy')
]
