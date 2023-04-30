# Getters in Python are methods that are used to access thevalues of an object's properties.
# They are used to return the value of a specific property, 
# and are typically defined using the @property decorator.
class Myclass:
    def __init__(self, value):
        self._value = value

        @property
        def value(self):
            return self._value
        
obj = Myclass(10)
obj._value