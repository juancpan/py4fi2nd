#
# Jupyter Notebook Configuration File
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
# SSL ENCRYPTION
# replace the following filenames (and files used) with your choice/files
c.NotebookApp.certfile = u'/root/.jupyter/cert.pem'
c.NotebookApp.keyfile = u'/root/.jupyter/cert.key'

# IP ADDRESS AND PORT
# set ip to '0.0.0.0' to bind on all IP addresses of the cloud instance
c.NotebookApp.ip = '0.0.0.0'
# it is a good idea to set a known, fixed default port for server access
c.NotebookApp.port = 8888

# PASSWORD PROTECTION
# here: 'jupyter' as password
# replace the hash code with the one for your strong password
c.NotebookApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$aD0gRO6vocgR1nG4cf1aLg$B8uA0Ec6C/2WRUxeQv6pw5OW2jf/mWHoUb9fsXJb+o0'

# NO BROWSER OPTION
# prevent Jupyter from trying to open a browser
c.NotebookApp.open_browser = False
