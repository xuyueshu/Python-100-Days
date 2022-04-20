# Python sys模块介绍



Python的sys模块提供访问解释器使用或维护的变量，和与解释器进行交互的函数。通俗来讲，sys模块负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python运行时的环境。

（1）sys.argv   获取当前正在执行的命令行参数的参数列表（list）

​	sys.argv[]是一个程序获取外部参数的桥梁。sys.argv[0]表示代码本身的文件路径，所以参数从1开始

```python
import sys
print(sys.argv[0])
print("---------------------------------------------")
for i in sys.argv:
	print(i)
```
输出：

```
C:/Users/dell/Desktop/OSVOS_learning/my_code/test1.py
C:/Users/dell/Desktop/OSVOS_learning/my_code/test1.py
Process finished with exit code 0
```


更复杂一点，创建test.py：

```PYTHON
import sys    
def readfile(filename):  #定义readfile函数，从文件中读出文件内容    
    '''''''Print a file to the standard output.'''    
    f = file(filename)    
    while True:    
        line = f.readline()    
        if len(line) == 0:    
            break    
        print line, # notice comma  分别输出每行内容    
    f.close()    
# Script starts from here  
print sys.argv  
if len(sys.argv) < 2:    
    print 'No action specified.'    
    sys.exit()    
if sys.argv[1].startswith('--'):    
    option = sys.argv[1][2:]    
    # fetch sys.argv[1] but without the first two characters    
    if option == 'version':  #当命令行参数为-- version，显示版本号    
        print 'Version 1.2'    
    elif option == 'help':  #当命令行参数为--help时，显示相关帮助内容    
        print '''
This program prints files to the standard output.  
Any number of files can be specified.  
Options include:  
  --version : Prints the version number  
  --help    : Display this help'''    
    else:    
        print 'Unknown option.'    
    sys.exit()    
else:    
    for filename in sys.argv[1:]: #当参数为文件名时，传入readfile，读出其内容    
        readfile(filename) 
```
​	在test.py文件下创建test.txt, test1.txt, test2.txt文件并在里面分别添加如下内容：

test.txt :   hello python!

test1.txt:  hello world!

test2.txt:  hello my friends!

 Good luck！

然后在终端里执行如下内容：

```python
C:\Users\dell\Desktop\my_code>python test.py
['test.py']
No action specified
```

```python
C:\Users\dell\Desktop\my_code>python test.py --version
['test.py', '--version']
Version 1.2
```

```python
C:\Users\dell\Desktop\my_code>python test.py --help
['test.py', '--help']
This program prints files to the standard output.
                 Any number of files can be specified.
                 Options include:
                 --version : Prints the version number
                 --help    : Display this help
```

```python
C:\Users\dell\Desktop\my_code>python test.py test.txt
['test.py', 'test.txt']
hello python!
```

**(2) sys.modules.keys()   返回所有已经导入的模块列表**

