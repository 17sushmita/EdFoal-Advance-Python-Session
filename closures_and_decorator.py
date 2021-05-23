def outer(func):
    def wrapper():
        print("I'm the wrapper")
        print("I can perform some functionalities")
        return func()
    return wrapper

@outer
def display():
    print("Pushpak Rai is awesome!!")

@outer
def display2():
    print('Sushmita mam teachs very well')
# a = decorator(display)
# a()
display()
# print(display.__name__)

display2()