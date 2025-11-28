# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Advent of Code 2024 solutions in Python. Uses uv for package management and requires Python 3.14+.

## Commands

```bash
# Run a specific day's solution
uv run aoc <day>           # Run both parts
uv run aoc <day> -p 1      # Run only part 1
uv run aoc <day> -p 2      # Run only part 2
uv run aoc <day> -s        # Run with sample input
uv run aoc <day> -s -p 1   # Sample input, part 1 only
```

## Architecture

### Solution Structure

Each day's solution goes in `src/aoc/days/dayXX.py` (zero-padded, e.g., `day01.py`).

Two supported patterns for solution modules:

1. **Single function style** - implement `solve(input_text) -> (part1_answer, part2_answer)`
2. **Two function style** - implement `solve_part1(input_text)` and `solve_part2(input_text)`

### Input Files

- Main inputs: `inputs/dayXX.txt` (e.g., `inputs/day01.txt`)
- Sample inputs: `inputs/dayXX_sample.txt` (e.g., `inputs/day01_sample.txt`)

### Runner

`src/aoc/runner.py` handles CLI parsing, dynamic module loading, and input file reading.
