import sys
import time
from collections import deque
fancy_loading = deque('>--------------------')
while True:
    print('\r%s' % ''.join(fancy_loading),end = '')
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)