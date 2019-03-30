import os
import notebook
import site

location = os.path.dirname(os.path.realpath(__file__))
packageDir = site.getsitepackages()[0]
notebookPath = os.path.join(packageDir, 'notebook')

os.popen('cp %s/custom.css %s/static/custom/custom.css' % (location, notebookPath))
os.system('jupyter nbextension enable jupyterExtension/main')
os.system('git clone https://github.com/quantitatetrading/trader %s/trader' % packageDir)
