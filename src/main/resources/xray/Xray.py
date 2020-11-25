#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import json, time
from xlrelease.HttpRequest import HttpRequest
from xlrelease.CredentialsFallback import CredentialsFallback
from org.apache.http.client import ClientProtocolException
from com.xebialabs.overthere import CmdLine
from com.xebialabs.overthere.util import (
    CapturingOverthereExecutionOutputHandler,
    OverthereUtils,
)
from com.xebialabs.overthere.local import LocalConnection
from com.xebialabs.overthere.OperatingSystemFamily import UNIX
from java.lang import String
import org.slf4j.Logger as Logger
import org.slf4j.LoggerFactory as LoggerFactory


class XrayClient(object):
    def __init__(self, server):
        self.logger = LoggerFactory.getLogger("com.xebialabs.xray-plugin")
        if server in [None, ""]:
            raise Exception("Server is undefined.")
                
        self.http_request = HttpRequest(server)