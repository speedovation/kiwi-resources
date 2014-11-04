#!/usr/bin/env python
"""
nftp.py - A Simple FTP Command Line Utility

Help: ./nftp.py --help
Author: Sean B. Palmer, inamidst.com
License: GNU GPL 2
Date: 2003-11
"""

import sys, os, re, ftplib
from optparse import OptionParser

config = os.path.expanduser('~/.nftprc')
r_field = re.compile(r'(?s)([^\n:]+): (.*?)(?=\n[^ \t]|\Z)')

def getConfig(name=None): 
   # Find the config file
   home = os.path.expanduser('~/')
   nftp_conf = os.getenv('NFTP_CONF')
   if nftp_conf is not None: 
      s = open(confenv).read()
   elif os.path.exists(config): 
      s = open(config).read()
   elif os.path.exists('.nftprc'): 
      s = open('.nftprc').read()
   elif os.path.exists('nftp.conf'): 
      s = open('nftp.conf').read()
   elif os.path.exists(home + 'nftp.conf'): 
      s = open(home + 'nftp.conf').read()
   else: return {}

   # Parse the config file
   conf = {}
   s = s.replace('\r\n', '\n')
   s = s.replace('\r', '\n')
   for item in s.split('\n\n'): 
      meta = dict(r_field.findall(item.strip()))
      if meta.has_key('name'): 
         fname = meta['name']
         del meta['name']
         conf[fname] = meta
      else: raise 'ConfigError', 'Must include a name'

   if name is not None: 
      return conf[name]
   else: return conf

def pathSplit(filepath): 
   if filepath.startswith('/'): 
      filepath = filepath[1:]

   if '/' not in filepath: 
      return '', filepath

   parts = filepath.split('/')
   filename = parts.pop()
   return '/'.join(parts), filename   

def getFtp(meta): 
   ftp = ftplib.FTP(meta['host'], meta['username'], meta['password'])
   ftp.cwd(meta['remotedir'])
   return ftp

def chmod(name, filepath, code): 
   meta = getConfig(name)

   ftp = getFtp(meta)
   path, fn = os.path.split(filepath)
   path = path.lstrip('/')
   ftp.cwd(path)

   print >> sys.stderr, 'Performing CHMOD -%s on %s...' % (code, fn)
   result = ftp.sendcmd('SITE CHMOD %s %s' % (code, fn))
   print >> sys.stderr, 'Result: %s' % result

def upload(name, filepath): 
   meta = getConfig(name)

   ftp = getFtp(meta)
   path, fn = os.path.split(filepath)
   path = path.lstrip('/') or '.'
   try: ftp.cwd(path)
   except ftplib.error_perm, e: 
      print >> sys.stderr, 'Got error: "%s"' % e
      if raw_input("Create folder /%s? [y/n]: " % path).startswith('y'): 
         for folder in path.split('/'): 
            try: ftp.cwd(folder)
            except: 
               ftp.mkd(folder)
               ftp.cwd(folder)
      else: sys.exit(1)

   f = open(os.path.join(meta['localdir'], path+'/'+fn), 'rb')
   print >> sys.stderr, 'Storing %s...' % filepath
   result = ftp.storbinary('STOR %s' % fn, f)
   print >> sys.stderr, 'Result: %s' % result
   f.close()

def get(name, filepath): 
   meta = getConfig(name)

   ftp = getFtp(meta)
   path, fn = os.path.split(filepath)
   path = path.lstrip('/')
   ftp.cwd(path)

   retrieve = False
   filename = os.path.join(meta['localdir'], path + '/' + fn)
   if os.path.exists(filename): 
      retrieve = raw_input('Overwrite %s? [y/n]: ' % fn).startswith('y')
   else: retrieve = True

   if retrieve: 
      f = open(filename, 'wb')
      print >> sys.stderr, 'Getting %s...' % filepath
      ftp.retrbinary("RETR %s" % fn, f.write)
      print >> sys.stderr, 'Downloaded successfully'
      f.close()
   else: print >> sys.stderr, "Didn't download %s" % fn

def delete(name, filepath): 
   meta = getConfig(name)

   ftp = getFtp(meta)
   path, fn = os.path.split(filepath)
   path = path.lstrip('/')
   ftp.cwd(path)

   if raw_input('Really delete %s? [y/n]: ' % fn).startswith('y'): 
      print >> sys.stderr, 'Deleting %s...' % fn
      try: result = ftp.delete(fn)
      except ftplib.error_perm, e: 
         msg = 'Got "%s", try deleting as directory? [y/n]: ' % e
         if raw_input(msg).startswith('y'): 
            try: result = ftp.rmd(fn)
            except ftplib.error_perm, e: 
               print >> sys.stderr, 'Error:', e
               sys.exit(1)
      print >> sys.stderr, 'Result: %s' % result
   else: print >> sys.stderr, "Didn't delete %s" % fn

# upload, -c chmod, -d delete, -u update, -g get

def main(argv=None): 
   parser = OptionParser(usage='%prog [options] <name> <path>')
   parser.add_option("-c", "--chmod", dest="chmod", default=False, 
                     help="chmod a file on the server")
   parser.add_option("-u", "--update", dest="update", 
                     action="store_true", default=False, 
                     help="update a file, on the server or locally")
   parser.add_option("-g", "--get", dest="get", 
                     action="store_true", default=False, 
                     help="download a file from the server")
   parser.add_option("-d", "--delete", dest="delete", 
                     action="store_true", default=False, 
                     help="delete a file from the server")

   options, args = parser.parse_args(argv)

   if (len(args) < 1) or (len(args) > 2): 
      parser.error("Incorrect number of arguments")
   elif len(args) == 1: 
      print >> sys.stderr, 'Guessing account and path...'
      found, cwd, fn = False, os.getcwd(), args[0]
      for (account, info) in getConfig().items(): 
         if cwd.startswith(info['localdir']): 
            path = cwd[len(info['localdir']):]
            filepath = path + '/' + fn
            print >> sys.stderr, 'Found "%s %s"' % (account, filepath)
            # if raw_input(msg).startswith('y'): 
            name, found = account, True
      if not found: 
         print >> sys.stderr, "Couldn't find an account!"
         sys.exit(1)
   else: name, filepath = args

   if options.update: 
      raise "NotImplemented", "@@ implement!"
   elif options.chmod: 
      chmod(name, filepath, options.chmod)
   elif options.get: 
      get(name, filepath)
   elif options.delete: 
      delete(name, filepath)
   else: upload(name, filepath)

if __name__=="__main__": 
   main()
