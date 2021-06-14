#!/usr/bin/env python


class Underscore:
    def map(self, iterable, callback):
        # your code here
        new_iterable = []
        for item in iterable:
            new_iterable.append(callback(item))
        return new_iterable


    def find(self, iterable, callback):
        # your code here
        for item in iterable:
            if callback(item) is True:
                return item
        return None


    def filter(self, iterable, callback):
        # your code
        new_iterable = []
        for item in iterable:
            if callback(item) is True:
                new_iterable.append(item)
        return new_iterable


    def reject(self, iterable, callback):
        # your code
        new_iterable = []
        for item in iterable:
            if callback(item) is False:
                new_iterable.append(item)
        return new_iterable


# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(f'Evens:   {evens}')
# should return [2, 4, 6] after you finish implementing the code above

odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(f'Odds:    {odds}')

squares = _.map([1, 2, 3, 4, 5, 6], lambda x: x ** 2)
print(f'Squares: {squares}')

found = _.find([1, 2, 3, 4, 5, 6], lambda x: x == 4)
print(f'Four:    {found}')
