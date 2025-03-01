from django.urls import path
from .views import EventView,TicketView

urlpatterns = [
    path("", EventView.as_view(), name="events"),
    path("<int:event_id>/purchase/",TicketView.as_view(),name="tikcets")
]