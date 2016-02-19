import webview
import multiprocessing
import os
import sys


if __debug__:
    from sddweb.sddweb import settings
    print(settings.DATABASES)


SERVER_ADDRESS = "127.0.0.1:9966"  # include port  # "http://google.com:80"
START_PATH = "http://" + SERVER_ADDRESS + "/polls"
if __debug__:
    print("start path", START_PATH)

    
    
def manageweb(*args):
    """mimics django's manage.py"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sddweb.sddweb.settings")
    
    print("\n---------manageweb---------")
    print("args", args)
    
    from django.core.management import execute_from_command_line
    execute_from_command_line(args)
    #call_command(name, *args, **options)



def start_server():
    """starts our internal web server (or will soon)"""
    manageweb("manageweb", "runserver", "--noreload", SERVER_ADDRESS)  # addrport=
    # manageweb("manageweb", "help", "runserver")  # this works!



if __name__ == '__main__':
    t = multiprocessing.Process(target=start_server)
    t.daemon - True
    t.start()
    
    webview.create_window("Spike Django Desktop", START_PATH)
    
    # do clean up procedure and destroy any remaining threads after the window is destroyed
    sys.exit()

