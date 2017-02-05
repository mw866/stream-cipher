#!/usr/bin/python 

from AESCtr import AESCtr
import pytest
import base64
import os

def test_basic():
  key = base64.urlsafe_b64encode(os.urandom(16))

  aes = AESCtr(key)
  txt = b'A great Secret message'*12  # To make it larger than 128-bit
  print 'txt: ', len(txt), type(txt), txt

  ctx = aes.encrypt(txt)
  print 'ctx (nonce, ctx): ', len(ctx[1]), type(ctx[1]), ctx[1]

  dtxt = aes.decrypt(ctx)
  print 'dtxt: ', len(dtxt), type(dtxt), dtxt

  assert dtxt==txt, "The decrypted text is not the same as the original text"

# TODO: Fill in more tests of AESCtr