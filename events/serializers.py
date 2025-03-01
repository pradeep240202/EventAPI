from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Event,Ticket

# Serializer Class For Events(GET and POST)
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

# Serializer Class FOr Ticket(Purchase and List)
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ["user","event"]

    # validate quantity of tickets purchase
    def validate_quantity(self, value):
        event_id = self.context['view'].kwargs.get('event_id')
        event = get_object_or_404(Event,pk=event_id)

        ticket_available = event.total_tickets - event.tickets_sold

        if value > ticket_available:
            raise serializers.ValidationError(f"Olny {ticket_available} are availabe you can't buy more than that")
        
        if value == 0:
            raise serializers.ValidationError(f"You can buy minimum 1 tickets")
        
        return value
    
    # This is for ticket creation and update sold tickets in event
    def create(self, validated_data):
        request = self.context.get('request')
        
        event_id = self.context['view'].kwargs.get('event_id')
        event = get_object_or_404(Event,pk=event_id)
        event.tickets_sold += validated_data["quantity"]
        event.save()

        ticket = Ticket.objects.create(user=request.user,event=event,**validated_data)
        return ticket