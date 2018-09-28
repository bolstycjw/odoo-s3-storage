# odoo-s3

## Dependencies
`Odoo-S3-Storage` uses [`boto3`](https://github.com/boto/boto3) to talk to DigitalOcean. You will need to install it on the host running Odoo.

## Installation
Make sure you set the `ODOO_ADDONS_PATH` variable to the directory where you install your custom Odoo modules.
 
```
pip install boto3
cd $ODOO_ADDONS_PATH
git clone https://github.com/HP-bkeys/odoo-s3-storage.git
```

## Compatibility
This module is compatible with **Odoo 11** and **Python 3**. For older versions, you can refer to the original source code (see credits below).

## Configuration
In order to use `odoo-s3` you will need to switch to "Developer mode" and define a new system parameter as follows:

* without encryption:
```
ir_attachment.location  --->  s3://<Your-AWS-Access-Key-ID>:<Your-AWS-Secret-Key>@<Your-S3-Bucket-name>&<Your-DigitalOcean-base-url>

```
* with server-side encryption (only AES256, since [aws:kms is not supported in boto3](https://github.com/boto/botocore/issues/471)):
```
ir_attachment.location  --->  s3://<Your-AWS-Access-Key-ID>:<Your-AWS-Secret-Key>@<Your-S3-Bucket-name>+SSE

## Additional Information
This module is based on `Odoo-S3`(https://github.com/tvanesse/odoo-s3) and  `Odoo-S3-Storage`(https://github.com/bolstycjw/odoo-s3-storage). The code was rewritten to work with **Odoo v10.0**, uses boto3 instead of boto, and works with DigitalOcean Spaces.

## Additional Information and Credits
This code is [forked from brolycjw's repository](https://github.com/brolycjw/odoo-s3-storage) who ported the [original code from tvanesse](https://github.com/tvanesse/odoo-s3) to Odoo v10.0, and moving from boto to boto3.

