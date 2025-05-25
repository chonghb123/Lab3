import employee_info as employee

employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def test_get_employees_by_age_range():
    test_lower_limit = 20
    test_upper_limit = 33
    result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
        
        
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    test = employee.get_employees_by_age_range(test_lower_limit,test_upper_limit)
    assert(test == result)
def test_calculate_average_salary():
    result = 60166.666666666664
    test = employee.calculate_average_salary()
    assert(test == result)

def test_get_employees_by_dept():
    inputDept = "Marketing"
    result = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    test = employee.get_employees_by_dept(inputDept)
    assert(test == result)

