# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))