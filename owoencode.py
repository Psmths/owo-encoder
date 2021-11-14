import bitarray

def encode(s):
    ba = bitarray.bitarray()
    ba.frombytes(s.encode('utf-8'))
    o = ''
    s = 0
    g = ''
    for b in ba:
      if s == 0:
        g = ('u' if b else 'o')
        s = 1
        continue
      if s == 1:
        o = o + (g.upper() if b else g)
        s = 2
        continue
      if s == 2:
        o = o + ('W' if b else 'w')
        s = 3
        continue
      if s == 3:
        o = o + (g.upper() if b else g)
        s = 0
        continue
    return o
