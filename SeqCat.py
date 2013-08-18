"""
"""
import os, os.path, sys, errno
from os.path import isdir
import fnmatch
import gzip

def mkdir_p(newfolder):
  """
  """
  try:
    os.makedirs(newfolder)
  except OSError as exception:
    if exception.errno == errno.EEXIST and os.path.isdir(newfolder):
      pass
    else:
      raise

def findFolders(path = '.'):
  """
  """
  folders = [fold for fold in os.listdir(path) if isdir(fold)]
  return folders

def findZips(path = '.'):
  """
  """
  zips = []
  for root, dirs, files in os.walk(path):
    for file in fnmatch.filter(files, '*.fastq.gz'):
      zips.append(file)
  unique = list(set(zips))
  return unique

def concatZips(zip, folder, newpath):
  """
  """
  dest = './' + newpath + '/' + zip[:-3]
  print 'Creating ' + dest
  command = 'gzip -dc'
  files = []
  for folder in folders:
    src = './' + folder + '/' + zip
    if os.path.isfile(src):
      files.append(src)
  for file in files:
    f = gzip.open(file, 'rb')
    file_content = f.read()
    with open(dest, "a") as myfile:
      myfile.write(file_content)
      myfile.close()
    f.close()

if __name__ == '__main__':
  if len(sys.argv) < 2:
    sys.exit('Usage: %s <folder_name>' % sys.argv[0])
  mkdir_p(sys.argv[1])
  folders = findFolders()
  zips = findZips()
  print folders
  print zips
  for zip in zips:
    concatZips(zip, folders, sys.argv[1])
  print 'Done'
