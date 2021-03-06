#!/router/bin/python

import sys
import os

_ext_libs = [ {'name': 'simple_enum'},
              {'name': 'pyyaml-3.11', 'py-dep': True},
              {'name': 'pyzmq-ctypes'},
              {'name': 'jsonrpclib-pelix-0.4.1'},
              {'name': 'termstyle'},
              {'name': 'netstat'},
              {'name': 'jsonpickle-2.0.0'}
            ]

def _import_server_modules():

    march = os.uname()[4]

    if march == 'aarch64':
        cpu_vendor = 'arm'
    elif march == 'x86_64' or march == 'i386' or march == 'i686':
        cpu_vendor = 'intel'
    elif march == 'ppc64le':
        cpu_vendor = 'ppc'
    else:
        raise Exception('Unknown CPU architecture: ' + march)

    cpu_bits   = '64bit' if sys.maxsize > 0xffffffff else '32bit'
    python_ver = 'python%s' % sys.version_info.major

    cur = cur = os.path.dirname(__file__)
    par = os.pardir
    parent_path = os.path.abspath(os.path.join(cur, par))
    if parent_path not in sys.path:
        sys.path.insert(1, parent_path)
    interactive_path = os.path.join(parent_path, 'interactive')
    if interactive_path not in sys.path:
        sys.path.insert(1, interactive_path)

    if os.getenv('TREX_EXT_LIBS'):
        ext_libs_path = os.environ['TREX_EXT_LIBS']
    else:
        ext_libs_path = os.path.abspath(os.path.join(cur, par, par, par, 'external_libs'))

    if not os.path.isdir(ext_libs_path):
        raise Exception('Could not determine path of external_libs, try setting TREX_EXT_LIBS variable')

    for p in _ext_libs:
        special = []
        if p.get('py-dep'):
            special.append(python_ver)
        if p.get('arch-dep'):
            special.append(cpu_vendor)
            special.append(cpu_bits)
        full_path = os.path.join(ext_libs_path, p['name'], *special)

        if not os.path.exists(full_path):
            err_msg  =  "\n\nUnable to find required external library: '{0}'\n".format(p['name'])
            err_msg +=  "Current path used: '{0}'".format(full_path)

            raise Exception(err_msg)

        if full_path not in sys.path:
            sys.path.insert(1, full_path)


_import_server_modules()

