DROP TABLE raw.timesheet;
CREATE TABLE raw.timesheet(
    employee_id varchar(255),
    cost_center varchar(255),
    punch_in_time varchar(255),
    punch_out_time varchar(255),
    punch_apply_date varchar(255),
    hours_wokred varchar(255),
    paycode varchar(255)
)
