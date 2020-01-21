import sys
import os
import inspect

# Add path of src files.
currentdir = os.path.dirname(
				os.path.abspath(
					inspect.getfile(
						inspect.currentframe()
						)
					)
				)

parentdir = os.path.dirname(currentdir)
parentdir += "/src"
sys.path.insert(0,parentdir) 
