TRUNCATE TABLE raw.timesheet;
CREATE TABLE IF NOT EXISTS raw.timesheet(
    employee_id varchar(255),
    cost_center varchar(255),
    punch_in_time varchar(255),
    punch_out_time varchar(255),
    punch_apply_date varchar(255),
    hours_worked varchar(255),
    paycode varchar(255)
)