```python
>>>import os
>>>import sys
>>>import numpy
>>>sys.modules.keys()
dict_keys(['builtins', 'sys', '_frozen_importlib', '_imp', '_warnings', '_thread', '_weakref', '_frozen_importlib_external', '_io', 'marshal', 'nt', 'winreg', 'zipimport', 'encodings', 'codecs', '_codecs', 'encodings.aliases', 'encodings.utf_8', '_signal', '__main__', 'encodings.latin_1', 'io', 'abc', '_weakrefset', 'site', 'os', 'errno', 'stat', '_stat', 'ntpath', 'genericpath', 'os.path', '_collections_abc', '_sitebuiltins', 'sysconfig', '_bootlocale', '_locale', 'encodings.gbk', '_codecs_cn', '_multibytecodec', 'types', 'functools', '_functools', 'collections', 'operator', '_operator', 'keyword', 'heapq', '_heapq', 'itertools', 'reprlib', '_collections', 'weakref', 'collections.abc', 'importlib', 'importlib._bootstrap', 'importlib._bootstrap_external', 'warnings', 'importlib.util', 'importlib.abc', 'importlib.machinery', 'contextlib', 'mpl_toolkits', '_pydev_imps', '_pydev_imps._pydev_saved_modules', 'threading', 'time', 'traceback', 'linecache', 'tokenize', 're', 'enum', 'sre_compile', '_sre', 'sre_parse', 'sre_constants', 'copyreg', 'token', 'socket', '_socket', 'selectors', 'math', 'select', 'queue', 'xmlrpc', 'xmlrpc.client', 'base64', 'struct', '_struct', 'binascii', 'datetime', '_datetime', 'decimal', 'numbers', '_decimal', 'http', 'http.client', 'email', 'email.parser', 'email.feedparser', 'email.errors', 'email._policybase', 'email.header', 'email.quoprimime', 'string', '_string', 'email.base64mime', 'email.charset', 'email.encoders', 'quopri', 'email.utils', 'random', 'hashlib', '_hashlib', '_blake2', '_sha3', 'bisect', '_bisect', '_random', 'urllib', 'urllib.parse', 'email._parseaddr', 'calendar', 'locale', 'email.message', 'uu', 'email._encoded_words', 'email.iterators', 'ssl', 'ipaddress', 'textwrap', '_ssl', 'xml', 'xml.parsers', 'xml.parsers.expat', 'pyexpat.errors', 'pyexpat.model', 'pyexpat', 'xml.parsers.expat.model', 'xml.parsers.expat.errors', 'gzip', 'zlib', '_compression', 'xmlrpc.server', 'http.server', 'html', 'html.entities', 'mimetypes', 'posixpath', 'shutil', 'fnmatch', 'bz2', '_bz2', 'lzma', '_lzma', 'socketserver', 'copy', 'argparse', 'gettext', 'pydoc', 'inspect', 'ast', '_ast', 'dis', 'opcode', '_opcode', 'pkgutil', 'platform', 'subprocess', 'signal', 'msvcrt', '_winapi', 'code', 'codeop', '__future__', '_pydevd_bundle', '_pydevd_bundle.pydevd_constants', '_pydevd_bundle.pydevd_vm_type', '_pydev_bundle', '_pydev_bundle.fix_getpass', 'getpass', '_pydevd_bundle.pydevd_vars', 'pickle', '_compat_pickle', '_pickle', '_pydevd_bundle.pydevd_custom_frames', 'pydevd_file_utils', '_pydev_bundle._pydev_filesystem_encoding', 'json', 'json.decoder', 'json.scanner', '_json', 'json.encoder', 'ctypes', '_ctypes', 'ctypes._endian', '_pydevd_bundle.pydevd_xml', '_pydev_bundle.pydev_log', '_pydevd_bundle.pydevd_extension_utils', 'pydevd_plugins', 'pkg_resources', 'zipfile', 'plistlib', 'tempfile', 'pkg_resources.extern', 'pkg_resources._vendor', 'pkg_resources.extern.six', 'pkg_resources._vendor.six', 'pkg_resources.extern.six.moves', 'pkg_resources._vendor.six.moves', 'pkg_resources.extern.appdirs', 'pkg_resources._vendor.packaging.__about__', 'pkg_resources.extern.packaging', 'pkg_resources.extern.packaging.version', 'pkg_resources.extern.packaging._structures', 'pkg_resources.extern.packaging.specifiers', 'pkg_resources.extern.packaging._compat', 'pkg_resources.extern.packaging.requirements', 'pprint', 'pkg_resources.extern.pyparsing', 'pkg_resources.extern.six.moves.urllib', 'pkg_resources.extern.packaging.markers', 'pydevd_plugins.extensions', '_pydevd_bundle.pydevd_resolver', '_pydev_bundle.pydev_imports', '_pydev_imps._pydev_execfile', '_pydevd_bundle.pydevd_exec2', '_pydevd_bundle.pydevd_extension_api', 'xml.sax', 'xml.sax.xmlreader', 'xml.sax.handler', 'xml.sax._exceptions', 'xml.sax.saxutils', 'urllib.request', 'urllib.error', 'urllib.response', 'nturl2path', '_pydevd_bundle.pydevd_save_locals', '_pydevd_bundle.pydevd_utils', '_pydev_bundle.pydev_console_utils', '_pydev_bundle._pydev_calltip_util', '_pydev_bundle._pydev_imports_tipper', '_pydev_bundle._pydev_tipper_common', '_pydev_bundle.pydev_umd', 'pydevconsole', '_pydev_bundle.pydev_localhost', 'encodings.idna', 'stringprep', 'unicodedata', 'pydev_ipython', 'pydev_ipython.matplotlibtools', 'pydev_ipython.inputhook', '_pydev_bundle.pydev_import_hook', '_pydev_bundle.pydev_import_hook.import_hook', 'pydevd_plugins.extensions.types', 'pydevd_plugins.extensions.types.pydevd_plugin_numpy_types', 'pydevd_plugins.extensions.types.pydevd_helpers', 'pydevd_plugins.extensions.types.pydevd_plugins_django_form_str', '_pydevd_bundle.pydevd_comm', '_pydevd_bundle.pydevd_tracing', '_pydev_bundle._pydev_completer', '_pydevd_bundle.pydevd_console', '_pydev_bundle.pydev_override', '_pydevd_bundle.pydevd_io', '_pydev_bundle.pydev_monkey', 'numpy', 'numpy._globals', 'numpy.__config__', 'numpy.version', 'numpy._import_tools', 'numpy.add_newdocs', 'numpy.lib', 'numpy.lib.info', 'numpy.lib.type_check', 'numpy.core', 'numpy.core.info', 'numpy.core.multiarray', 'numpy.core.umath', 'numpy.core._internal', 'numpy.compat', 'numpy.compat._inspect', 'numpy.compat.py3k', 'pathlib', 'numpy.core.numerictypes', 'numpy.core.numeric', 'numpy.core.fromnumeric', 'numpy.core._methods', 'numpy.core.arrayprint', 'numpy.core.defchararray', 'numpy.core.records', 'numpy.core.memmap', 'numpy.core.function_base', 'numpy.core.machar', 'numpy.core.getlimits', 'numpy.core.shape_base', 'numpy.core.einsumfunc', 'numpy.testing', 'unittest', 'unittest.result', 'unittest.util', 'unittest.case', 'difflib', 'logging', 'atexit', 'unittest.suite', 'unittest.loader', 'unittest.main', 'unittest.runner', 'unittest.signals', 'numpy.testing.decorators', 'numpy.testing.nose_tools', 'numpy.testing.nose_tools.decorators', 'numpy.testing.nose_tools.utils', 'numpy.lib.utils', 'numpy.testing.nosetester', 'numpy.testing.nose_tools.nosetester', 'numpy.testing.utils', 'numpy.lib.ufunclike', 'numpy.lib.index_tricks', 'numpy.lib.function_base', 'numpy.lib.twodim_base', 'numpy.matrixlib', 'numpy.matrixlib.defmatrix', 'numpy.lib.stride_tricks', 'numpy.lib.mixins', 'numpy.lib.nanfunctions', 'numpy.lib.shape_base', 'numpy.lib.scimath', 'numpy.lib.polynomial', 'numpy.linalg', 'numpy.linalg.info', 'numpy.linalg.linalg', 'numpy.linalg.lapack_lite', 'numpy.linalg._umath_linalg', 'numpy.lib.arraysetops', 'numpy.lib.npyio', 'numpy.lib.format', 'numpy.lib._datasource', 'numpy.lib._iotools', 'numpy.lib.financial', 'numpy.lib.arrayterator', 'numpy.lib.arraypad', 'numpy.lib._version', 'numpy._distributor_init', 'numpy.fft', 'numpy.fft.info', 'numpy.fft.fftpack', 'numpy.fft.fftpack_lite', 'numpy.fft.helper', 'numpy.polynomial', 'numpy.polynomial.polynomial', 'numpy.polynomial.polyutils', 'numpy.polynomial._polybase', 'numpy.polynomial.chebyshev', 'numpy.polynomial.legendre', 'numpy.polynomial.hermite', 'numpy.polynomial.hermite_e', 'numpy.polynomial.laguerre', 'numpy.random', 'numpy.random.info', 'cython_runtime', 'mtrand', 'numpy.random.mtrand', 'numpy.ctypeslib', 'numpy.ma', 'numpy.ma.core', 'numpy.ma.extras'])
```

