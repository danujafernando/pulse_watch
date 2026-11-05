# PulseWatch

PulseWatch is an API availability monitoring project. The goal is to let users
register APIs, check whether they are available, track response times, and
identify failures. AI-assisted incident investigation may follow later.

The first version is intentionally small: build something useful, then improve
the architecture as the product grows.

> **Early development:** This repository is currently a starter scaffold. API
> registration, scheduled checks, response-time history, failure tracking, and
> incident investigation have not been implemented yet.

## Requirements

- Python 3.15 or newer
- [uv](https://docs.astral.sh/uv/)

## Getting started

Clone the repository and enter its directory, then install the project
dependencies:

```bash
uv sync
```

Run the current command-line entry point:

```bash
uv run pulse-watch
```

At this stage, it prints a greeting; it does not start a monitoring service.

## Project direction

The planned capabilities are:

- Register APIs to monitor.
- Check availability and record response times.
- Surface failures so users can see when an API is unhealthy.
- Explore AI-assisted incident investigation as a later step.

These are goals, not features available in the current scaffold. The initial
implementation will favor a straightforward, working foundation over
prematurely complex architecture.

## Development

Install dependencies with `uv sync`, then run the project with
`uv run pulse-watch`. The project is packaged from `src/pulse_watch` and uses
FastAPI; application routes and a server entry point have not been added yet.