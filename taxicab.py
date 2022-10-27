# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Taxicab:

    def __init__(self,x,y):
        #define x and y coordinates
        self._x=x
        self._y=y
        self.reading=0
    def move_x(self, num):
        #moves taxicab in the x direction
        self.num=num
        self.reading += abs(num)
        self._x = self._x+num
        return self._x
    def move_y(self, num2):
        #moves taxicab in the y direction
        self.num2=num2
        self.reading += abs(num2)
        self._y = self._y+num2
        return self._y
    def get_odometer(self):
        #distance taxicab has gone
        new_x=self._x
        new_y=self._y
        print("At this point the cab has traveled",self.reading, "units and is now at coordinates (", new_x,new_y,")")

#cab=Taxicab(5,-4)
#cab.move_x(-3)
#cab.move_y(5)
#cab.move_y(2)
#print(cab.get_odometer())
