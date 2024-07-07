from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize



setup(
    name='Quantise',
    ext_modules=cythonize([
        Extension(
            "Quantise_Cython",
            sources=["cython_qfunc.pyx"]

        ),
    ])
)

