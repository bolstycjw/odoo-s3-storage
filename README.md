# odoo-s3

## Dependencies
`odoo-s3` uses [`boto3`](https://github.com/boto/boto3) to talk to Amazon S3. You will need to install it on the host running Odoo.

## Installation
Make sure you set the `ODOO_ADDONS_PATH` variable to the directory where you install your custom Odoo modules.
 
```
pip install boto3
cd $ODOO_ADDONS_PATH
git clone https://github.com/marclijour/odoo-s3
```

## Compatibility
This module is compatible with **Odoo 11** and **Python 3**. For older versions, you can refer to the original source code (see credits below).

## Configuration
In order to use `odoo-s3` you will need to switch to "Developer mode" and define a new system parameter as follows:

* without encryption:
```
ir_attachment.location  --->  s3://<Your-AWS-Access-Key-ID>:<Your-AWS-Secret-Key>@<Your-S3-Bucket-name>

```
* with server-side encryption (only AES256, since [aws:kms is not supported in boto3](https://github.com/boto/botocore/issues/471)):
```
ir_attachment.location  --->  s3://<Your-AWS-Access-Key-ID>:<Your-AWS-Secret-Key>@<Your-S3-Bucket-name>+SSE

```

## Additional Information and Credits
This code is [forked from brolycjw's repository](https://github.com/brolycjw/odoo-s3-storage) who ported the [original code from tvanesse](https://github.com/tvanesse/odoo-s3) to Odoo v10.0, and moving from boto to boto3.

