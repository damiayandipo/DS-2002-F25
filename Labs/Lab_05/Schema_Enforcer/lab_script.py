# lab_script.py
import csv
import json
import pandas as pd
import numpy as np

print("Starting Lab 5: Schema Contract Enforcer")

# Part 1: Acquisition and Flexible Formatting
print("\n=== Part 1: Data Acquisition ===")

# Task 1: Create the Tabular CSV Data (Requires Cleaning)
def create_raw_survey_data():
    print("Creating raw_survey_data.csv...")
    
    # Data with intentional type inconsistencies
    survey_data = [
        # Headers
        ['student_id', 'major', 'GPA', 'is_cs_major', 'credits_taken'],
        # Data with type issues
        [1001, 'Computer Science', 3.8, 'Yes', '45.5'],        # credits_taken as string
        [1002, 'Data Science', 3, 'Yes', '60.0'],              # GPA as integer
        [1003, 'Mathematics', 3.5, 'No', '42.75'],             # Proper types
        [1004, 'Statistics', '3.2', 'No', '38.0'],             # GPA as string
        [1005, 'Computer Science', 4.0, 'Yes', '52.5']         # Proper types
    ]
    
    with open('raw_survey_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(survey_data)
    
    print("raw_survey_data.csv created successfully!")

# Task 2: Create the Hierarchical JSON Data (Requires Normalization)
def create_raw_course_catalog():
    print("Creating raw_course_catalog.json...")
    
    # Hierarchical course data
    course_catalog = [
        {
            "course_id": "DS2002",
            "section": "001",
            "title": "Data Science Systems",
            "level": 200,
            "instructors": [
                {"name": "Austin Rivera", "role": "Primary"},
                {"name": "Heywood Williams-Tracy", "role": "TA"}
            ]
        },
        {
            "course_id": "DS3003",
            "section": "001", 
            "title": "Machine Learning Fundamentals",
            "level": 300,
            "instructors": [
                {"name": "Sarah Chen", "role": "Primary"},
                {"name": "Alex Johnson", "role": "TA"},
                {"name": "Maria Garcia", "role": "Grader"}
            ]
        },
        {
            "course_id": "STAT2020",
            "section": "002",
            "title": "Probability and Statistical Inference",
            "level": 200,
            "instructors": [
                {"name": "Robert Wilson", "role": "Primary"}
            ]
        }
    ]
    
    with open('raw_course_catalog.json', 'w') as file:
        json.dump(course_catalog, file, indent=2)
    
    print("raw_course_catalog.json created successfully!")

# Part 2: Data Validation and Type Casting
print("\n=== Part 2: Data Validation ===")

# Task 3: Clean and Validate the CSV Data
def clean_survey_data():
    print("Cleaning survey data...")
    
    # Load raw data
    df = pd.read_csv('raw_survey_data.csv')
    print("Raw data loaded:")
    print(df)
    print("\nRaw data types:")
    print(df.dtypes)
    
    # Enforce Boolean Type
    df['is_cs_major'] = df['is_cs_major'].replace({'Yes': True, 'No': False})
    
    # Enforce Numeric Types
    df['GPA'] = pd.to_numeric(df['GPA'], errors='coerce')
    df['credits_taken'] = pd.to_numeric(df['credits_taken'], errors='coerce')
    
    # Ensure student_id is integer
    df['student_id'] = df['student_id'].astype('int64')
    
    print("\nCleaned data:")
    print(df)
    print("\nCleaned data types:")
    print(df.dtypes)
    
    # Save cleaned data
    df.to_csv('clean_survey_data.csv', index=False)
    print("clean_survey_data.csv saved successfully!")

# Task 4: Normalize the JSON Data
def normalize_course_catalog():
    print("Normalizing course catalog data...")
    
    # Load JSON data
    with open('raw_course_catalog.json', 'r') as file:
        course_data = json.load(file)
    
    print("Raw JSON data structure:")
    print(json.dumps(course_data[:1], indent=2))  # Show first item as sample
    
    # Normalize with record_path for instructors
    df_normalized = pd.json_normalize(
        course_data,
        record_path=['instructors'],
        meta=['course_id', 'title', 'level', 'section'],
        meta_prefix='course_'
    )
    
    print("\nNormalized data:")
    print(df_normalized)
    print("\nNormalized data types:")
    print(df_normalized.dtypes)
    
    # Save normalized data
    df_normalized.to_csv('clean_course_catalog.csv', index=False)
    print("clean_course_catalog.csv saved successfully!")
    
    return df_normalized

# Part 3: The Schema Contract
print("\n=== Part 3: Schema Documentation ===")

# Task 5: Document the Tabular Schema
def create_survey_schema():
    print("Creating survey_schema.md...")
    
    schema_content = """# Survey Data Schema

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
"""
    
    with open('survey_schema.md', 'w') as file:
        file.write(schema_content)
    
    print("survey_schema.md created successfully!")

# Task 6: Document the Normalized Catalog Schema
def create_catalog_schema():
    print("Creating catalog_schema.md...")
    
    schema_content = """# Course Catalog Schema

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
"""
    
    with open('catalog_schema.md', 'w') as file:
        file.write(schema_content)
    
    print("catalog_schema.md created successfully!")

# Run all functions
if __name__ == "__main__":
    create_raw_survey_data()
    create_raw_course_catalog()
    clean_survey_data()
    normalize_course_catalog()
    create_survey_schema()
    create_catalog_schema()
    print("\n=== Lab 5 Complete! ===")
    print("All files generated successfully!")