# CS 5830 HW1

## Instructions
* Activate virtualenv:


        source my-venv/bin/activate

* Deactivate virtualenv:


        deactivate

* Run test_AESCtr


        py.test -s test_AESCtr.py

## Reference:

* Python cryptography: https://cryptography.io/en/latest/

* Python virtualenv: https://virtualenv.pypa.io/en/latest/userguide/
* 
* XOR on bytes: http://stackoverflow.com/questions/29408173/byte-operations-xor-in-python

## Troubleshooting:
* Error installing Python cryptography library:


        sudo apt-get install build-essential libssl-dev libffi-dev python-dev

* pytest does not shaw stdout if test passed: add -s argument

