#!/usr/bin/env python3
"""
Task 3: Serializing and Deserializing with XML
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): dictionary to serialize
        filename (str): output XML filename
    """
    try:
        root = ET.Element("data")

        # Add each key/value as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, str(key))
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception:
        # Project statement doesn't specify return behavior,
        # so we fail silently (no crash).
        pass


def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.

    Args:
        filename (str): input XML filename

    Returns:
        dict: reconstructed dictionary (values as strings)
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text if child.text is not None else ""
        return result
    except Exception:
        return {}
