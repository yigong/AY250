from CalCalc import calculate
def test_1():
	assert abs(4.-calculate('2**2'))<0.001