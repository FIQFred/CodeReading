def process_employee_data(employee_data):
    # employee_data is a list of strings: ["John,Doe,30,50000,Engineering,2020-01-15"]
    processed_employees = []
    
    for emp_str in employee_data:
        parts = emp_str.split(',')
        
        # Primitive obsession - using strings/primitives instead of proper objects
        first_name = parts[0]
        last_name = parts[1]
        age = int(parts[2])
        salary = float(parts[3])
        department = parts[4]
        hire_date = parts[5]  # String instead of date object
        
        # Business logic mixed with data parsing
        if age >= 18 and age <= 65:
            if salary > 0:
                if department in ["Engineering", "Sales", "Marketing", "HR"]:
                    # Calculate years of service using string manipulation
                    hire_year = int(hire_date.split('-')[0])
                    current_year = 2024  # Hardcoded
                    years_service = current_year - hire_year
                    
                    # Salary calculations with magic numbers
                    if years_service >= 5:
                        bonus_percentage = 0.1
                    elif years_service >= 2:
                        bonus_percentage = 0.05
                    else:
                        bonus_percentage = 0.02
                    
                    annual_bonus = salary * bonus_percentage
                    
                    # Creating another primitive-heavy structure
                    employee_info = [
                        first_name,
                        last_name,
                        age,
                        salary,
                        department,
                        hire_date,
                        years_service,
                        annual_bonus,
                        f"{first_name} {last_name}",  # Duplicate data
                        salary + annual_bonus  # Total compensation
                    ]
                    
                    processed_employees.append(employee_info)
    
    return processed_employees