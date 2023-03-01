P=[]
import time
import matplotlib.pyplot as plt
alpha = dict()
alpha["A"] = dict()
alpha["C"] = dict()
alpha["T"] = dict()
alpha["G"] = dict()
alpha["A"]["A"] = 0
alpha["A"]["C"] = 110
alpha["A"]["G"] = 48 
alpha["A"]["T"] = 94

alpha["C"]["A"] = 110
alpha["C"]["C"] = 0
alpha["C"]["G"] = 118 
alpha["C"]["T"] = 48

alpha["G"]["A"] = 48
alpha["G"]["C"] = 118
alpha["G"]["G"] = 0 
alpha["G"]["T"] = 110

alpha["T"]["A"] = 94
alpha["T"]["C"] = 48
alpha["T"]["G"] = 110 
alpha["T"]["T"] = 0
delta=30

def generate_actual_string(parameter_string, op):
	r=parameter_string
	p=r
	for i in op:
		r=r[0:i+1]+p+r[i+1:]
		p=r
	return r


def Space_Efficient_Alignment(X ,Y):

	B=[[0 for c in range(2)] for r in range(m+1)]

	for i in range(m+1):
		B[i][0]=delta * i

	for j in range(1,n+1):
		B[0][1]=delta*j

		for i in range(1,m+1):
			B[i][1]= min[alpha[X[i]][Y[j]] + B[i − 1][0], delta+B[i−1][1], delta+B[i][0]]
		
		for i in range(1,m+1):
			B[i][0]= B[i][1]


def Backward_Space_Efficient_Alignment(X,Y):


def divide_and_conquer(X, Y):
	m=len(X)
	n=len(Y)
	if m<=2 or n<=2:
		Alignment(X,Y)
	else:
		Space_Efficient_Alignment(X,Y[1:n//2])
		Backward_Space_Efficient_Alignment(X,Y[n//2+1:n])



		divide_and_conquer(X[1:q], Y[1:n//2])
		divide_and_conquer(X[q+1:n],Y[n//2+1 : n])

