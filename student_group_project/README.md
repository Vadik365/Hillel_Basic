# Student Group Project

## Description
This project implements a simple student group system using OOP principles in Python.

## Project structure
- `human.py` — base Human class
- `student.py` — Student class with `__eq__` and `__hash__`
- `group.py` — Group class with add, delete, find methods
- `exceptions.py` — custom exception for group limit
- `main.py` — script for checking functionality

## Features
- Add student to group
- Delete student by last name
- Find student by last name
- Compare students correctly
- Limit group size to 10 students
- Raise and handle custom exception when adding the 11th student

## Run
```bash
python main.py