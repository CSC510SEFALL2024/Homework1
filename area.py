import math

def compute_area(shape, value):
    if shape == "circle":
        r = float(value)
        return math.pi * r * r
    elif shape == "square":
        a = float(value)
        return a * a
    else:
        return None

def main():
    shape = input("Select Shape (circle or square): ").strip().lower()
    side = "side"
    if shape == "circle":
        side = "radius"
    value = input(f"Enter {side}: ")
    area = compute_area(shape, value)
    
    if area is not None:
        print(f"The area of the {shape} is: {area}")
    else:
        print("Invalid shape selected.")

if __name__ == "__main__":
    main()
