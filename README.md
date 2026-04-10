```markdown
# Todo Manager CLI

A simple command‑line task manager written in Python that allows users to create, view, complete, and delete tasks. Tasks are stored in a JSON file so they remain available between program runs.

This project was built to practice fundamental Python programming concepts such as modular code organization, file handling, JSON data storage, and basic command‑line application design.

## Overview

The application provides a small interactive command‑line interface that helps users manage their tasks directly from the terminal. Each task contains a unique identifier, a title, a completion status, and a creation timestamp.

The project is intentionally structured in a modular way. The command‑line interface is separated from the task management logic and the storage logic. This design improves code readability and maintainability while reflecting how real software projects are organized.

## Features

The task manager provides the following functionality:

- Add new tasks
- View all existing tasks
- Mark tasks as completed
- Delete tasks
- Automatic task ID generation
- Persistent task storage using JSON
- Modular project structure

Each task includes a unique ID and a timestamp, making it easier to track and manage tasks over time.

## Project Structure

```
todo-manager
│
├── main.py
├── todo
│   ├── __init__.py
│   ├── manager.py
│   └── storage.py
│
├── tasks.json
├── README.md
└── .gitignore
```

**main.py**

The entry point of the application. It provides the command‑line interface, displays the menu, and handles user input.

**todo/manager.py**

Contains the core logic for managing tasks, including creating tasks, listing tasks, marking them as completed, and deleting them.

**todo/storage.py**

Handles reading and writing tasks to the JSON file used for persistent storage.

**tasks.json**

Stores all tasks created during program execution.

## Requirements

- Python 3.x

You can check your Python installation using:

```
python --version
```

or

```
python3 --version
```

## Running the Program

Navigate to the project directory and run the program:

```
python main.py
```

or

```
python3 main.py
```

After running the program, a simple menu will appear in the terminal. Select an option by entering the corresponding number.

Example:

```
Todo Manager

1. Add task
2. List tasks
3. Complete task
4. Delete task
5. Exit
```

Example output when listing tasks:

```
1 | [✗] Learn Python
2 | [✔] Build CLI project
3 | [✗] Practice algorithms
```

## Task Data Structure

Tasks are stored in a JSON file using the following structure:

```
{
  "id": 1,
  "title": "Learn Python",
  "done": false,
  "created_at": "2026-04-09T10:12:00"
}
```

This structure allows the application to easily manage and update tasks.

## Concepts Practiced

This project focuses on strengthening several core Python concepts, including modular project structure, working with JSON files, implementing a simple command‑line interface, separating application logic from storage logic, and managing structured data using dictionaries and lists.

## Possible Improvements

Several improvements could make this project more powerful and realistic. For example, the interface could be converted to a command‑based CLI using argparse, tasks could support editing and due dates, filtering tasks by status could be added, and automated tests could be written to ensure the reliability of the task manager.

## License

This project is intended for learning and educational purposes.
```