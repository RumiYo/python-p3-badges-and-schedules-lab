def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    # badge_list = list()
    # for n in names:
    #     badge_list.append(badge_maker(n))

    badge_list  = [badge_maker(n) for n in names]

    return badge_list

def assign_rooms(names):
    # room_number = 1
    # room_assignments = list()
    # for n in names:
    #     room_assignments.append(f"Hello, {n}! You'll be assigned to room {room_number}!")
    #     room_number += 1

    room_assignments = [ f"Hello, {n}! You'll be assigned to room {names.index(n)+1}!" for n in names]

    return room_assignments

def printer(names):
    for n in batch_badge_creator(names):
        print(n)
    for n in assign_rooms(names):
        print(n)
    return None
