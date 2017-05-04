
#filename: readbin.py

import argparse


def readbin(binaryfile = None):
	'''
	The functtion for read binary file to send to display
	'''
	
	bytea = bytearray(binaryfile.read())
	
	dict = {}
	key = 0
	value = 0
	for data in bytea:
		value |= (data << 8 * (key % 4))
		key += 1
		if (key % 4) == 0:
			dict[(key - 1) >> 2] = value
			value = 0
	
	print 'HexAdd:               HexData:'
	for key in dict:
		print '{:08X}+(3,2,1,0) -> {:08X}'.format(key << 2, dict[key])

if __name__ == "__main__":
	ap = argparse.ArgumentParser(description='Read binary file utility.')
	ap.add_argument('binfile', type=argparse.FileType('rb'), help='binary file to read')
	args = ap.parse_args()
	
	readbin(args.binfile)
	