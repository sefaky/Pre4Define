from . import views
from django.urls import path

urlpatterns = [
    path('' , views.define, name = 'define') ,

  """  path('category<category>/' , views.categorize, name = 'category') ,"""
"""    path('plot/',views.index),"""


]