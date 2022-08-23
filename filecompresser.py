import zipfile,os,sys,shutil
import numpy as np

username=input("enter your name: ")
username=str(username)
print("hello "+username+" welcome to ziply a file and directrory compressor")
print('----------------------------------------------------------------------------------------')
userresponse=input("do you want to know more about us?(press y or n)")
userresponse=str(userresponse)
for i in range(1):
    if userresponse=='y':
        print('ziply was developed by Kris Muiru,a python geek. It was developed to make compression of files much easier and convenient ')
    else:
        pass
print('-------------------------------------------------------------------------------------------------------------------------------------')
userpath=input("enter  the folder that contains your files:  ")
userpath=str(userpath)
for i in os.listdir(userpath):
        try:
            if i.startswith('.'):
                pass
            else:
                print(i)
        except Exception as error:
            print("an error occurred when listing folder containing your files")
            
print('------------------------------------------------------------------------------------------------------------------------------------')
userrange=input("How many files and/ folders do you want to compress: ")
#array
userinput=np.array([])
for i in range(int(userrange)):
    file2compress=input('enter file and/ folder'+str(i+1)+'     (press /t to terminate,enter to go to next line): \n')
    file2compress=str(file2compress)
    print('')
    if file2compress=='/t':
        break
    else:
        userinput=np.append(userinput,file2compress)
print('----------------------------------------------------------------------------------------------------------------------------------')
completefilelist=np.array([])
for i in range(len(userinput)): 
    completefilepath=userpath+'/'+str(userinput[i])
    completefilelist=np.append(completefilelist,completefilepath)
    print(completefilelist[i])
print('---------------------------------------------------------------------------------------------------------------')
dir2save=input('Create a directory name to save your zipfile:  ')
dir2save=str(dir2save)
print(' ')
print('------------------------')
createdfolder=os.mkdir(dir2save)
userzipfile=input('Create your zipfile name with a .zip extension:  ')
userzipfile=str(userzipfile)
if userzipfile.endswith('.zip'):
    pass
else:
    sys.exit()
userzipfile=str(userzipfile)
newzip=zipfile.ZipFile(userzipfile,'a')
for i in range(len(completefilelist)):
    newzip.write(completefilelist[i],compress_type=zipfile.ZIP_DEFLATED)
newzip.close()
print('')
print('----------------------------------------------')
shutil.move(userzipfile,dir2save)
print('thanks for using our service')
