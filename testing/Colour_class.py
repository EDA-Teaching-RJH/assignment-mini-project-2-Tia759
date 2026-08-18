class Colour: 
    #classes use Upper case 
 
 
    #level means primary colour/secondary colour or neither, i am unsure what other term i could use
    def __init__(self,natural,level):
        self.natural = natural
        self.level = level

    def primary_colour(self):
        print ("This colour is a primary colour.")

    def secondary_colour(self):
        print ("This colour is a secondary colour.")

    def neither(self):
        print ("This colour is neither a primary nor secondary colour.")
