import os
import notebook

location = os.path.dirname(os.path.realpath(__file__))
notebookPath = os.path.dirname(notebook.__file__)
print(location, notebookPath, 'cp %s/custom.css %s/static/custom/custom.css' % (location, notebookPath))
os.popen('cp %s/custom.css %s/static/custom/custom.css' % (location, notebookPath))
os.system('jupyter nbextension enable DisplayData')
