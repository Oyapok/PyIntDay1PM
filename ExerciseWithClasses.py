
'''
Given a file with the following format:
    
    City name;time;date;temperature
    Geneva;12:34;2003/12/23;2.34;
    Lausanne;12:36;2003/12/23;3.34;
    Bern;12:36;2003/12/23;-3.34;
    ....
    
Write a python script to parse this file and store it's content into a "custom
object".

You could define a class "Record" that will represent a line of this file and
a class "ListOfRecord" to represent a list of "Record".
This class "ListOfRecord" should offer a way to construct an instance of it
with the help of a text file like the one above.
It should also offers ways to save/restore the list easily.
And a method to compute the average of the temperature recorded for a given city name.

with open("data.txt") as fic:
    first=fic.readline()
    for line in fic:
        print(line)

'''

# import pickle

class Record:
    def __init__(self,name,time,date,temperature):
        self.city=name
        self.time=time
        self.date=date
        self.temperature=temperature
        
    def __str__(self):
        return str("City of {self.city} at {self.time} on the {self.date} the temperature was {self.temperature}°C")
    
    def parseRecord(text):
        c,t,d,temp=text.split(";")
        return Record(c, t, d, float(temp))
        

class ListOfRecord:
    def __init__(self):
        self.data=[] 
        
    def __str__(self):
        return str(self.data)
       
    def addRecord(self, record):
        self.data.append(record)
    
    @staticmethod
    def parseFile(fname):
        recList = ListOfRecord()
        with open(fname) as fic:
            for line in fic:
                recList.addRecord(line)
        return recList

if __name__ == "__main__":
      
    records=ListOfRecord.parseFile("measures.txt")
    print(records[1])
    
    
    record1=Record.parseRecord(ListOfRecord.da


# with open("measures.txt") as fic:
#     d=fic.readline()
#     # for line in fic:
#     #     print(line)
    
#     print(fic)
# print(d, type(d))

# class Data:
#     def __init__(self,name,time,date,t):
        
#         self.content[]