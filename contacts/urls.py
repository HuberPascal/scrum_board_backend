from django.urls import path
from .views import ContactListCreateView, ContactDetailView

urlpatterns = [
    path('', ContactListCreateView.as_view(), name='contact-list-create'),
    path('<int:id>/', ContactDetailView.as_view(), name='contact_detail'),
]
