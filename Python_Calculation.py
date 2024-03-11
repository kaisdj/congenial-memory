import math

import matplotlib.pyplot as plt
from sympy import Triangle

import matplotlib.pyplot as py
import numpy as np
class Triangle:


    def main(self):
        while True:

            print(">Choose options:")

            print(">Choose(1) For Calculation C Side :")

            print(">Choose(2) For Calculation A Side:")

            print(">Choose(3) For Calculation B Side:")

            print(">Choose(4) For Calculation For The Area:")

            print(">Choose(5) Show Triangel:")

            print(">Choose(6) For Calculation of A Angle:")

            print(">Choose(7) For Calculation of B Angle:")

            print(">Choose(X) To Exit:")

            option = (input("Enter your option: "))

            if option == '1':

                print(">Calculation For C Side:")
                triangle.pythagoras_input()
                triangle.value_conditions()
                triangle.is_number()


            elif option == '2':
                print(">Calculation For A Side:")
                triangle.calc_a_side_input()
                triangle.value_conditions()
                triangle.is_number()


            elif option == '3':
                print(">Calculation For B Side:")
                triangle.calc_b_side_input()
                triangle.value_conditions()
                triangle.is_number()

            elif option =='4':
                print(">Calculation For Area:")
                triangle.calc_area_input()
                triangle.value_conditions()
                triangle.is_number()

            elif option =='5':

                print("Showing Triangel:")
                triangle.show_triangle()
                triangle.value_conditions()
                triangle.is_number()

            elif option =='6':
                    print(">Calculation of A Angle:")
                    triangle.calc_A_Angle_input()
                    triangle.value_conditions()
                    triangle.is_number()

            elif option =='7':
                    print(">Calculation of B Angle:")
                    triangle.calc_B_Angle_input()
                    triangle.value_conditions()
                    triangle.is_number()

            elif option =='X':
                print("EXIT")

                break

    def __init__(self,a=0, b=0, c=0, A=0, B=0,C=0):

        self.a = a
        self.b = b
        self.c = c

        self.A = A
        self.B = B
        self.C = C


    def calc_c_side(self):

        calc_c= math.sqrt(self.a**2 +self.b**2)

        return calc_c


    def calc_a_side(self):

        calc_a = math.sqrt(self.c**2-self.b**2)

        return calc_a

    def calc_b_side(self):

        calc_b = math.sqrt(self.c**2-self.a**2)

        return calc_b

    def A_angle(self):
        sin_A = math.asin(self.a / self.c)
        self.A = math.degrees(sin_A)
        return self.A


    def B_angle(self):

        Sin_B = math.asin(self.b/self.c)

        self.B = math.degrees(Sin_B)

        return self.B


    def pythagoras_input(self):

        self.a = self.safe_float_int_input(input("Enter the value of a: "))
        self.b = self.safe_float_int_input(input("Enter the value of b: "))
        self.c = self.calc_c_side()
        print(f"The value of c is:",self.c)

    def calc_a_side_input(self):
        self.b = self.safe_float_int_input(input("Enter the value of b:"))
        self.c = self.safe_float_int_input(input("Enter the value of c: "))
        self.a = self.calc_a_side()
        print(f"The value of a is:", self.a)

    def show_triangle(self):

        points = np.array([[0, 0], [self.a, 0], [0, self.b]])

        fig, ax = plt.subplots()

        ax.fill_between(points[:, 0], 0, points[:, 1], color='b')

        plt.show()

    def calc_b_side_input(self):

        self.a = self.safe_float_int_input(input("Enter the value of a: "))
        self.c = self.safe_float_int_input(input("Enter the value of c: "))
        self.b = self.calc_b_side()
        print(f"The value of b is:", self.b)

    def calculation_area(self):

        area = self.b*self.a

        return area


    def calc_area_input(self):

        self.a = self.safe_float_int_input(input("Enter the value of a: "))
        self.b = self.safe_float_int_input(input("Enter the value of b: "))
        area = self.calculation_area()
        print(f"The area of the triangle is:", area)


    def calc_A_Angle_input(self):

        self.a = self.safe_float_int_input(input("Enter the value of a:"))
        self.c = self.safe_float_int_input(input("Enter the value of c:"))
        Sin_A = self.A_angle()
        print(f" The Angle of A is:", Sin_A)


    def calc_B_Angle_input(self):

        self.b = self.safe_float_int_input(input("Enter the value of b:"))
        self.c = self.safe_float_int_input(input("Enter the value of c:"))
        self.B = self.B_angle()
        print(f" The Angle of B is:", self.B)

    def is_number(self):
            if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)) or not isinstance(self.c, (
            int, float)):
                return False
            return True

    def safe_float_int_input(self, prompt: str) -> float:
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def value_conditions(self):

        if self.a < 0 or self.b < 0 or self.c <0:

            raise ValueError("Invalid input: a and b must be greater than or equal to 0")





if __name__=='__main__':
    triangle = Triangle()
    triangle.main()
















