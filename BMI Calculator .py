def calculate_bmi():
    weight = int(input("Enter your weight in Kg :"))
    Height = float(input("Enter your height in meters :"))
    result = weight/(Height**2)
    print(result)

calculate_bmi()