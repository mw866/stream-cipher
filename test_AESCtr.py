#!/usr/bin/python 
# -*- coding: utf-8 -*-
from AESCtr import AESCtr
import pytest
import base64
import os

def test_basic():
  key = base64.urlsafe_b64encode(os.urandom(16))
  aes = AESCtr(key)
  txt = b'A great Secret message'*12  # To make it larger than 128-bit
  # print 'txt: ', len(txt), type(txt), txt
  ctx = aes.encrypt(txt)
  # print 'ctx (nonce, ctx): ', len(ctx[1]), type(ctx[1]), ctx[1]
  dtxt = aes.decrypt(ctx)
  # print 'dtxt: ', len(dtxt), type(dtxt), dtxt
  assert dtxt==txt, "The decrypted text is not the same as the original text"

# TODO: Fill in more tests of AESCtr


def test_ascii_varied_length():
  import random, string
  key = base64.urlsafe_b64encode(os.urandom(16))
  aes = AESCtr(key)
  for length in xrange(0xff):
    txt = bytes(''.join([random.choice(string.ascii_letters) for i in xrange(length)]))
    ctx = aes.encrypt(txt)
    dtxt = aes.decrypt(ctx)
    assert dtxt==txt, "Length Test Failed at length = " + str(length)+"."

def test_utf8():
  key = base64.urlsafe_b64encode(os.urandom(16))
  aes = AESCtr(key)
  txt = b'café'
  ctx = aes.encrypt(txt)
  dtxt = aes.decrypt(ctx)
  assert dtxt==txt, "UTF-8 Test Failed. It is expected because ASECtr accepts byte/ASCII (0-255), whereas UTF-8 has variable length."