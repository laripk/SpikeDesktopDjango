import webview
import threading
import os
import sys


SERVER_ADDRESS = "http://google.com:80" # include port


def manageweb(*args):
	"""mimics django's manage.py"""
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sddweb.settings")

	from django.core.management import execute_from_command_line

	execute_from_command_line(args)



def start_server():
	"""starts our internal web server (or will soon)"""
	pass


if __name__ == '__main__':
	t = threading.Thread(target=start_server)
	t.daemon - True
	t.start()
	
	webview.create_window("Spike Django Desktop", SERVER_ADDRESS)
	
	# do clean up procedure and destroy any remaining threads after the window is destroyed
	sys.exit()

