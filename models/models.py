# -*- coding: utf-8 -*-
"""
    s3-storage.models
    ~~~~~~~~~~~~~~~~~

    Use s3 as file storage mechanism

    :copyright: (c) 2017 by Marc Lijour, brolycjw.
    :license: MIT License, see LICENSE for more details.
"""

import hashlib
import base64

from odoo import models

from . import s3_helper


class S3Attachment(models.Model):
    """Extends ir.attachment to implement the S3 storage engine
    """
    _inherit = "ir.attachment"

    def _connect_to_S3_bucket(self, s3, bucket_name):
        s3_bucket = s3.Bucket(bucket_name)
        exists = s3_helper.bucket_exists(s3, bucket_name)

        if not exists:
            s3_bucket = s3.create_bucket(Bucket=bucket_name)
        return s3_bucket

    def _file_read(self, fname, bin_size=False):
        storage = self._storage()
        if storage[:5] == 's3://':
            access_key_id, secret_key, bucket_name, encryption_enabled = s3_helper.parse_bucket_url(storage)
            s3 = s3_helper.get_resource(access_key_id, secret_key)
            s3_bucket = self._connect_to_S3_bucket(s3, bucket_name)
            file_exists = s3_helper.object_exists(s3, s3_bucket.name, fname)
            if not file_exists:
                # Some old files (prior to the installation of odoo-s3) may
                # still be stored in the file system even though
                # ir_attachment.location is configured to use S3
                try:
                    read = super(S3Attachment, self)._file_read(fname, bin_size=False)
                except Exception:
                    # Could not find the file in the file system either.
                    return False
            else:
                s3_key = s3.Object(s3_bucket.name, fname)
                read = base64.b64encode(s3_key.get()['Body'].read())
        else:
            read = super(S3Attachment, self)._file_read(fname, bin_size=False)
        return read

    def _file_write(self, value, checksum):
        storage = self._storage()
        if storage[:5] == 's3://':
            access_key_id, secret_key, bucket_name, encryption_enabled = s3_helper.parse_bucket_url(storage)
            s3 = s3_helper.get_resource(access_key_id, secret_key)
            s3_bucket = self._connect_to_S3_bucket(s3, bucket_name)
            bin_value = base64.b64decode(value)
            fname = hashlib.sha1(bin_value).hexdigest()
            if encryption_enabled:
                s3.Object(s3_bucket.name, fname).put(Body=bin_value, ServerSideEncryption='AES256')
            else:
                s3.Object(s3_bucket.name, fname).put(Body=bin_value)

        else: # falling back on Odoo's local filestore
            fname = super(S3Attachment, self)._file_write(value, checksum)

        return fname

