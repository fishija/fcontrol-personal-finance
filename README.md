# FControl

Personal finance control application. Python 3.13, PySide6 (Qt6), SQLite.

## Core Concepts

- **Transaction-based** — every balance change is a tracked transaction
- **Rule-based income allocation** — income is distributed across pockets via ordered rules (fixed amount, percentage, or target balance)
- **Goal contributions** — goals don't hold money; they track contributions reserved within a pocket

## Entity Structure

```
Pocket
├── balance, currency
├── reserved_amount (computed from goal contributions)
├── has many → Transactions
├── has many → Allocation Rules (ordered)
└── has many → Goals
    └── has many → Goal Contributions (amount, date, note)
```

| Entity | Purpose |
|--------|---------|
| **Pocket** | A container for money (bank account, cash, card). Holds balance and currency. |
| **Transaction** | Income or expense against a pocket. Tracks source (manual, allocation, adjustment). |
| **Allocation Rule** | Defines how income is split: fixed amount, % of income, or target balance. Ordered by position. |
| **Goal** | A savings target within a pocket. Progress computed from contributions. |
| **Goal Contribution** | A recorded amount saved toward a goal. Sum = pocket's reserved amount. |

## Architecture

Package-by-layer structure:

```
models/       → dataclasses + repositories (DB access)
services/     → business logic, validation
controllers/  → QObject layer connecting views to services
ui/views/     → BaseWidget/BaseDialog subclasses
ui/qt_generated/ → auto-generated from .ui files (never edit)
```

## Running

```bash
uv run fcontrol
```

## Ideas / Roadmap

- Pocket types (cash, card, investment)
- "All remaining" allocation rule option
- Home dashboard with summaries
