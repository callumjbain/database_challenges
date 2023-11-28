Record
-- Students

Properties
-- student_names
-- student_cohort

id: SERIAL
student_names: text
student_cohort: int

CREATE TABLE sutdents (
    id SERIAL PRIMARY KEY, 
    student_name text,
    student_cohort int
);