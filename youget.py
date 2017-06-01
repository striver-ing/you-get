#!/usr/bin/env python3
import os, sys

_srcdir = '%s/src/' % os.path.dirname(os.path.realpath(__file__))
_filepath = os.path.dirname(sys.argv[0])
sys.path.insert(1, os.path.join(_filepath, _srcdir))
print(os.path.join(_filepath, _srcdir))

# if sys.version_info[0] == 3:
#     import you_get
#     if __name__ == '__main__':
#         you_get.main(video_url = 'http://tv.sohu.com/20170522/n493980844.shtml')
# else: # Python 2
#     from you_get.util import log
#     log.e("[fatal] Python 3 is required!")
#     log.wtf("try to run this script using 'python3 you-get'.")

import you_get
urls = you_get.main(video_url = 'http://tv.sohu.com/20170522/n493980844.shtml')
print(urls)