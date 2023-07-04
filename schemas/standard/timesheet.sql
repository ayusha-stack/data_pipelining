DROP TABLE standard.timesheet;

CREATE TABLE standard.timesheet (
  employee_id VARCHAR,
  cost_center VARCHAR,
  punch_in_time TIME,
  punch_out_time TIME,
  punch_apply_date DATE,
  hours_worked FLOAT,
  paycode VARCHAR
);
