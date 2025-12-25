#!/usr/bin/python3
"""Defines a function that reads a UTF-8 text file and prints it to stdout."""


def read_file(filename=""):
    """Read a text file (UTF-8) and print its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
