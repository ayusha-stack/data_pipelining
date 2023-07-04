TRUNCATE TABLE raw.employee;

CREATE TABLE  IF NOT EXISTS raw.employee (
    employee_id varchar(255),
    first_name varchar(255),
    last_name varchar(255),
    department_id varchar(255),
    department_name varchar(255),
    manager_employee_id varchar(255),
    employee_role varchar(255),
    salary varchar(255),
    hire_date varchar(255),
    terminated_date varchar(255),
    terminated_reason varchar(255),
    dob varchar(255),
    fte varchar(255),
    location varchar(255)
    )


