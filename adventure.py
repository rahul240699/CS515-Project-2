import sys
import json
import traceback
import inspect

class adventure:
    def __init__(self, map):
        self.inventory_items = []
        self.room = 0
        self.map = map

    def go(self, dir):
        if dir not in self.map[self.room]['exits'].keys():
            print(f"There's no way to go {dir}.")
        else:
            print(f"You go {dir}.\n")
            self.room = self.map[self.room]['exits'][dir]
            self.look()
        return True

    def look(self):
        print(f"> {self.map[self.room]['name']}\n")
        print(f"{self.map[self.room]['desc']}\n")
        if "items" in self.map[self.room].keys():
            items = self.map[self.room]['items']
            i_string = ""
            if len(items) >= 1:
                for i in items:
                    i_string += f"{i}, "
                print(f"Items: {i_string[:-2]}\n")
        exits = self.map[self.room]['exits'].keys()
        e_string = ""
        if len(exits) >= 1:
            for i in exits:
                e_string += f"{i} "
        print(f"Exits: {e_string[:-1]}\n")
        return True

    def get(self, item):
        if item in self.map[self.room]['items']:
            self.inventory_items.append(item)
            self.map[self.room]['items'].remove(item)
            print(f"You pick up the {item}.")
        else:
            print(f"There's no {item} anywhere.")
        return True
    
    def inventory(self):
        if len(self.inventory_items) > 0:
            print("Inventory: ")
            for i in self.inventory_items:
                print(f" {i}")
        else:
            print("You're not carrying anything.")
        return True

    def quit(self):
        print("Goodbye!")
        return False
    
    #Extensions

    def help(self):
        all_attributes = dir(adventure)
        functions = [func for func in all_attributes if not func.startswith("__") and not func.endswith("__")]
        print("You can run the following commands:")
        for i in functions:
            func = getattr(adventure, i)
            signature = inspect.signature(func)
            parameters = signature.parameters
            if len(parameters) > 1:
                print(f" {i} ...")
            else:
                print(f" {i}")
    


def main():
    try:
        with open(sys.argv[1]) as file:
            m = json.load(file)
    except ValueError as e:
        print("Invalid Map!")
    
    a = adventure(m)
    a.look()

    while True:
        try:
            inp = input("What would you like to do? ")
        except EOFError as e:
            print("\nUse 'quit' to exit.")
            continue
        except KeyboardInterrupt as e:
            print(traceback.format_exc())
            return 0
        inp = inp.strip().lower().split(" ")
        # print(f"{inp[0]}")
        
        if inp[0] == "quit":
            a.quit()
            return 0
        
        if inp[0] == "look":
            a.look()
        
        if inp[0] == "go":
            if len(inp) > 1:
                a.go(inp[1])
            else:
                print("Sorry, you need to 'go' somewhere.")
                continue

        if inp[0] == "get":
            if len(inp) > 1:
                a.get(inp[1])
            else:
                print("Sorry, you need to 'get' something.")
                continue
        
        if inp[0] == "inventory":
           a.inventory()

        if inp[0] == "help":
            a.help()



        

if __name__ == "__main__":
    main()