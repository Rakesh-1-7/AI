import random


class Room:
    #randomly select vacuum position
    cost = 0
    def __init__(self,room_num,state):
        self.room_num = room_num
        self.state = state

if __name__ == "__main__":
    vacuum_pos = random.randint(1,2)
    print("Vacuum")
    states = ['clean','dirty']
    room1 = Room(1,random.choice(states))
    room2 = Room(2,random.choice(states))
    print(f"Start states : {[room1.state,room2.state]}")


    while room1.state == 'dirty' or room2.state == 'dirty':
        if vacuum_pos == 1:
            if room1.state == 'clean':
                print(f"{room1.room_num} is clean.")
                vacuum_pos = 2
            else:
                print(f"Cleaning room number : {room1.room_num}")
                Room.cost += 1
                print(f"{room1.room_num} is clean.")
                room1.state = 'clean'
        else:
            if room2.state == 'clean':
                print(f"{room2.room_num} is clean.")
                vacuum_pos = 1
            else:
                print(f"Cleaning room number : {room2.room_num}")
                print(f"{room2.room_num} is clean.")
                Room.cost += 1
                room2.state = 'clean'
    print(f"Cost : {Room.cost}")

