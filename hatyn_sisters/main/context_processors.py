from .models import ModelEvents

def events_obj_context(request):
    return {'events_obj_context': ModelEvents.objects.filter(draft=False) if ModelEvents.objects.filter(draft=False).count() >= 1 else []}