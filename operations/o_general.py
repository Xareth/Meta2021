from data_manager import dm_general, dm_users
from flask import jsonify
from models.a_schemas import SubDepartmentSchema
from data_manager.connection import update


def get_all_sub_departments_jsonify():
    sub_departments_db = dm_general.get_all_sub_departments()
    schema = SubDepartmentSchema(many=True)
    sub_department = schema.dump(sub_departments_db).data
    return jsonify({'sub_department': sub_department})


@update
def add_subdepartment_to_user(user_id, subdepartment_id):
    user = dm_users.get_user_by_id(user_id)
    subdepartment = dm_general.get_sub_department_by_id(subdepartment_id)
    user.ex_user_subdepartments.append(subdepartment)
    return True