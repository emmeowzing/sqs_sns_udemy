#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Working with AWS SNS now, again for the following Udemy course.

https://www.udemy.com/course/working-with-sqs-and-sns-aws-with-python-and-boto3-series/
"""

from typing import Any

import boto3
import json


def sns_client() -> Any:
    """
    Get an SNS client object.

    Returns:
        An SNS client.
    """
    return boto3.client('sns', region_name='us-east-1')


if __name__ == '__main__':
    ...