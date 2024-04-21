class Car:
    def __init__(self, model, brand, year, ownerName, carNumber, totalKm):
        self.model = model
        self.brand = brand
        self.year = year
        self.ownerName = ownerName
        self.carNumber = carNumber
        self.totalKm = totalKm

    def showCarDetails(self):
        print("Model:", self.model)
        print("Brand:", self.brand)
        print("Year:", self.year)
        print("Owner Name:", self.ownerName)
        print("Car Number:", self.carNumber)
        print("Total Kilometers:", self.totalKm)

    @staticmethod
    def showSoldOutCars():
        total_sold = 100
        print("Total Sold Cars:", total_sold)

    @staticmethod
    def loanApproval(salary):
        if salary >= 60000:
            print("Loan Eligible")
        else:
            print("Not Eligible for Loan")

# Step 1 - Car Setup
car_ABC = Car("ABC", "Honda", 2020, "John", "XYZ1234", 0)

# Step 2 - Modify & Display
car_ABC.totalKm = 5000
car_ABC.showCarDetails()

# Step 3 - Count & Check
Car.showSoldOutCars()
Car.loanApproval(60000)  # Checking loan eligibility for a salary of 60,000
