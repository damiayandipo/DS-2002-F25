# Survey Data Schema

| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `student_id` | `INT` | Unique identifier for the student. |
| `major` | `VARCHAR(50)` | Academic major or field of study. |
| `GPA` | `FLOAT` | Grade Point Average on a 4.0 scale. |
| `is_cs_major` | `BOOL` | Indicates if student is a Computer Science major. |
| `credits_taken` | `FLOAT` | Total number of academic credits completed. |

## Schema Notes:
- `student_id` must be unique and non-null
- `GPA` ranges from 0.0 to 4.0
- `credits_taken` represents cumulative credits
- `is_cs_major` is a boolean flag for CS major status
