# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))