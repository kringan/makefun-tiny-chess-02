# Pack a chess engine source into a <=4096-byte main.py (LZMA + base85).
# Usage: python3 pack.py <engine_source.py> <output_main.py>
import sys, lzma, base64
src = open(sys.argv[1], 'rb').read()
comp = lzma.compress(src, preset=9, format=lzma.FORMAT_ALONE)
b85 = base64.b85encode(comp).decode()
out = "import lzma as z,base64 as b\n# LZMA packed chess engine\nP='" + b85 + "'\nexec(z.decompress(b.b85decode(P)))\n"
open(sys.argv[2], 'w').write(out)
print(f"source {len(src)} -> packed {len(out)} bytes")
assert len(out) <= 4096, "packed file too big"
