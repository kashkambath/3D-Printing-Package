import numpy as np

xValues = [];     
yValues = [];
zValues = [];

firstxBound = 1;       ### starting x Bound 
finalxBound = 10;      ### starting y Bound
deltaX = (finalBound - firstBound) * .01 ###steps for the x-values 

for (x=firstxBound; x<finalxBound; x+=deltaX) {
	for i in range(1,40) {
		yValue = xValue**2 * np.cos(np.pi*x/18);
		zValue = xValue**2 * np.sin(np.pi*x/18);
		yValues.append(yValue);
		zValues.append(zValues);
	}
}



