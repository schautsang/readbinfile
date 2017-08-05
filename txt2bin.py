#filename: txt2bin.py

import argparse
from array import array


def asbytes(s):
	if isinstance(s, bytes):
		return s
	return s.encode('latin1')


def txt2bin(txtfile = None):

	'''
	The functtion for read .txt file to send to display and save as .bin
	'''

	filename = '{}'.format(args.outfile)
	fp = open(filename, 'wb')
	bin = array('B')

	while True:
		line = txtfile.readline()
		if (len(line) == 0):
			break

		integer = int(line[0:8], 16)
		
		bin.append(integer & 0x0FF)
		bin.append(integer >> 8  & 0x0FF)
		bin.append(integer >> 16 & 0x0FF)
		bin.append(integer >> 24 & 0x0FF)
	
	fp.write(asbytes(bin.tostring()))

	txtfile.close()
	fp.close()

	print 'covert completed...'


if __name__ == "__main__":

	'''
	The functtion for read txt file to converse bin file
	
	example: txt2bin.py -o output.bin input.txt
	
	'''
	
	ap = argparse.ArgumentParser(description='Read txt file utility.')
	ap.add_argument('txtfile', type=argparse.FileType('rb'), help='txt file to read')
	ap.add_argument('-o', '--outfile', help='bin file to write')
	args = ap.parse_args()
	
	txt2bin(args.txtfile)