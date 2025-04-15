from django.urls import path
from . import views

urlpatterns = [
    path('locations', views.get_locations),
    path('locations/<pk>', views.get_location),
    path('locations/add', views.create_location),

    path('faculties', views.get_faculties),
    path('faculties/<pk>', views.get_faculty),
    path('faculties/add', views.create_faculty),

    path('equipment', views.get_equipments),
    path('equipment/<pk>', views.get_equipment),
    path('equipment/add', views.create_equipment),

    path('organization', views.get_organizations),
    path('organization/<pk>', views.get_organization),
    path('organization/add', views.create_organization),

]
