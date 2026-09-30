# UML Intro — Library Loan System

## About the project
This project is my first step into software modeling with UML. The goal is to read a problem description and translate it into **Mermaid diagrams** (a class diagram and a sequence diagram) without adding anything that isn't in the text.

## The problem (summary)
A small library wants to manage its books and users. The system revolves around a `Library` that manages books, users, and loans. When a user borrows a book, a `Loan` is created.

## Repository structure
```
holbertonschool-sw_design_architecture/
└── uml_intro/
    ├── 0-class_diagram.mmd
    ├── 1-sequence_diagram.mmd
    └── README.md
```

| File | Description |
|---|---|
| `0-class_diagram.mmd` | Mermaid class diagram of the system |
| `1-sequence_diagram.mmd` | Mermaid sequence diagram of a user borrowing a book |

## Requirements
- Ubuntu 20.04
- A Mermaid-compatible renderer (e.g. [mermaid.live](https://mermaid.live))
- Python-style data types (`str`, `bool`, `date`)
- File and element names must match the problem statement exactly

## 0. Class diagram

```mermaid
classDiagram
    class Book {
        +str title
        +str author
        +bool state
        +mark_as_unavailable()
        +mark_as_available()
    }
    class User {
        +str name
        +str email
    }
    class Loan {
        +date start_date
        +date end_date
        +close_loan()
    }
    class Library {
        +add_book()
        +register_user()
        +create_loan()
    }
    Loan "*" --> "1" Book
    Loan "*" --> "1" User
    Library "1" o-- "*" Book
    Library "1" o-- "*" User
    Library "1" o-- "*" Loan
```

### Design decisions

**Classes, attributes, and methods** are taken directly from the problem statement. `Library` has no attributes because none are described.

**Association (`-->`) between `Loan` and `Book` / `User`**
- A `Loan` cannot exist without a book and a user (it must *reference* them).
- A `Book` or `User` can exist without any loans.
- Each `Loan` has exactly one `Book` and one `User` (`1`); a `Book` or `User` can have many loans over time (`*`).

**Aggregation (`o--`) between `Library` and `Book` / `User` / `Loan`**
- The `Library` *manages* all three.
- If the `Library` is removed, books and users still exist independently, so this is aggregation and not composition.
- One `Library` manages many of each (`1` to `*`).

## 1. Sequence diagram

Use case: a user borrows a book from the library.

```mermaid
sequenceDiagram
    participant User
    participant Library
    participant Book
    User->>Library: create_loan()
    Library->>Book: mark_as_unavailable()
    create participant Loan
    Library->>Loan: close_loan()
    Library-->>User: loan created
```

### Design decisions

- `User`, `Library`, and `Book` are declared at the start because they already exist before the interaction begins.
- `Loan` is not declared at the start. It appears only when it is created, using `create participant Loan`.
- The `User` starts the process by asking the `Library` to create a loan.
- The `Library` asks the `Book` to mark itself as unavailable, then creates the `Loan` and interacts with it.
- The last message is the `Library` confirming to the `User` with `loan created`.
- Method names match the class diagram exactly.

## How to view the diagrams
1. Open [mermaid.live](https://mermaid.live).
2. Paste the contents of a `.mmd` file.
3. Check that it renders without errors.

## Key concepts practiced
| Relationship | Symbol | Question to ask |
|---|---|---|
| Association | `-->` | Does one class reference the other? |
| Aggregation | `o--` | Does it contain the other, but the part can live on its own? |
| Composition | `*--` | If the whole is destroyed, is the part destroyed too? |

| Sequence arrow | Symbol | Meaning |
|---|---|---|
| Message | `->>` | A call from one participant to another |
| Reply | `-->>` | A return message or response |
