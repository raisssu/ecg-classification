# Source - https://stackoverflow.com/a/63162156
# Posted by David Kim, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-13, License - CC BY-SA 4.0
import numpy as np

INDENT = 2
SPACE = " "
NEWLINE = "\n"

# Changed basestring to str, and dict uses items() instead of iteritems().
def to_json(o, level=0):
  ret = ""
  if isinstance(o, dict):
    ret += "{" + NEWLINE
    comma = ""
    for k, v in o.items():
      ret += comma
      comma = ",\n"
      ret += SPACE * INDENT * (level + 1)
      ret += '"' + str(k) + '":' + SPACE
      ret += to_json(v, level + 1)

    ret += NEWLINE + SPACE * INDENT * level + "}"
  elif isinstance(o, str):
    ret += '"' + o + '"'
  elif isinstance(o, list):
    ret += "[" + ",".join([to_json(e, level + 1) for e in o]) + "]"
  # Tuples are interpreted as lists
  elif isinstance(o, tuple):
    ret += "[" + ",".join(to_json(e, level + 1) for e in o) + "]"
  elif isinstance(o, bool):
    ret += "true" if o else "false"
  elif isinstance(o, int):
    ret += str(o)
  elif isinstance(o, float):
    ret += '%.7g' % o
  elif isinstance(o, np.ndarray) and np.issubdtype(o.dtype, np.integer):
    ret += "[" + ','.join(map(str, o.flatten().tolist())) + "]"
  elif isinstance(o, np.ndarray) and np.issubdtype(o.dtype, np.inexact):
    ret += "[" + ','.join(map(lambda x: '%.7g' % x, o.flatten().tolist())) + "]"
  elif o is None:
    ret += 'null'
  else:
    raise TypeError("Unknown type '%s' for json serialization" % str(type(o)))
  return ret
