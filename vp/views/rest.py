from flask import Blueprint, request, abort, url_for, send_from_directory, Response
import codecs
import os.path
import imghdr


from pygments import highlight
from pygments.formatters import HtmlFormatter

from vp.views.util import make_random_name, is_valid_filename, get_best_lexer, PseudoFile
from vp.db import db_session
from vp.db.models import Paste, Image
from vp import app

mod = Blueprint('rest', __name__)

@mod.route('/', methods=['PUT', 'POST'])
@mod.route('/put', methods=['PUT', 'POST'])
def put():
    fobj = request.files.get('file')
    data = request.form.get('data')
    more_data = request.data;

    if not fobj and not data and not more_data:
        return abort(400)

    fobj = PseudoFile(fobj, data if data else more_data)  
    if not imghdr.what(fobj) is None:
        return put_file(fobj, 'IMAGE')
    return put_file(fobj, 'PASTE')
    

def put_file(fobj, uptype):
    name = make_random_name(app.config[uptype]) 
    path = os.path.join(app.config[uptype], name)
    
    fobj.save(path)
    
    db = None
    if uptype == 'IMAGE':
        ext = ''
        if fobj.has_filename:
            _, ext = os.path.splitext(fobj.filename)
        db = Image(name=name, ext=ext)
    else:
        db = Paste(name=name)
    db_session.add(db)
    
    url = url_for('.show_{}'.format(uptype.lower()), name=name, _external=True)
    if fobj.has_filename and uptype.lower() == 'paste':
        url = '{}?{}'.format(url, fobj.filename.lstrip('.'))
    
    return url, 201


@mod.route('/<name>', methods=['GET'])
def show_paste(name):
    if not is_valid_filename(name):
        return abort(404)
    
    syntax = False
    keys = request.args.keys()
    if keys:
        syntax = keys[0]
        syntax = syntax.replace('.volt', '.d').replace('.v', '.d')
        syntax = 'd' if syntax == 'v' else syntax
    
    path = os.path.join(app.config['PASTE'], name)
    if not os.path.exists(path):
        return abort(404)
    
    with codecs.open(path, 'r', 'utf-8') as f:
        if syntax:
            lexer = get_best_lexer('x.' + syntax, syntax)
            formatter = HtmlFormatter(encoding=None, linenos=True)
            formatter.full = True
        
            return highlight(f.read(), lexer, formatter)
    
        return Response(f.read(), mimetype='text/plain')


@mod.route('/img/<name>', methods=['GET'])
def show_image(name):
    if not is_valid_filename(name):
        return abort(404)

    path = os.path.join(app.config['IMAGE'], name)
    if not os.path.exists(path):
        return abort(404)
    
    #ext = db_session.query(Image).filter_by(name=name).one().ext.lstrip('.')
    ext = imghdr.what(path)
    return send_from_directory(app.config['IMAGE'], name, mimetype='image/{}'.format(ext))
    

