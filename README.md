# CS 515 Project 2

# Adventure Game

## Author Information
Rahul Sohandani 
rsohanda@stevens.edu

[Github Repository](https://github.com/rahul240699/CS515-Project-2)

## Estimation of Hours Spent on the project
I spent around 7 hours approximately on the project.

## Testing of the code
1. Initially I started the testing on my PC's terminal.
2. Later on I wrote test cases in the format specified in description, and wrote a test harness to check the output.

## Unresolved Issue or bug
1. Although the basic functionality is completely implemented, the autograder doesn't clear some of the tests.

## Examples of difficult bugs resolved
1. I didn't encounter any masjor issue as such.

## Extensions Implemented
1. **help** : I have implemented the help extension, that shows a list of commands that the user can run. The implementation is dynamic which means everytime one adds a command it will dynamically appear in response from the help command. It also print "..", indicating the commands which accept input parameters. The following example shows the help command.

```
What would you like to do? help
You can run the following commands:
 drop ...
 get ...
 go ...
 help
 inventory
 look
 quit
 unlock ...
```

2. **drop** : I have implemented the drop extension which drops an item from the player's inventory. The following example demonstrates the drop command.
```
What would you like to do? go east
You go east.

> A red room

This room is fancy. It's red!

Items: rose

Exits: north west

What would you like to do? get rose
You pick up the rose.
What would you like to do? inventory
Inventory: 
 rose
What would you like to do? drop rose
You drop the rose.
What would you like to do? inventory
You're not carrying anything.
What would you like to do? look
> A red room

This room is fancy. It's red!

Items: rose

Exits: north west

What would you like to do? drop
Sorry, you need to 'drop' something.
What would you like to do? drop x
You dont't have the x in your inventory to drop.
```

3. **Locked doors** : I have implemented a locked door extension where certain doors will be locked on the map, the door can be unlocked using **unlock** command. Every locked door will need a specific key that will be needed to unlock the door. The key can searched in the map. If the player posesses this key in their inventory, they will be able to unlock the door The follwing example shows the locked door extension. You need to use **lock.map** file provided as the map for using this extension.
```
> A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? go east
The door is locked, you need to unlock the door.
What would you like to do? unlock east
You don't have the correct key to unlock the door.
What would you like to do? inventory
You're not carrying anything.
What would you like to do? go north
You go north.

> A blue room

This room is simple, too, but with blue walls.

Exits: east south

What would you like to do? go east
You go east.

> A green room

You are in a simple room, with bright green walls.

Items: red key

Exits: west south

What would you like to do? get red key
You pick up the red key.
What would you like to do? inventory
Inventory: 
 red key
What would you like to do? go west
You go west.

> A blue room

This room is simple, too, but with blue walls.

Exits: east south

What would you like to do? go south
You go south.

> A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? unlock east
You have now unlocked the door! You can go in!
What would you like to do? go east
You go east.

> A red room

This room is fancy. It's red!

Items: rose

Exits: north west

What would you like to do? unlock north  
The door is already unlocked.
```