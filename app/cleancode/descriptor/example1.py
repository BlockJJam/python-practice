from functools import partial
from typing import Callable


class HistoryTracedAttribute:
    def __init__(self, trace_attribute_name) -> None:
        self.trace_attribute_name = trace_attribute_name
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        self._track_change_in_value_for_instance(instance, value)
        instance.__dict__[self._name] = value

    def _track_change_in_value_for_instance(self, instance, value):
        self._set_default(instance)
        if self._needs_to_track_change(instance, value):
            instance.__dict__[self.trace_attribute_name].append(value)

    def _needs_to_track_change(self, instance, value) -> bool:
        try:
            current_value = instance.__dict__[self._name]
        except KeyError:
            return True

        return value != current_value
    
    def _set_default(self, instance:object):
        instance.__dict__.setdefault(self.trace_attribute_name, [])

class Traveller:
    current_city = HistoryTracedAttribute('cities_visited')

    def __init__(self, name, current_city):
        self.name = name
        self.current_city = current_city
    
t = Traveller('jjm', 'seoul')
t.current_city = 'paris'
t.current_city = 'newyork'

print(t.cities_visited)

class FoodFighter:
    current_food = HistoryTracedAttribute('ate_foods')
    
    def __init__(self, name, current_food) -> None:
        self.name = name
        self.current_food = current_food

f1 = FoodFighter('jjm', 'hotdog')
f1.current_food = 'noodle'
f1.current_food = 'frenchfries'

print(f1.ate_foods)
