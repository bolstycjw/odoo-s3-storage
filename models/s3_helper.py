#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import botocore


def parse_bucket_url(bucket_url):
    scheme = bucket_url[:5]
    assert scheme == 's3://', \
        "Expecting an s3:// scheme, got {} instead.".format(scheme)

    try:
        remain = bucket_url.lstrip(scheme)
        access_key_id = remain.split(':')[0]
        remain = remain.lstrip(access_key_id).lstrip(':')
        do_space_url = remain.split('&')[1]
        remain = remain.rstrip(do_space_url).rstrip('&')
        secret_key = remain.split('@')[0]
        bucket_name = remain.split('@')[1]
        if not access_key_id or not secret_key:
            raise Exception(
                "No AWS access and secret keys were provided."
                " Unable to establish a connexion to S3."
            )
    except Exception:
        raise Exception("Unable to parse the S3 bucket url.")

    return (access_key_id, secret_key, bucket_name, do_space_url)


def bucket_exists(s3, bucket_name):
    exists = True
    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            exists = False
    return exists


def object_exists(s3, bucket_name, key):
    exists = True
    try:
        s3.meta.client.head_object(Bucket=bucket_name, Key=key)
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            exists = False
    return exists


def get_resource(access_key_id, secret_key, endpoint_url):
    session = boto3.Session(access_key_id, secret_key)
    s3 = session.resource('s3', endpoint_url='https://' + endpoint_url)
    return s3
