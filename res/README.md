## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [File Structure](#file-structure)
- [How It Works](#how-it-works)
- [Functionality](#functionality)
- [Customization](#customization)
- [Conclusion](#Conclusion)

## Overview

The calculator is designed to allow users to perform basic arithmetic calculations. It features a clean layout, digit buttons, operation buttons, and special function buttons (like clear and backspace). The application is built to be easily customizable via a theme configuration file.

## Requirements

To run this project, ensure you have the following installed:

- Python (version 3.7 or higher)
- Tkinter library (included with standard Python installations)

## File Structure

```
calculator/
├── calculator.py         # Main script for the calculator application
└── theme.ini             # Configuration file for themes
```

## How It Works

### Main Components

1. **Importing Libraries**:
   The script imports the necessary libraries:
   ```python
   import tkinter as tk
   from configparser import ConfigParser
   ```

2. **Theme Loading**:
   The `load_theme(theme_name)` function reads the `theme.ini` file to load color configurations for the calculator's interface. If the specified theme is not found, it defaults to the "Classic" theme.

3. **Calculator Class**:
   The core functionality of the calculator is encapsulated in the `Calculator` class, which initializes the application window, sets up the display, and handles user interactions.

### Key Methods

- **Initialization (`__init__`)**: 
  The constructor initializes the main window, sets up the layout, and creates buttons for digits, operators, and special functions.

- **Creating Buttons**:
  The methods `create_digit_buttons()`, `create_operator_buttons()`, and `create_special_buttons()` create and arrange buttons in the interface. Each button is linked to a specific function via the `command` parameter.

- **Updating Labels**:
  The methods `update_label()` and `update_total_label()` are responsible for updating the displayed expressions in the calculator's UI.

- **Handling Input**:
  The `add_to_expression(value)`, `append_operator(operator)`, and `evaluate()` methods handle user input, perform calculations, and update the display accordingly.

- **Special Functions**:
  Methods like `clear()`, `backspace()`, `square()`, and `sqrt()` handle specific operations related to the calculator's functionality.

### User Input Handling

The application binds keyboard inputs for digits and operations, allowing users to interact with the calculator using both the mouse and keyboard. For example, pressing the `Enter` key triggers the evaluation of the current expression.

## Functionality

- **Basic Arithmetic Operations**: 
  Users can perform addition, subtraction, multiplication, and division using the respective buttons.

- **Square and Square Root**: 
  Users can calculate the square of a number and the square root.

- **Clear and Backspace**: 
  The "C" button clears the current input, while the backspace button removes the last character from the input.

## Customization

The appearance of the calculator can be customized by editing the `theme.ini` file. Users can define their own themes by specifying colors for various elements (buttons, backgrounds, labels, etc.).

### Example Theme Structure

```ini
[default]
theme_name = Gray

[Gray]
DARK_GRAY = #1E1E1E
MEDIUM_GRAY = #3C3C3C
LIGHT_GRAY = #E1E1E1
BUTTON_BACKGROUND = #FFFFFF
```

## Conclusion

This calculator project serves as a practical application for learning GUI programming with Tkinter. Users are encouraged to modify the code and experiment with new features to enhance their understanding of Python and software development.

