from django.urls import path
from . import views


urlpatterns = [
	path('', views.product, name="product"),
	path('create', views.createData, name="createData"),
	path('delete', views.deleteData, name="deleteData"),
	path('update', views.updatedata, name="updatedata"),
	# path('', views.Yourdef, name="Yourdef"),
	]