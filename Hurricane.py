##Emily Dennis 13/04/19


###program displays the correct Saffir-Simpson Hurricane Wind
###Scale category for a wind speed entered by the user and the selected unit.

#imports items from tkinter
from tkinter import Frame, OptionMenu, StringVar, Tk, Entry, Button, LEFT, Label


#creates hurricane class 
class Hurricane(Frame):
    #initialises the class
    def __init__(self, master = None):
        #intitalises the frame
        Frame.__init__(self, master)

        loadData = self.LoadData()
        #loads in data
        list2 = loadData[1]
        #sets list2 variable as the 2nd item of loadData

        self.populate =[list2[0],list2[1],list2[2]]
        #populates the dropdown using the 2nd tuple by splitting it
        

        self.variable = StringVar()
        #creates a string variable
        
        self.variable.set(self.populate[0])
        #set the first item in the list to appear as default on dropdown
    
        Label(self, text = "select units").pack(side = LEFT)
        #sets label
        self.HurricaneMenu = OptionMenu(self, self.variable,*self.populate)
        #set option menu parameters

        self.HurricaneMenu.pack(side = LEFT)
        #packs the menu so it appears on the frame
        self.e =StringVar()
        #creates a string variable
        hurricane_entry = Entry(self, width = 7, textvariable = self.e )
        #sets the hurricane entry widget
        hurricane_entry.pack(side = LEFT)
        #packs the entry box so it appears on the frame

        self.feedback =loadData[0]
        #sets self.feedback as the first item in the tuple from loadData
        self.possibleUnits =loadData[1]
        #sets self.possibleUnits as the second item in the tuple from loadData
        self.thresholds =loadData[2]
        #sets self.thresholds as the third item in the tuple from loadData
 
   
        
      
        calc = Button(self, text = "Calculate", command = self.GetFeedback).pack(side = LEFT)
        #calculate button runs GetFeedback method
        


        hurricane_entry.focus()
        #the application focuses on the entry box on load
        for c in self.master.winfo_children():
            c.pack_configure(padx = 100, pady = 5)
            #configures the packing on the window
        self.var = StringVar()
        #sets a string variable
        self.var.set("                              ")
        #sets this as blank
        self.L2 = Label(self, textvariable=self.var).pack()
        #sets the label text as self.var
        


    #loads data from Hurricane.dat

    def LoadData(self):
        feedback = []
        possibleUnits =[]
        thresholds=[]
        SEPARATOR = '----------'
        #set the values to be determined, and the seperator
	
        inf = open("Hurricane.dat", "r")
        #open Hurricane.dat
        sData = inf.readlines()
        #set sData to readlines of file
        inf.close()
        #close file
        
        i=0
        while sData[i].strip() != SEPARATOR:
            #when the line being read is not equal to seperator
            feedback.append(sData[i].strip())
            #appends read data to feedback
            i = i + 1
   
        i = i + 1 
    
    
        while i<len(sData):
            #while the length of sData is bigger than the iterator
            possibleUnits.append(sData[i].strip())
            #appends read data to possibleUnits
            i = i + 1
            thresholdlist = []
            while sData[i].strip() != SEPARATOR:
                thresholdlist.append(int(sData[i].strip()))
                #appends read data to threshold list
                i = i + 1
            thresholds.append(thresholdlist)
            #appends the thresholdlist to threshold
            i = i + 1

        # @return a tuple
        return (feedback, possibleUnits, thresholds)

        
   #is loaded when the calc button is clicked
    def GetFeedback(self):
        feedback = self.feedback
        possibleUnits = self.possibleUnits
        thresholds = self.thresholds
        #sets the parameters to be used in get feedback using self statements.
        units = (self.variable.get()) 
        query = (self.e.get())
        #additional parameters set using get statements
        
        

        feedbackForInput= ["Both inputs are not valid",
                           "The query type is not correct",
                           "The query value is not a whole number",
                           "Inputs are all valid"]
        #loop through feedback

        validInput = str(query).isdigit() and (units in possibleUnits)
        #set what a valid input is
        inputValidation = feedbackForInput[int(str(query).isdigit()) + 2*int(units in possibleUnits)]
        #determine the correct index

        output = ""

        if validInput:
        #determines things if validInput is True

            iquery= int(query)
            #a variable for int form of query
            iUnit = possibleUnits.index(units)
            #a variable for that matches the index for thresholds based on the unit
            i = 0
            while (i<len(thresholds[iUnit])) and (iquery>thresholds[iUnit][i]):
            #determines the threshold values

                i = i + 1
            output = feedback[i]

        #ouput is retrieved
            
        if (inputValidation == ("Inputs are all valid")):
            self.var.set(output)
        #label to display input if the validation condition is met

        else:
            self.var.set(inputValidation)
        #present error message if input is not valid
            

        

if __name__ == "__main__":
    Hurricane().mainloop()
#runs the code