**(3)sys.platform     获取当前执行环境的平台**

```python
# linux 
>>> import sys
>>> sys.platform
'linux2'
 
# windows
>>> import sys
>>> sys.platform
'win32'
```

**（4）sys.path  **

​     path是一个目录列表，供Python从中查找第三方扩展模块。

```python
>>>sys.path
['D:\\Engineering software\\PyCharm Community Edition 2018.1.2\\helpers\\pydev', 'D:\\Engineering software\\PyCharm Community Edition 2018.1.2\\helpers\\pydev', 'C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip', 'C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36\\DLLs', 'C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36\\lib', 'C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36', 'C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages', 'C:\\Users\\dell\\Desktop\\OSVOS_learning\\my_code', 'C:/Users/dell/Desktop/OSVOS_learning/my_code']
```

**(5) sys.exit(n) **

 调用sys,exit(n)可以中途退出程序sys.exit(0)表示正常退出，n不为0时，会引发SystemExit异常，从而在主程序中可以捕获该异常。

```python
import sys
print("running ...")
try:
    sys.exit(1)
except SystemExit:
    print("SystemExit exit 1")
 
print("exited")
```

执行：

```python
running ...
SystemExit exit 1
exited
 
Process finished with exit code 0
```

**（6）sys.version    获取python解释程序的版本信息**

