#!/usr/bin/python3.7

import sys, os
from time import sleep
from threading import Thread



#######################################################

def help_text(create:bool=False, serve:bool=False) -> None:
	"""
	print help text

	params:
		create:bool : prints help text for create command
		serve:bool  : prints help text for serve command
	"""

	print('usage:')

	if create:
		print('\tmanage create [project_name]')

	if serve:
		print('\tmanage serve')
		print('\tmanage serve [project_name]')






#######################################################

def create_p5_project(name:str) -> None:
	"""
	create a p5 project with specified name

	params:
		name:str : create a folder "name" with default files
	"""
	if name in os.listdir():
		print(f'folder {name} already exists')
		print('exiting')
		return

	print(f'creating project {name}')

	os.mkdir(name)
	with open(f'{name}/index.html', 'w') as f:
		f.write(f"""<!DOCTYPE html>
<html>
<head>
	<title>{name}</title>
	<script src='../lib/p5.js'></script>
	<script src='script.js'></script>
</head>
<body>
	<h1>{name}</h1>
</body>
<style>
	* {{padding: 0px; margin: 0px;}}
	body {{
		text-align: center;
		color: #fff;
		font-family: Roboto;
		background: #111;
	}}
</style>
</html>""")

	with open(f'{name}/script.js', 'w') as f:
		f.write(f"""function setup() {{
	createCanvas(400,400);
	mouseX = -100;
	mouseY = -100;
}}

function draw() {{
	noStroke();
	fill(255, 255, 255, 3);
	ellipse(mouseX, mouseY, 250);
}}""")







#######################################################

def serve_project(name:str=None) -> None:
	"""
	create a p5 project with specified name

	params:
		name:str : name for the project to serve, optional param
	"""

	if name:
		if name not in os.listdir():
			print(f'folder {name} doesn\'t exists')
			print('exiting')
			return
		s = f'x-www-browser http://localhost:8000/{name}'
	else:
		s = 'x-www-browser http://localhost:8000'

	def f1():
		sleep(1)
		os.system(s+' > /dev/null 2>&1')
	Thread(target=f1).start()
	os.system('python3 -m http.server 8000 --bind 0.0.0.0')








#######################################################

if __name__ == '__main__':

	args = sys.argv[1:]

	if len(args)==0 or '-h' in args or '--help' in args:
		help_text(create=True, serve=True)

	elif args[0]=='create':
		if '-h' in args or '--help' in args or len(args) == 1:
			help_text(create=True)
		else:
			create_p5_project(args[1])

	elif args[0]=='serve':
		if '-h' in args or '--help' in args:
			help_text(serve=True)
		elif len(args) == 1:
			serve_project()
		else:
			serve_project(args[1].split('/')[-1] if '/' in args[1] else args[1])

