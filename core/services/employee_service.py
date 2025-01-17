from flask import Blueprint, request, jsonify, flash, redirect, url_for, render_template
from flask_login import login_required
from extensions import db
from core.models.db_schemas import Employee
from core.handlers.employee_handler import EmployeeManager

employee_bp = Blueprint('employee', __name__, url_prefix='/employees')

@employee_bp.route('/')
@login_required
def index():
    employees = EmployeeManager.get_all_employees()
    return render_template('index.html', employees=employees)

@employee_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_employee():
    if request.method == 'POST':
        form_data = request.form
        result = EmployeeManager.add_employee(form_data)
        if result['success']:
            flash(result['message'], 'success')
            return redirect(url_for('employee.index'))
        else:
            flash(result['message'], 'danger')
    return render_template('add.html')

@employee_bp.route('/edit/<int:employee_id>', methods=['GET', 'POST'])
@login_required
def edit_employee(employee_id):
    if request.method == 'POST':
        form_data = request.form
        result = EmployeeManager.edit_employee(employee_id, form_data)
        if result['success']:
            flash(result['message'], 'success')
            return redirect(url_for('employee.index'))
        else:
            flash(result['message'], 'danger')
    employee = EmployeeManager.get_employee_by_id(employee_id)
    return render_template('edit.html', employee=employee)

@employee_bp.route('/delete/<int:employee_id>', methods=['POST'])
@login_required
def delete_employee(employee_id):
    result = EmployeeManager.delete_employee(employee_id)
    flash(result['message'], 'success' if result['success'] else 'danger')
    return redirect(url_for('employee.index'))

@employee_bp.route('/api', methods=['GET'])
def api_employees():
    employees = EmployeeManager.get_all_employees_json()
    return jsonify(employees)
