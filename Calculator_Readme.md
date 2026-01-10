# Calculator.py README

## Overview

This is a versatile command-line calculator written in Python. It supports basic arithmetic operations, advanced mathematical functions, and handles single, dual, or multiple number inputs. The calculator includes a menu-driven interface, direct expression evaluation mode, and calculation history tracking.

The script is designed to be user-friendly, with clear prompts, error handling for invalid inputs, and emoji-based feedback for better readability.

## Features

- **Multiple Input Modes**:
  - Single number operations (e.g., square root, sine).
  - Two-number operations (e.g., addition, power).
  - Multiple number operations (e.g., sum, average).

- **Supported Operations**:
  - Basic: Addition (+), Subtraction (-), Multiplication (*), Division (/), Modulus (%), Power (^).
  - Unary: Square Root (sqrt), Square (sq), Logarithm base 10 (log), Natural Log (ln), Sine (sin), Cosine (cos), Tangent (tan), Factorial (!), Absolute Value (abs), Negate (neg).
  - Aggregate: Average (avg), Maximum (max), Minimum (min).

- **Direct Expression Mode**: Evaluate complex expressions like `(2 + 3) * sqrt(16)` directly, with support for functions like sin, cos, tan, log, ln, and sqrt.

- **History**: View recent calculations (up to the last 10 shown, but all are stored).

- **Error Handling**: Graceful handling of invalid inputs, division by zero, negative square roots, etc.

- **Trigonometric Functions**: Angles in degrees (automatically converted to radians internally).

## Requirements

- Python 3.x (tested on Python 3.12, but compatible with most versions).
- Standard libraries: `math` (for mathematical functions). No external dependencies required.
- Note: The script imports `re` but it is not used in the current version (possible remnant from development).

## How to Run

1. **Download the Script** : Save the code as `Calculator.py`.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `Calculator.py`.
   - Execute: `python Calculator.py` (or `python3 Calculator.py` on some systems).

3. **Exit the Calculator**:
   - Select option `0` from the main menu, or use Ctrl+C (KeyboardInterrupt) to stop.

## Usage Instructions

### Main Menu
Upon starting, you'll see the welcome message and main menu:

```
🧮 CALCULATOR 
============================================================

🎯 MODE SELECTION:
  1. Standard Calculator (select number of inputs)
  2. Direct Expression Mode (type full expressions)
  3. View History
  0. Exit

Select mode (0-3): 
```

- **Mode 1: Standard Calculator**
  - Choose the number of inputs: 1 (single), 2 (two numbers), 3 (multiple numbers), or 0 to cancel.
  - Input numbers as prompted (supports floats and integers).
  - Select an operation from the available list.
  - View the result, which is added to history.
  - For multiple numbers: Enter separated by spaces or commas (e.g., `1, 2, 3` or `1 2 3`).

- **Mode 2: Direct Expression Mode**
  - Enter mathematical expressions directly (e.g., `2 + 3 * 4`, `sqrt(25)`, `sin(45) + cos(45)`).
  - Supports parentheses for grouping.
  - Trig functions assume degrees.
  - Type `back` to return to the main menu.
  - Results are displayed immediately, but not added to history.

- **Mode 3: View History**
  - Displays the last 10 calculations (or all if fewer).
  - Shows total number of calculations performed in the session.

- **Continue or Exit**:
  - After each operation (except in expression mode), you'll be asked: `Continue with calculator? (y/n):`.
  - Enter `y` to continue or `n` to exit.

### Full Operations Menu
Displayed in the script for reference:

```
🔢 NUMBER OF INPUTS:
  1. Single Number Operations
  2. Two Numbers
  3. Multiple Numbers
  0. Exit

📊 OPERATIONS AVAILABLE:
  +   : Addition
  -   : Subtraction
  *   : Multiplication
  /   : Division
  %   : Modulus (Remainder)
  ^   : Power
  sqrt: Square Root
  sq  : Square (x²)
  log : Logarithm (base 10)
  ln  : Natural Logarithm
  sin : Sine (in degrees)
  cos : Cosine (in degrees)
  tan : Tangent (in degrees)
  !   : Factorial
  avg : Average of numbers
  max : Maximum of numbers
  min : Minimum of numbers
```

Note: Operations are filtered based on input mode (e.g., single-number ops only show unary functions).

## Examples

### Single Number (Mode 1, Choice 1)
- Input: Number = 16, Operation = sqrt
- Output: `√16 = 4.0`

### Two Numbers (Mode 1, Choice 2)
- Input: First = 5, Second = 3, Operation = ^
- Output: `5^3 = 125.0`

### Multiple Numbers (Mode 1, Choice 3)
- Input: Numbers = 1 2 3 4, Operation = avg
- Output: `avg(1.0, 2.0, 3.0, 4.0) = 2.5`

### Direct Expression (Mode 2)
- Input: `(10 + 2) * sqrt(9)`
- Output: `(10 + 2) * sqrt(9) = 36.0`

### History (Mode 3)
- After a few calculations:
  ```
  📜 CALCULATION HISTORY:
  ============================================================
  1. √16 = 4.0
  2. 5^3 = 125.0
  3. avg(1.0, 2.0, 3.0, 4.0) = 2.5

  Total calculations: 3
  ```

## Limitations

- **Factorial (!)**: Only for non-negative integers (uses `math.factorial`).
- **Trigonometric Functions**: Input in degrees; outputs rounded to 6 decimal places.
- **Expression Mode**: Limited to supported functions; no variables or advanced scripting. Unsafe inputs may raise errors (e.g., invalid syntax).
- **History**: Stored in memory only (clears on exit). No persistent storage.
- **No GUI**: Command-line only.
- **Precision**: Uses floating-point arithmetic, so large numbers or divisions may have precision issues.
- **Security**: Expression mode uses `eval()` with restricted globals, but avoid running untrusted inputs.

## Contributing

Feel free to fork and improve! Suggestions:
- Add more functions (e.g., exponential, inverse trig).
- Implement persistent history (e.g., save to file).
- Remove unused imports (e.g., `re`).

## License

This script is open-source and free to use/modify under the MIT License.

Author: [Omkar Shirse]  
