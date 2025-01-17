from core.models.db_schemas import Employee
from extensions import db

class EmployeeManager:
    @staticmethod
    def get_all_employees():
        return Employee.query.all()

    @staticmethod
    def get_all_employees_json():
        employees = Employee.query.all()
        return [
            {
                'employee_id': emp.employee_id,
                'name': emp.name,
                'email': emp.email,
                'position': emp.position,
                'salary': emp.salary,
                'date_of_joining': emp.date_of_joining.strftime('%Y-%m-%d')
            } for emp in employees
        ]

    @staticmethod
    def get_employee_by_id(employee_id):
        return Employee.query.get_or_404(employee_id)

    @staticmethod
    def add_employee(data):
        if Employee.query.filter_by(email=data['email']).first():
            return {'success': False, 'message': 'Email already exists!'}
        try:
            new_employee = Employee(
                name=data['name'],
                email=data['email'],
                position=data['position'],
                salary=float(data['salary']),
                date_of_joining=data['date_of_joining']
            )
            db.session.add(new_employee)
            db.session.commit()
            return {'success': True, 'message': 'Employee added successfully!'}
        except Exception as e:
            return {'success': False, 'message': str(e)}

    @staticmethod
    def edit_employee(employee_id, data):
        employee = Employee.query.get_or_404(employee_id)
        try:
            employee.name = data['name']
            employee.email = data['email']
            employee.position = data['position']
            employee.salary = float(data['salary'])
            employee.date_of_joining = data['date_of_joining']
            db.session.commit()
            return {'success': True, 'message': 'Employee updated successfully!'}
        except Exception as e:
            return {'success': False, 'message': str(e)}

    @staticmethod
    def delete_employee(employee_id):
        employee = Employee.query.get_or_404(employee_id)
        try:
            db.session.delete(employee)
            db.session.commit()
            return {'success': True, 'message': 'Employee deleted successfully!'}
        except Exception as e:
            return {'success': False, 'message': str(e)}