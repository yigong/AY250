from CalCalc import calculate
def test_3():
	assert abs(6.-calculate('1+2+3'))<0.001