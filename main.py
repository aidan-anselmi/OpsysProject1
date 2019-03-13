import random
import argparse

import SJF
import SRT
import FCFS
import RR

# random number generator 
class Rand48(object):
    def __init__(self, seed):
        self.n = seed
    def seed(self, seed):
        self.n = seed
    def srand(self, seed):
        self.n = (seed << 16) + 0x330e
    def next(self):
        self.n = (25214903917 * self.n + 11) & (2**48 - 1)
        return self.n
    def drand(self):
        return self.next() / 2**48
    def lrand(self):
        return self.next() >> 17
    def mrand(self):
        n = self.next() >> 16
        if n & (1 << 31):
            n -= 1 << 32
        return n   


def runAlgs():
	SJF.SJF()
	SRT.SRT()
	FCFS.FCFS()
	RR.RR()

	return 1;



if __name__ == '__main__':

	#set stuff up
	parser = argparse.ArgumentParser()
	parser.add_argument("cpuArriveTime")
	parser.add_argument("lambdaC")
	parser.add_argument("upperBound")
	parser.add_argument("numProcesses")
	parser.add_argument("contextSwitchTime")
	parser.add_argument("alpha")
	parser.add_argument("timeSlice")
	parser.add_argument("cpuArriveTime")
	parser.add_argument("addToEnd")
	args = parser.parse_args()

	cpuArriveTime = args.cpuArriveTime
	lambdaC = args.lambdaC
	upperBound = args.upperBound
	numProcesses = args.numProcesses
	contextSwitchTime = args.contextSwitchTime
	alpha = args.alpha
	timeSlice = args.timeSlice
	cpuArriveTime = args.cpuArriveTime
	addToEnd = args.addToEnd

	# #example using the random number generator
	# r = Rand48(0)
	# r.srand(12345)
	# print(r.drand())
	# print(r.drand())

	#runAlgs()