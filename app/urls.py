from django.urls import path

from .views import import_leki, home_view, export_data, get_queryset

urlpatterns = [
    #path('search/', SearchResultsView.as_view(), name='search_results'),
    #path('search/',get_queryset, name='search_results'),
    #path('', HomePageView.as_view(), name='home2'),
    path('export/', export_data, name="export"),
    path('import/', import_leki, name="import"),
    #path('export/', export_data, name="export"),

    path('',get_queryset, name='home'),
    #path('', home_view, name="home"),
]