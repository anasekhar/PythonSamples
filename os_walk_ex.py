"""
 program to print os.walk ( using my function)
"""
import argparse
import os
import os.path
import sys

def my_os_walk(path):
    if not os.path.exists(path):
	print " Given {0} path is not vaild".format(path) 
    elif os.path.isdir(path):
	dir_list = os.listdir(path)
        for dir_name in dir_list:
		if os.path.isdir(os.path.join(path,dir_name)):
		    print "\n%s\n" %(dir_name)
		    my_os_walk(os.path.join(path,dir_name))
		else:
		    print "\t%s\n"%(dir_name)
	
	

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Please provide directory <pgm> -p <dirname>")
    parser.add_argument('-p','--path',help='provide dir/file path',required=True)
    args = parser.parse_args()
    print args
  #  argdict = vars(args)
  #  print argdict
  #  sys.exit(0)
    if args.path == 'None':
	print " Please provide directory/file as a argument"
    else:
    	my_os_walk(args.path)

