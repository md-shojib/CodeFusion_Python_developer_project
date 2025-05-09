from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from .models import Country
from .serializers import CountrySerializer
from django.db.models import Q
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# CRUD Views
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('country_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def country_list_view(request):
    query = request.GET.get("search", "")
    countries = Country.objects.filter(name__icontains=query)
    return render(request, 'country_list.html', {'countries': countries})

class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

class CountryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

# List same region countries
class SameRegionCountriesView(generics.ListAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        country = Country.objects.get(pk=self.kwargs['pk'])
        return Country.objects.filter(region=country.region).exclude(id=country.id)

# List countries that speak a given language
class SameLanguageCountriesView(generics.ListAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        language = self.kwargs['language']
        return Country.objects.filter(languages__icontains=language)

# Search by name
class CountrySearchView(generics.ListAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        name = self.request.GET.get('name', '')
        return Country.objects.filter(name__icontains=name)


@login_required
def regional_and_languages_view(request, pk):
    country = Country.objects.get(pk=pk)
    same_region = Country.objects.filter(region=country.region).exclude(id=pk)
    return render(request, 'details.html', {
        'country': country,
        'same_region': same_region
    })
