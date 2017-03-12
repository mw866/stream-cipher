# Stream Cipher 

Implementation of stream cipher using block cipher i.e. AES ECB mode
CS 5830 HW1

## Instructions
* Install and initilize virtualenv:


        pip install virtualenv
        virtualenv --python=python2.7 my-venv
     
* Activate virtualenv:


        source my-venv/bin/activate
        
* Install Python cryptography library


        pip install cryptography
        
* Install Python pytest library
 
 
        pip install pytest

* Deactivate virtualenv:


        deactivate

* Run test_AESCtr and excluding the `my-venv` folder:


        py.test --ignore=my-venv

* Run standard debugger pdb 

        py.test -x --pdb --ignore=my-venv

* RUN GUI debugger [pudb](https://github.com/inducer/pudb) and [pytest-pudb](https://github.com/wronglink/pytest-pudb):

 
        pip install pudb pytest-pudb
        py.test -x --pudb --ignore=my-venv
        
* Run debugger without pytest:


        python -m {pdb|pudb.run} my-script.py


## Reference:

* Python cryptography: https://cryptography.io/en/latest/

* Python virtualenv: https://virtualenv.pypa.io/en/latest/userguide/

* XOR on bytes: http://stackoverflow.com/questions/29408173/byte-operations-xor-in-python

* Python2.7 Unicode: https://fedorahosted.org/releases/k/i/kitchen/docs/unicode-frustrations.html

* Python2.7 String Literal: https://docs.python.org/2.7/reference/lexical_analysis.html#string-literals 

## Troubleshooting

### Error installing Python cryptography library:


        sudo apt-get install build-essential libssl-dev libffi-dev python-dev

### `pytest` does not show stdout if test passed: add -s argument

### `pytest` and `py.test` behave inconsistenly:

`pytest` is from logilab-common instead of Python: http://www.christianlong.com/blog/pytest-vs-pytest.html#the-problem

Solution: `sudo apt-get autoremove python-logilab-common`

