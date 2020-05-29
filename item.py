class Item():

    def __init__ (self, item_name):
        """ Initializes the item with a name"""
        self.name = item_name
        self.description = None


    def set_name(self, item_name):
        """ Sets the name of the item to the item_name"""
        self.name = item_name

    def get_name(self):
        """ Returns the name of the item"""
        return self.name

    def set_description(self, item_description):
        """ Sets the description of the item"""
        self.description = item_description


    def get_description(self):
        """ Returns the description of this item"""
        return self.description

    def describe(self):
        print("The  [" + self.name + " ] is here - " + self.description)