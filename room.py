class Room():

    def __init__ (self, room_name):
        """ Initializes the room with a name"""
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_character(self, new_character):
        """ Sets the character to new_character"""
        self.character = new_character

    def get_character(self):
        """ Returns character"""
        return self.character

    def set_name(self, room_name):
        """ Sets the name of the room to the room_name"""
        self.name = room_name

    def get_name(self):
        """ Returns  name"""
        return self.name

    def set_item(self, item_name):
        """ Sets item to item_name"""
        self.item = item_name

    def get_item(self):
        """ Returns  item"""
        return self.item

    def set_description(self, room_description):
        """ Sets room description"""
        self.description = room_description


    def get_description(self):
        """ Returns room description"""
        return self.description

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        """ Links rooms"""
        self.linked_rooms[direction] = room_to_link
        #print(self.name + "linked_rooms: " + repr(self.linked_rooms))

    def get_details(self):
        """ Returns details of this room"""
        print(self.name)
        print("_______________")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)


    def move(self, direction):
        """ Moves character in given direction"""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("Sorry you can't go that way")
            return self








