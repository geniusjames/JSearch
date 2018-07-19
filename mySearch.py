from tkinter import *
from ScrolledText import ScrolledText


import os

root = Tk()
location='/root' # for users of linux distro edit it to fit ur os and home name
#TODO: automatically detect os of host 
global save
tries=False
save={}
class JSearch():
    
    def __init__(self, master):
        tries=False
        self.var=StringVar()
        self.var.set('Nothing to Display, Enter text to search')
        self.master=master
        master.title("JSearch")
        
        self.var1=StringVar() #holds the result
        

        self.label2=Label(master, text='type text to search')
        self.label2.grid(row=0)
        
        self.entry=Entry(master,bd=5)
        self.entry.grid(row=0, column=1) #search entry
        self.label=Label(master, text=self.var.get(), width=40, height=5)
        self.label.grid(row=2)
        
        self.results=ScrolledText(master, width=70, height=15)
        self.results.insert(INSERT, '')
        self.results.grid(row=2, column=1)

        self.searchButton=Button(master, text="Search", command=self.main)
        self.searchButton.grid(row=1, column=1)

    def chDsp(self):
        
        self.var.set('updated')
        self.label.configure( text=self.var.get())
       
        self.label.update()
        root.update_idletasks()
    #scans the system
    def systemScan(self,iniList, location):
        self.location=location
        self.iniList=iniList
        length= len(iniList)
        searchText=self.entry.get()
        if (self.entry.get()==''):
            self.var.set('you must enter a text to search for')
            self.label.configure(text=self.var.get())            
            self.label.update()
            return
        else:
            self.var.set('SEARCHING...............')
            self.label.configure(text=self.var.get())            
            
            pass
       
        
        for i in range(length):
            
            if (iniList[i].find('.wine')!=-1):
                continue
            try:
                new_list = os.listdir(location +'/' + iniList[i])
                
                temp=location + '/' + iniList[i]
                self.var.set(temp)
                self.label.configure(text=self.var.get())
                self.label.update()                
                save[temp] = new_list
		        
               
                self.systemScan(new_list, temp)
                
            except OSError:
            	
                pass
            try:
                           
                self.fileSearch(searchText, str(iniList[i]), location)
            except:
                
                pass
        self.var.set('finished....')
        self.label.configure(text=self.var.get())
        self.label.update()
        return save
    

    # method to search for strings in a file

    def fileSearch(self, toSearch, currentFile, loc):
        self.currentFile=currentFile
        self.toSearch=toSearch
        s=''
        lst=len(os.listdir(location))
        
        global tries
               
     
        if(currentFile.find('.wine')!=-1):
            print 'found', loc
            return
        if (currentFile.find(toSearch)!=-1):
            
            s+='\n found '+ currentFile + '==> '+ loc+ ' \n'
            
            self.results.insert(INSERT, str(s))
            self.results.update
           
            
    def main(self):
        
        try:
            initial_list=os.listdir(location)
      
            
        except OSError:
            print ("error")
        print ('.......................')
        k = self.systemScan(initial_list, location)
        
    def get_input(self):
        searchStr =input()
        return str(searchStr)

    
    
search=JSearch(root)

root.mainloop()
