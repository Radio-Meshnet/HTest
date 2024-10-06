from pythonforandroid.recipe import RustCompiledComponentsRecipe

class IOPPythonRecipe(RustCompiledComponentsRecipe):
    name = 'iop-python'
    version = '0.2.0'
    url = 'https://files.pythonhosted.org/packages/9d/7c/e405bd67f5317fdb046ae496f8c2faa7ac75c41c06fe5027ef8d33c07bb9/iop_python-{version}.tar.gz'
    depends = []
    
recipe = IOPPythonRecipe()
