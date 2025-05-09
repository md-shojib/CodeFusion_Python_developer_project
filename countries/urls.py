from django.urls import path
from . import views

urlpatterns = [
    path('contry-list', views.country_list_view, name='country_list'),
    path('', views.login_view, name='login'),
    path('details/<int:pk>/', views.regional_and_languages_view, name='regional_and_languages'),
    path('api/countries/', views.CountryListCreateView.as_view()),
    path('api/countries/<int:pk>/', views.CountryRetrieveUpdateDeleteView.as_view()),
    path('api/countries/<int:pk>/regional/', views.SameRegionCountriesView.as_view()),
    path('api/countries/language/<str:language>/', views.SameLanguageCountriesView.as_view()),
    path('api/countries/search/', views.CountrySearchView.as_view()),
]
