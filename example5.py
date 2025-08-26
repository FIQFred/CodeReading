def process_employee_data(employee_data):

    processed_employees = []
    
    for emp_str in employee_data:
        parts = emp_str.split(',')
        
   
        first_name = parts[0]
        last_name = parts[1]
        age = int(parts[2])
        salary = float(parts[3])
        department = parts[4]
        hire_date = parts[5]          
      
        if age >= 18 and age <= 65:
            if salary > 0:
                if department in ["Engineering", "Sales", "Marketing", "HR"]:
                  
                    hire_year = int(hire_date.split('-')[0])
                    current_year = 2024  
                    years_service = current_year - hire_year
                    
                    if years_service >= 5:
                        bonus_percentage = 0.1
                    elif years_service >= 2:
                        bonus_percentage = 0.05
                    else:
                        bonus_percentage = 0.02
                    
                    annual_bonus = salary * bonus_percentage
                
                    employee_info = [
                        first_name,
                        last_name,
                        age,
                        salary,
                        department,
                        hire_date,
                        years_service,
                        annual_bonus,
                        f"{first_name} {last_name}",  
                        salary + annual_bonus  
                    ]
                    
                    processed_employees.append(employee_info)
    
    return processed_employees
