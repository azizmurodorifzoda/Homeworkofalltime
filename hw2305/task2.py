class Employee:
    def __init__(self, name, department, salary, years_of_experience):
        self.name = name
        self.department = department
        self.salary = salary
        self.years_of_experience = years_of_experience

    def calculate_bonus(self):
        bonus_percentage_per_year = 0.05
        bonus = self.salary * self.years_of_experience * bonus_percentage_per_year
        return bonus

    def display_info(self):
        print(f"Employee's Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:,.2f}")
        print(f"Years of Experience: {self.years_of_experience} years")
        print(f"Calculated Bonus: ${self.calculate_bonus():,.2f}")

employee1 = Employee("John Doe", "Engineering", 80000, 5)
employee1.display_info()

employee2 = Employee("Jane Smith", "Marketing", 90000, 8)
employee2.display_info()
