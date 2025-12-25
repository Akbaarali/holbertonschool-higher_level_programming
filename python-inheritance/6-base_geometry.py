#!/usr/bin/python3
"""Defines BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")
