# -*- coding: utf-8 -*-

from StatusCode import BaseStatusCode, StatusCodeField


class TestStatusCodeCommands(object):

    def test_status_code_field(self):
        message, description = 'Profile Not Found', u'用户不存在'
        PROFILE_NOT_FOUND = StatusCodeField(410000, message, description=description)
        assert PROFILE_NOT_FOUND == 410000
        assert PROFILE_NOT_FOUND.message == message
        assert PROFILE_NOT_FOUND.description == description
