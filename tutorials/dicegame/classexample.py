

class Dog():
    ''' Example CLass of a dog!
    Just more stuff!
    and it goes on.
    '''
    legs = 4
    dog_count = 0

    # __slots__ = ['name', 'breed', 'age']
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.__class__.dog_count +=1

    
    def __str__(self):
        return '{}, {}'.format(self.name, self.breed)

    def __len__(self):
        return len(self.name)

    def speak(self):
        'Good dogs speak'
        print('my name is ', self.name)

    def size():
        self.__class__.dog_count += 1

    def info(self):
        print(dir(self))
        print(self.__class__)
max = Dog('max', 'mutt', 3)

print(Dog.dog_count)
    
