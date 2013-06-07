import os

ONLINE = not os.getenv('VP', 'offline') == 'offline'

THIS_PATH = os.path.abspath(os.path.split(__file__)[0])

if ONLINE:
    IMAGE = os.path.join(THIS_PATH, 'upload', 'img')
    PASTE = os.path.join(THIS_PATH, 'upload', '')
else:
    IMAGE = '/tmp/upload/image'
    PASTE = '/tmp/upload/paste'

if not os.path.exists(IMAGE):
    os.makedirs(IMAGE)

if not os.path.exists(PASTE):
    os.makedirs(PASTE)

if os.path.exists(os.path.join(THIS_PATH, 'entropy')):
    with open(os.path.join(THIS_PATH, 'entropy')) as f:
        ENTROPY = f.read()
else:
    ENTROPY = 'thisismyentropy!42'


MAX_CONTENT_LENGTH = 8 * 1024 * 1024 

DB_PATH = os.path.join(THIS_PATH, 'vp.sqlite')
DATABASE_URI = 'sqlite:///' + DB_PATH