#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

# [!] the right way of enabling outside-of-shell running of project-specific 
# scripts
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'unifi.settings'

import qrcode
from django.contrib.auth.models import User




if __name__ == "__main__":

    URI_PATTERN = "http://un.ifi.uio.no/users/{0}"
    STORAGE_PATH = "./static_base/images/users"

    users = User.objects.all()

    for u in users:
        user_id = u.pk
        uri = URI_PATTERN.format( user_id )
        code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=4,
            border=1
        )
        code.add_data( URI_PATTERN.format( u.pk ) )
        code.make( fit=True )
        code_image = code.make_image()
        
        with open( "%s/%s.png" % (STORAGE_PATH, user_id), "w" ) as output:
            code_image.save( output )