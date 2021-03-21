from models.m_general import Department, SubDepartment


def get_all_departments():
    departments = Department.query.all()
    return departments


def get_all_sub_departments():
    sub_departments = SubDepartment.query.all()
    return sub_departments


def get_sub_department_by_id(department_id):
    sub_department = SubDepartment.query.filter_by(id=department_id).first()
    return sub_department
