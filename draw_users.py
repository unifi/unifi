#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

import qrcode
from unifi import *
from django.contrib.auth.models import User

if __name__ == "__main__":

    URI_PATTERN = "http://un.ifi.uio.no/users/{0}"
    STORAGE_PATH = "./static_base/images/users"

    from student.models import Student

    users = User.objects.all()

    for u in users:
        user_id = u.pk
        uri = URI_PATTERN.format( user_id )
        code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=4,
            border=2
        )
        code.add_data( URI_PATTERN.format( u.pk ) )
        code.make( fit=True )
        code_image = code.make_image()

        with open( "%s/%s.png" % (STORAGE_PATH, user_id), "w" ) as output:
            code_image.save( output )