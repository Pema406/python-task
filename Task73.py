import math
def calculate_hypotenuse(side1,side2):
    hypotenues = math.sqrt(side1**side2 + side2**2)
    return hypotenues
    def triangle_info(side1, side2):
        hypotenuse = calculate_hypotenuse(side1,side2)
        print("the length of the hypotenuse is:",hypotenuse)