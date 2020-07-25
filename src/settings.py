#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Get environment variables / settings for import into another program.
"""

from dotenv import load_dotenv

load_dotenv()

import os

__all__ = [
    'env'
]

env = {
    'EMAIL': os.getenv('EMAIL'),
    'PHONE': os.getenv('PHONE')
}