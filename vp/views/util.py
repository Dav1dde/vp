import random
import string
import os
import io

from pygments.lexers import (get_lexer_by_name,
                             get_lexer_for_filename,
                             #get_lexer_for_mimetype,
                             TextLexer)
from pygments.util import ClassNotFound


IMG_EXTENSIONS = set(['.png', '.jpg', '.jpeg', '.gif', '.bmp'])
ALLOWED_CHARS = string.ascii_letters + string.digits

def is_image(filename):
    _, ext = os.path.splitext(filename)
    return ext in IMG_EXTENSIONS


def make_random_name(basepath, alphabet=ALLOWED_CHARS):
    name = ''.join(random.sample(alphabet, random.randint(3,5)))
    while os.path.exists(os.path.join(basepath, name)):
        name = ''.join(random.sample(alphabet, random.randint(3,5)))
    
    return name

def is_valid_filename(name, alphabet=ALLOWED_CHARS):
    return all(c in alphabet for c in name)


def get_best_lexer(filename, syntax=None):
    for func, data in [(get_lexer_by_name, syntax),
                       (get_lexer_for_filename, filename)]:
        try:
            return func(data, encoding=None)
        except ClassNotFound:
            pass
    return TextLexer(encoding=None)


class PseudoFile(object):
    def __init__(self, fobj, data):
        self.fobj = fobj
        self.has_filename = True
               
        if not fobj:
            if isinstance(data, unicode):
                data = data.encode('utf-8')
            self.fobj = io.BytesIO(data)
            self.fobj.filename = data[:15]
            self.has_filename = False
        
        self.filename = self.fobj.filename
                
    def read(self, *args, **kwargs):
        return self.fobj.read(*args, **kwargs)
    
    def write(self, *args, **kwargs):
        return self.fobj.write(*args, **kwargs)
    
    def tell(self, *args, **kwargs):
        return self.fobj.tell(*args, **kwargs)
    
    def seek(self, *args, **kwargs):
        return self.fobj.seek(*args, **kwargs)
    
    def save(self, path):
        if hasattr(self.fobj, 'save'):
            return self.fobj.save(path)
        
        with open(path, 'wb') as f:
            f.write(self.fobj.read())           
            
        
