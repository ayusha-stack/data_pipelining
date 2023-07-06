DROP TABLE standard.timesheet;

CREATE TABLE standard.timesheet (
  employee_id INT,
  cost_center INT,
  punch_in_time TIME,
  punch_out_time TIME,
  punch_apply_date DATE,
  hours_worked FLOAT,
  paycode VARCHAR
);
