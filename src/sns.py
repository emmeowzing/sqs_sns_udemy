#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Working with AWS SNS now, again for the following Udemy course.

https://www.udemy.com/course/working-with-sqs-and-sns-aws-with-python-and-boto3-series/
"""

from typing import Any, Dict

import boto3
import json

from settings import env


def sns_client() -> Any:
    """
    Get an SNS client object.

    Returns:
        An SNS client.
    """
    return boto3.client('sns', region_name='us-east-1')


def create_topic(client: Any, name: str) -> Any:
    """
    Create an SNS subscription topic.

    Args:
        client: SNS client object.
        name: name of the topic.

    Returns:
        Response object.
    """
    return client.create_topic(
        Name=name
    )


def get_all_topics(client: Any) -> Dict:
    """
    Get all topics on AWS.

    Args:
        client: SNS client object.
    
    Returns:
        A list of SNS topics.
    """
    return client.list_topics()


def get_topic_attributes(client: Any, arn: str) -> Dict:
    """
    Get a topic's attributes.

    Args:
        client: SNS client object.
        arn: arn of a topic.

    Returns:
        A dictionary of topic attributes.
    """
    return client.get_topic_attributes(
        TopicArn=arn
    )
    

def delete_topic(client: Any, arn: str) -> Dict:
    """
    Delete a topic.

    Args:
        client: SNS client object.
        arn: arn of a topic.

    Returns:
        The response object from deleting a topic.
    """
    return client.delete_topic(
        TopicArn=arn
    )


def email_subscription(client: Any, arn: str, email: str) -> Dict:
    """
    Create an email subscription.

    Args:
        client: SNS client object.
        arn: arn of a topic.
        email: the email to subscribe.

    Returns:
        The response object from creating the susbcription.
    """
    return client.subscribe(
        TopicArn=arn,
        Protocol='email',
        Endpoint=email
    )


def sms_subscription(client: Any, arn: str, sms: str) -> Dict:
    """
    Create an SMS subscription.

    Args:
        client: SNS client object.
        arn: arn of a topic.
        sms: the number to subscribe.

    Returns:
        The response object from creating the susbcription.
    """
    return client.subscribe(
        TopicArn=arn,
        Protocol='sms',
        Endpoint=sms
    )


if __name__ == '__main__':
    client = sns_client()

    ## Create an example topic we can play with.

    # Create a topic and get its ARN.

    print(json.dumps(create_topic(client, name='EXAMPLE_TOPIC')))
    topics = get_all_topics(client)
    for topic in topics['Topics']:
        if topic['TopicArn'].endswith('EXAMPLE_TOPIC'):
            example_topic_arn = topic['TopicArn']
    
    # Print our topic's attributes (which will be default).

    print(json.dumps(get_topic_attributes(client, example_topic_arn)))

    # Delete a topic.

    #print(json.dumps(delete_topic(client, example_topic_arn)))

    ## Subscriptions

    # Email subscription to our topic! :D

    #print(json.dumps(email_subscription(client, example_topic_arn, env['EMAIL'])))

    # SMS subscription to our topic!

    print(json.dumps(sms_subscription(client, example_topic_arn, env['PHONE'])))