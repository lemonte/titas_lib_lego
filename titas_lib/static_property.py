# static_property.py

class StaticProperty:
    def __init__(self, getter):
        self.getter = getter
    
    def __get__(self, obj, objtype=None):
        return self.getter()
