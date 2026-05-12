# fname=input("enter the file name")
# fptr=open(fname,"w")
# for i in range(2):
#     eid=input("enter the eid:")
#     ename=input("enter the ename:")
#     edes=input("enter the edes:")
#     esal=input("enter the esal:")
#     eaddr=input("enter the eaddr:")
#     fptr.write(eid+"\t"+ename+"\t"+edes+"\t"+esal+"\t"+eaddr+"\n")
# fptr.close()
# print("5 names are written to text file")


# print("enter file name")
# fname=input()
# fptr=open(fname,"r")
# data1=fptr.readline()
# print(data1)
# data5=fptr.readline(5)
# print(data5)
# data2=fptr.read(10)
# print(data2)

# data3=fptr.readline()

# data3=fptr.readline()
# print(data3)

# data4=fptr.read()
# print(data4)

# fptr=open("emp.txt","r")
# print("write",fptr.readable)

                                            # Split method 

# str1="rama krishna"
# res=str1.split()
# print(res)


# fptr=open("karachi.txt","r")
# print(fptr.name)m
# print(fptr.mode)
# print(fptr.writable)
# print(fptr.readable)
# print(fptr.closed)
# fptr.close()
# print(fptr.closed)


# fptr=open("car.jpg","rb")
# data=fptr.read()
# print(data)

# fptr=open("car.jpg","rb")
# data=fptr.read()
# fptr1=open("newimage.jpg","wb")
# fptr1.write(data)
# fptr.close()
# fptr1.close()

#                       TO WRITE INTO CSV FILE
# import csv
# print("enter the filename")
# fname=input()
# fptr=open(fname,"a",newline=" 80*-+)
# w=csv.writer(fptr)
# w.writerow(["eid","ename","edes","esal","eaadr"])
# for i in range(5):
#     eid=input("enter eid:")
#     ename=input("enter ename")
#     edes=input("Enter the eDesignation:")
#     esal=input("Enter salary")
#     eaadr=input("enter e address")
#     w.writerow([eid,ename,edes,esal,eaadr])
# fptr.close()
# print("5 employess details stored in csv file")



#                           TO READ FROM CSV FILE
# import csv
# print("enter the filename")
# fname=input()
# fptr=open(fname,"r")
# rea=csv.reader(fptr)
# header=next(rea)
# for row in rea:
#         print(" ".join(row))
       

# import csv
# print("enter the filename")
# fname=input()
# fptr=open(fname,"r")
# rea=csv.reader(fptr)
# next(rea)
# for row in rea:
#         print(row[0],row[1])

# import csv
# print("enter the filename")
# fname=input()
# fptr=open(fname,"r")
# row_num=int(input("Enter the row"))
# rea=csv.reader(fptr)
# next(rea)
# for cureent_row,row in enumerate (rea,start=1):
#     if cureent_row==row_num:
#         print(" ".join(row))
#         break
# else:
#         print("nothinf ")


#                                               READING FILE(image)
# fptr=open("car.jpg","rb")
# data=fptr.read()
# print(data)
# for i in data:
#     print(format(i,"02b"),end=" ")

# fptr=open("car.jpg","rb")
# data=fptr.read()
# fptr1=open("newimage.jpg","wb")
# fptr1.write(data)
# fptr.close()
# fptr1.close()
# print("file copied")

# fptr=open("text.txt","rb")
# data=fptr.read()
# print(data)
# for i in data:
#     print(format(i,"08b"),end=" ")

##                                      SERIALIZATION
# import pickle
# class Emp:
#     def __init__(self,eid,ename,edes,esal):
#         self.eid=eid
#         self.ename=ename
#         self.edes=edes
#         self.esal=esal
#     def disp(self):
#         print(self.eid)
#         print(self.ename)
#         print(self.edes)
#         print(self.esal)
# e=Emp(101,"rama","dev",20920)
# f=open("karachi.txt","wb")
# pickle.dump(e,f)
# f.close
# print("Object stored")



##                                      DESERIALIZATION   
# import pickle
# class Emp:
#     def __init__(self,eid,ename,edes,esal):
#         self.eid=eid
#         self.ename=ename
#         self.edes=edes
#         self.esal=esal
#     def disp(self):
#         print(self.eid)
#         print(self.ename)
#         print(self.edes)
#         print(self.esal)
# f=open("karachi.txt","rb")
# e=pickle.load(f)
# e.disp()
# f.close()
# print("Object loaded")

##                                    THREADING
# import time
# class vlc:
#     def apl_open(self):
#         print("vlc application opened")
#         time.sleep(3)
#     def video_play(self):6
#         print("video started playing")
#         time.sleep(3)          
#     def audio_play(self):
#         print("audio started playing")
#         time.sleep(3)
#     def timer_on(self):
#         print("timer turned on")
#         time.sleep(3)
#     def prg_bar(self):
#         print("progress bar is active")
#         time.sleep(3)
# v=vlc()
# v.apl_open()
# v.video_play()
# v.audio_play()
# v.timer_on()
# v.prg_bar()
# print("appplication closed:")
