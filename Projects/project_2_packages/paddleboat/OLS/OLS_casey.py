import numpy as np
import pandas as pd


def deg_freedom(dependent_variable_data)
	if isinstance(dependent_variable_data, np.array):
		dimensions = np.shape(dependent_variable_data)
		deg_freedom = dimension[0] - dimensions[1]

	return deg_freedom
		
        

