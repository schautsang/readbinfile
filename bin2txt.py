
#filename: bin2txt.py

import argparse


def bin2txt(binaryfile = None):

	'''
	The functtion for read binary file to coverse as txt
	'''
	
	bytea = bytearray(binaryfile.read())
	
	filename = '{}'.format(args.outfile)
	
	fp = open(filename, 'wb')
	
	
	dict = {}
	key = 0
	value = 0
	for data in bytea:
		"value |= (data << 8 * (3 - key % 4))"
		value |= (data << 8 * (key % 4))
		key += 1
		if (key % 4) == 0:
			dict[(key - 1) >> 2] = value
			value = 0

	for key in dict:
		fp.write('{:08X}\n'.format(dict[key]))
	
	fp.close()
	binaryfile.close()

print 'covert completed...'


if __name__ == "__main__":

	'''
	The functtion for read binary file to coverse as txt
	
	example: bin2txt.py -o output.txt input.bin
	
	'''
	
	ap = argparse.ArgumentParser(description='Read binary file utility.')
	ap.add_argument('binfile', type=argparse.FileType('rb'), help='binary file to read')
	ap.add_argument('-o', '--outfile', help='txt file to write')
	args = ap.parse_args()
	
	bin2txt(args.binfile)
	