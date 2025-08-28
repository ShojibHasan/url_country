"""
URL Country Package

A Python package to determine the country of a URL/domain using multiple methods
including TLD analysis, WHOIS lookup, DNS resolution, and GeoIP geolocation.
"""

__version__ = "1.0.0"
__author__ = "Mahfujul Hasan"
__email__ = "shojibhasan15@gmail.com"

from .geolocation import get_region

__all__ = ["get_region"]
