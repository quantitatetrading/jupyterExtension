import os
import notebook

location = os.path.dirname(os.path.realpath(__file__))
notebookPath = os.path.dirname(notebook.__file__)
os.popen('cp %s/custom.css %s/static/custom/custom.css' % (location, notebookPath))
