#!/usr/bin/env python3
"""
Created by: Gustav I.
Modified on: March 16, 2025
This module shows how local and global variables work with different values.
"""


# global variable
variable_x = 75


def local_variable() -> None:
    """The local_variable() function creates local variables, returns None."""
    variable_x = 20
    variable_y = 35

    variable_x = variable_x * 2  # Changed from +1 to *2
    variable_z = variable_x - variable_y  # Changed calculation

    print(f"Local variable:  {variable_x} - {variable_y} = {variable_z}")


def global_variable() -> None:
    """The global_variable() function uses a global variable, returns None."""
    global variable_x
    variable_y = 25

    variable_x = variable_x // 5  # Changed from +1 to integer division
    variable_z = variable_x + variable_y  # Changed calculation

    print(f"Global variable: {variable_x} + {variable_y} = {variable_z}")


def main() -> None:
    """The main() function shows local and global variables, returns None."""
    local_variable()
    global_variable()

    print("\nDone.")


if __name__ == "__main__":
    main()
