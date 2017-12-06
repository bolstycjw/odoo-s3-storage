# -*- coding: utf-8 -*-
{
    'name': "odoo-s3",

    'summary': """
        Stores attachments in Amazon S3 instead of the local drive""",

    'description': """
        In large deployments, Odoo workers need to share a distributed 
        filestore. Amazon S3 can store files (e.g. attachments and 
        pictures), such that all Odoo workers can access the same files.

        This module lets you configure access to an S3 bucket from Odoo,
        by settings a System parameter.
    """,

    'author': "Marc Lijour",
    'website': "https://github.com/marclijour/odoo-s3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # only the admin user should be having access
#    'data': [
        # 'security/ir.model.access.csv',
#    ],
}