```python
>>>sys.version
'3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)]'
```

**(7) sys.stdin, sys.stdout, sys.stderr    标准输入，标准输出，错误输出**

标准输入：一般为键盘输入，stdin对象为解释器提供输入字符流，一般使用raw_input()和input()函数

```python
import sys
 
print("Please input you name:")
name = sys.stdin.readline()
print(name)
```

执行：

```python
Please input you name:
Xiao Ming            #用户输入，然后Enter
Xiao Ming
 
 
Process finished with exit code 0
```

标准输出：一般为屏幕。stdout对象接收到print语句产生的输出

```python
import sys
 
sys.stdout.write("123456\n")
sys.stdout.flush()
```

执行：

```python
123456
 
Process finished with exit code 0
```

错误输出：一般是错误信息，stderr对象接收出错的信息。

例如：引发一个异常

```python
>>>raise Exception("raise...")
Traceback (most recent call last):
  File "<input>", line 1, in <module>
Exception: raise...
```

sys.stdout与print

当我们在 Python 中打印对象调用 print obj 时候，事实上是调用了 sys.stdout.write(obj+'\n') ；print 将你需要的内容打印到了控制台，然后追加了一个换行符；print 会调用 sys.stdout 的 write 方法

```python
1 sys.stdout.write('hello'+'\n') 
2 
3 print 'hello'
```

sys.stdin与raw_input

当我们用 raw_input('Input promption: ') 时，事实上是先把提示信息输出，然后捕获输入

以下两组在事实上等价：

```python
1 hi=raw_input('hello? ') 
2 
3 print 'hello? ', #comma to stay in the same line 
4 
5 hi=sys.stdin.readline()[:-1] # -1 to discard the '\n' in input stream
```

从控制台重定向到文件：

  原始的sys.stdout指向控制台。如果把文件的对象引用赋给sys.stdout，那么print调用的就是文件对象的write方法

```python
import sys
 
f_handler = open('out.log','w')
sys.stdout = f_handler
print("hello")
# this hello can't be viewed on console
# this hello is in file out.log
```

如果想要在控制台打印一些东西的话，最好先将原始的控制台对象引用保存下来，向文件中打印后再恢复sys.stdout:

```python
1 __console__=sys.stdout 
2 
3 # redirection start # 
4 
5 ... 
6 
7 # redirection end 
8 
9 sys.stdout=__console__
```

