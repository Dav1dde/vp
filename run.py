from vp import app

import sys
sys.stdout = sys.stderr

app.run(debug=True)