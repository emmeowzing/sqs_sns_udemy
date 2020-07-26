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
from datetime import datetime as dt


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


def sqs_queue_subscription(client: Any, arn: str, queue_arn: str) -> Dict:
    """
    Subscribe a queue to an SNS Topic.

    Args:
        client: SNS client object.
        arn: arn of a topic.
        queue_arn: arn of a queue to send messages to.

    Returns:
        The response object from creating the subscription.
    """
    return client.subscribe(
        TopicArn=arn,
        Protocol='sqs',
        Endpoint=queue_arn
    )


def get_topic_subscriptions(client: Any, arn: str) -> Dict:
    """
    Get a topic's subcribers.

    Args:
        client: SNS client object.
        arn: arn of a topic.

    Returns:
        A list of details about subscribers.
    """
    return client.list_subscriptions_by_topic(
        TopicArn=arn
    )


def opt_out(client: Any, arn: str, endpoint: str) -> Dict:
    """
    Opt out of a subscription.

    Args:
        client: SNS client object.
        arn: arn of a topic.
        endpoint: the endpoint that's opting out of a subscription to the topic.

    Returns:
        A response object after opting out.
    """
    #return client.unsubscribe(
    #    SubscriptionArn
    #)


def publish(client: Any, arn: str, message: str) -> Dict:
    """
    Publish a message to all subscribers of a topic.

    Args:
        client: SNS client object.
        arn: arn of a topic.

    Returns:
        A reponse object.
    """
    return client.publish(
        TopicArn=arn,
        Message=message
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
    #print(json.dumps(sms_subscription(client, example_topic_arn, env['PHONE'])))

    # SQS queue subscription to my topic.
    print(json.dumps(sqs_queue_subscription(client, example_topic_arn, env['QUEUE_ARN'])))

    # Get subscribers to a topic.
    print(json.dumps(get_topic_subscriptions(client, example_topic_arn)))

    ## Opting out of a subscription.

    ## Publishing a message to subscribers.
    example_message = {
        'MessageAttributes': {
            'Title': {
                'DataType': 'String',
                'StringValue': 'My example message'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'Example Author'
            },
            'Date': {
                'DataType': 'String',
                'StringValue': str(dt.now())
            }
        },
        'MessageBody': 'This is my first SQS message!!! :D :D'
    }
    # This call sends me a text ;) which is pretty neat.
    print(json.dumps(publish(client, example_topic_arn, str(example_message))))