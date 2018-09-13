# Odoo-S3-Storage

## Dependencies
`Odoo-S3-Storage` uses [`boto3`](https://github.com/boto/boto3) to talk to DigitalOcean. You will need to install it on the host running Odoo.

##Installation
```
pip install boto3
cd $ODOO_ADDONS_PATH
git clone https://github.com/HP-bkeys/odoo-s3-storage.git
```

## Compatibility
This module was written for **Odoo v10.0** and is only tested with this particular version. There is no warranty the addon
will work for other releases.

## Configuration
In order to use `Odoo-S3-Storage` you will need to switch to "Developer mode" and define a new system parameter as follow

```
ir_attachment.location  --->  s3://<Your-AWS-Access-Key-ID>:<Your-AWS-Secret-Key>@<Your-S3-Bucket-name>&<Your-DigitalOcean-base-url>

```

## Additional Information
This module is based on `Odoo-S3`(https://github.com/tvanesse/odoo-s3) and  `Odoo-S3-Storage`(https://github.com/bolstycjw/odoo-s3-storage). The code was rewritten to work with **Odoo v10.0**, uses boto3 instead of boto, and works with DigitalOcean Spaces.
