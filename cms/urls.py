from django.urls import path
from cms.views import IndexDatatableView
from django.views.generic import TemplateView



app_name = 'cms'
urlpatterns = [
    path('index/', TemplateView.as_view(template_name='cms/index.html')), 
    path('datatable-view/', IndexDatatableView.as_view()),
]
