import bencode
import os
import glob

def parseFile(filename):
	f = open(filename)
	f2 = open(filename + '.rtorrent')


	r = f.read()
	r2 = f2.read()

	b = bencode.bdecode(r)
	b2 = bencode.bdecode(r2)

	if 'files' in b['info']:
		for f in b['info']['files']:
			path = b2['directory']
			for g in f['path']:
				path = os.path.join(path, g)
			print path
	else:
		print os.path.join(b2['directory'], b['info']['name'])

for f in glob.glob('*.torrent'):
	parseFile(f)
