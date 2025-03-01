from rest_framework import generics
from .models import Event,Ticket
from .serializers import EventSerializer,TicketSerializer
from .permissions import EventPermisison

class EventView(generics.ListCreateAPIView):
    permission_classes = [EventPermisison]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TicketView(generics.ListCreateAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
    def get_queryset(self):
        if self.request.user.role == "Admin":
            return Ticket.objects.all()
        
        else:
            return Ticket.objects.filter(user=self.request.user)

