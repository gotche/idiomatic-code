## Descriptors

# Problem

You want to manage attributes of an object.

```
class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

book = Book(name='Utopia', price=30)
```

you want to avoid this

```
book = Book(name='Utopia', price=-20)
```

and this:

```
book.price = -20
```


# Naive solution

```
class Book:
    def __init__(self, name, price):
        self.name = name

        if price < 0:
            raise ValueError('The price of a book cannot be negative')
        else:
            self.price = price
```

Adding the price check in the initializer protects against instantiation

```
book = Book(name='Utopia', price=-20)

...

ValueError: The price of a book cannot be negative
```

but not against direct assignation to the instance attribute

```
book.price = -20

book.price
-20
```

# Better solution

Use a descriptor class

```
import weakref


class Price:
    def __init__(self):
        self.values = weakref.WeakKeyDictionary()

    def __get__(self, instance):
        return self.values.get(instance)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('The price of a book cannot be negative')
        else:
            self.values[instance] = value

    def __delete__(self, instance)
        del self.values[instance]


class Book:
    price = Price()

    def __init__(self, name, price):
        self.name = name
        self.price = price
```

# Better solution

Use property methods

```
class Book:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price < 0:
            raise ValueError('The price of a book cannot be negative')
        else:
            self._price = price

    price = property(get_price, set_price)
```

# Best solution

Use property decorator

```
class Book:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError('The price of a book cannot be negative')
        else:
            self._price = price
```
