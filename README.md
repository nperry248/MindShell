# MindShell

A natural language terminal interface for macOS. Type what you want to do in plain English — MindShell translates it into a shell command using Google Gemini, shows it to you, and runs it on confirmation.

```
USER (~): show me all files modified in the last 24 hours
AI suggests: find . -mtime -1 -type f
Execute this command? [y/n]: y
```

## Features

- Converts plain English to zsh/bash commands via Gemini AI
- Always shows the generated command before running — you stay in control
- Handles `cd` correctly (updates your working directory in the session)
- Basic safety filter blocks destructive commands
- Context-aware — passes your current directory to the model

## Setup

**1. Clone and install dependencies**
```bash
git clone https://github.com/nperry248/MindShell.git
cd MindShell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**2. Add your Gemini API key**

Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

Get a free key at [Google AI Studio](https://aistudio.google.com/).

**3. Run**
```bash
python main.py
```

Type `exit` or `quit` to close, or press `Ctrl+C`.

## Stack

- Python 3.11
- [Google Gemini](https://ai.google.dev/) (gemini-2.5-flash-lite)
- [Rich](https://github.com/Textualize/rich) for terminal UI
