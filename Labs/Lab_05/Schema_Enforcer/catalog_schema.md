# Course Catalog Schema

| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `name` | `VARCHAR(100)` | Full name of the instructor. |
| `role` | `VARCHAR(20)` | Role of the instructor (Primary, TA, Grader). |
| `course_course_id` | `VARCHAR(10)` | Unique course identifier code. |
| `course_title` | `VARCHAR(100)` | Official title of the course. |
| `course_level` | `INT` | Academic level of the course (100, 200, 300, etc.). |
| `course_section` | `VARCHAR(10)` | Specific section identifier for the course. |

## Schema Notes:
- One row per instructor per course section
- `course_course_id` follows department code + number format
- `course_level` indicates undergraduate level (100-400)
- `role` specifies the instructor's responsibility level
- Multiple instructors possible for a single course section
