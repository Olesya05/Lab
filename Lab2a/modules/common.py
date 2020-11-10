import datetime
import sys
import math
from math import sqrt


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def func(ar):
	if ar == True:
		for i in range (100):
			if i%2==0:
				print(i, end=' ')
	elif ar == False:
		for i in range (100):
			if i%2==1:
				print(i, end=' ')

def log_func():
    chyslo = input(" Please enter number : ")
    res = sqrt(int(chyslo))
    print(res)

