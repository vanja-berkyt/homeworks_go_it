from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1.0.2',
      description='my first package',
      author='Ivan Drago',
      author_email='i.dragomeretskyy@dmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean:clean_func']},
      classifier=["Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent"]
)