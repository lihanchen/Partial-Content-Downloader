#!/usr/bin/env python3
import os
import sys
import urllib.request

user_agent = 'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

def download(URL, filename):
	current_total_size = 0
	i = 1
	file = open(filename, 'wb')
	try:
		while True:
			req = urllib.request.Request(
				URL,
				data=None,
				headers={
					'User-Agent': user_agent,
					'Range': 'bytes=%d-' % current_total_size,
				}
			)
			print('%d part.\nDownloading from %d bytes...' % (i, current_total_size))
			response = urllib.request.urlopen(req)
			data = response.read()
			file.write(data)
			print('Received %d bytes.\n' % len(data))
			current_total_size += len(data)
			i += 1
			if response.status == 200: break
			if response.status != 206:
				print('Warning: unexpected status code: %d' % response.status)
	except urllib.request.HTTPError as err:
		if err.code != 416 or current_total_size == 0:
			print('Failed at %d bytes. Exit.' % current_total_size)
			raise e
		else:
			print('Nothing left.\n')
	print('Finished. Total size: ', current_total_size)
	file.close()

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: %s <URL> <output filename>' % sys.argv[0])
		exit(-1)
	URL = sys.argv[1]
	filename = sys.argv[2]
	if os.path.exists(filename):
		print('Output file already exist.')
		exit(-1)
	download(URL, filename)
