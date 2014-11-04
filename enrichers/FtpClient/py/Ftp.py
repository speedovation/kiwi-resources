from PythonQt import *
from ftplib import FTP
# set the title of the group box, accessing the title property
#ftpui.title = 'PythonQt Example'

# set the html content of the QTextBrowser
#box.browser.html = 'Hello <b>Qt</b>!'

# set the title of the button
#box.button1.text = 'Append Text' 

# set the text of the line edit
#box.edit.text = '42'

# define our own python method that appends the text from the line edit
# to the text browser


class YFtp(object):
  """docstring for YFtp"""
  
  ftp = ''

  def __init__(self):
    pass
    

  def connectHost(self,host,port,user,passwd):
    
    print (host,port,user,passwd)
    self.ftp = FTP()
    
    print("Done 1")
    
    print ( self.ftp.connect(host,int(port)) )
    print ( self.ftp.login(user,passwd) )
    print("Done 2")

  def getList(self):
    #self.ftp.retrlines('LIST')

    print ( FtpClient.listServerFiles.count )
    print ( FtpClient.listServerFiles.currentRow )
    #print ( ftpui.listServerFiles.item(0) )

    yyy = []
    self.ftp.retrlines("LIST", yyy.append)
    
    FtpClient.listServerFiles.addItem("some")

    for y in yyy:
      FtpClient.listServerFiles.addItem(str(y))
      #ftpui.listServerFiles.addItem(QtGui.QListWidgetItem(y))
    #ftpui.listServerFiles.count,
    #print (yyy)

  def showMe(self):
    print ( "Time SHOW" )
    FtpClient.show()


yftpInstance = YFtp() 

def connectFtp():
  yftpInstance.connectHost(FtpClient.hostname.text,FtpClient.port.text, FtpClient.username.text,FtpClient.password.text)


#  ftp = FTP('ftp.debian.org')     # connect to host, default port
#  ftp.login()                     # user anonymous, passwd anonymous@
  # Login successful.'
#  ftp.cwd('debian')               # change into "debian" directory
#  ftp.retrlines('LIST') 

# connect the button's clicked signal to our python method
FtpClient.btnConnect.connect('clicked()', connectFtp)

FtpClient.btnListFiles.connect('clicked()', yftpInstance.getList)

# connect the lineedit's returnPressed signal to our python method
#box.edit.connect('returnPressed()', appendLine)

# show the window


