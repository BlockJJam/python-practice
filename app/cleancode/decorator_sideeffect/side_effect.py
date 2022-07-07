EVENTS_REGISTRY={}

def register_event(event_cls):
    EVENTS_REGISTRY[event_cls.__name__] = event_cls
    return event_cls

class Event:
    pass

class UserEvent:
    pass

@register_event
class UserLoginEvent(UserEvent):
    pass

@register_event
class UserlogoutEvent(UserEvent):
    pass

