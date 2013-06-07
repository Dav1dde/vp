from flask import render_template, request, redirect

from vp import app
from vp.views.rest import put_file
from vp.views.util import PseudoFile, get_lexer_name_from_code


@app.route('/', methods=['GET'])
def index():
    return render_template('paste.html')

@app.route('/', methods=['POST'])
def index_post():
    code = request.form.get('code', '')
    
    if len(code.strip()) == 0:
        return render_template('paste.html', error='No code submitted')
    
    url, _ = put_file(PseudoFile(None, code), 'PASTE')
    
    h = get_lexer_name_from_code(code)
    if h:
        url = '{}?{}'.format(url, h)
    
    return redirect(url)