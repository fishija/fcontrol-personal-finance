# FControl

Personal finance control application. Python 3.13, PySide6 (Qt6), SQLite.

## Core Concepts

- **Transaction-based** — every balance change is a tracked transaction
- **Rule-based income allocation** — income is distributed across pockets via ordered rules (fixed amount, percentage, or target balance)
- **Goal movements** — goals don't hold money; they track contributions and withdrawals reserved within a pocket
- **Net worth tracking** — periodic snapshots of total balance across all pockets, converted to a single currency
- **Configurable default currency** — persisted via QSettings; changing it recalculates historical net worth snapshots using date-specific exchange rates

## Entity Structure

```
Pocket
├── balance, currency
├── reserved_amount (computed from goal contributions)
├── has many → Transactions
├── has many → Allocation Rules (ordered)
└── has many → Goals
    └── has many → Goal Movements (contribution or withdrawal, amount, date, note)

Net Worth Snapshot
├── amount (in default currency)
├── date
└── note
```

| Entity | Purpose |
|--------|---------|
| **Pocket** | A container for money (bank account, cash, card). Holds balance and currency. |
| **Transaction** | Income or expense against a pocket. Tracks source (manual, allocation, adjustment). |
| **Allocation Rule** | Defines how income is split: fixed amount, % of income, or target balance. Ordered by position. |
| **Goal** | A savings target within a pocket. Progress computed from movements. |
| **Goal Movement** | A contribution (+) or withdrawal (−) against a goal. Net sum = pocket's reserved amount. |
| **Net Worth Snapshot** | A point-in-time total of all pocket balances converted to the default currency. |

## Architecture

Package-by-layer structure:

```
models/       → dataclasses + repositories (DB access)
services/     → business logic, validation
controllers/  → QObject layer connecting views to services
ui/views/     → BaseWidget/BaseDialog subclasses
ui/qt_generated/ → auto-generated from .ui files (never edit)
settings.py   → AppSettings (QSettings wrapper for persisted preferences)
config.py     → constants (supported currencies)
```

## Features

- **Pockets** — create, edit, delete money containers with per-pocket currency
- **Transactions** — record income/expenses with categories, dates, descriptions
- **Allocation** — define ordered rules to split income across pockets/goals; run allocation in one click
- **Goals** — set savings targets with optional target dates; track progress via contributions and withdrawals; movements dialog shows pocket balance and available-for-contribution amount
- **Net Worth** — take snapshots, view history in a plotly bar chart, edit/delete past entries
- **Settings** — change default currency with automatic historical recalculation of net worth snapshots

## Dependencies

- **PySide6** — Qt6 UI framework
- **plotly** — interactive charts (net worth visualization)
- **currency_converter** — offline exchange rates for multi-currency conversion

## Running

```bash
uv run fcontrol
```

## Development

Compile `.ui` files after editing them in Qt Designer:

```bash
uv run python scripts/build_ui.py
```

## Ideas / Roadmap

- Pocket types (cash, card, investment)
- "All remaining" allocation rule option
- Home dashboard with summaries
