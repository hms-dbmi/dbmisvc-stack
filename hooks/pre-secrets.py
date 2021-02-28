#!/usr/bin/env python3
# coding: utf-8

import os

from dbmisvc_stack.app import Stack

import logging

logger = logging.getLogger("stack")

# Get the secrets file
path = os.path.join(Stack.get_stack_root(), ".env")
