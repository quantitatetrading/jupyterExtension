import os
import notebook

os.popen('cp custom.css', os.path.join(os.path.dirname(notebook.__file__), 'static/custom/custom.css'))
