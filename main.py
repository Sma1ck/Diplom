#Template Event Manager script
import cimplicity
import time
from usb.core import find as finddev


class EventHandlerState:
    def __init__(self, event_action_context: cimplicity.EMEventActionContext):
        # An instance of the EventHandlerState object will be 
        # created for each configured Event-Action.
        # Put one time setup for the EventHandlerState in this method
        pass

    def do_event_action(self, event_data: cimplicity.CimEMEvent):
        # Place the event processing code in this method
        # This method will be called when the event triggers the action
        pass

    def do_shutdown(self, event_data: cimplicity.CimEMEvent):
        # This method will be called before the event manager reloads
        # a script or when emrp shutsdown.  This allows for the 
        # saving of results before the EventHandlerState is destroyed.
        pass

def do_test():
    # Put code in this function for testing the EventHandlerState class when testing the script outside of the event manager
    # 1) Create cimplicity.EMEventActionContext
    # 2) Create an instance of EventHandlerState passing in EMEventActionContext
    # 3) Create an instance of CimEMEvent passing it into the do_event_action method 
    #    of the EventHandlerState object instance
    #
    # Remove the following line when your implementation is provided.
    pass

def camera_reset():
    dev = finddev(idVendor=0x1234, idProduct=0x5678)
    dev.reset()

direction_dic = {
                'forward1': ['Robot1.Up1', 'Robot1.Up2'],
                 'back1': ['Robot1.Up2', 'Robot1.Up1'],
                 'up1': ['Robot1.Up4', 'Robot1.Up3'],
                 'down1': ['Robot1.Up3', 'Robot1.Up4'],
                 'clockwise1': ['Robot1.Up7', 'Robot1.Up8'],
                 'counterclockwise1': ['Robot1.Up8', 'Robot1.Up7'],
                 'grab1': ['Robot1.Up5', 'Robot1.Up6'],
                 'release1': ['Robot1.Up6', 'Robot1.Up5'],
                 'forward2': ['Robot2.Up5', 'Robot2.Up6'],
                 'back2': ['Robot2.Up6', 'Robot2.Up5'],
                 'up2': ['Robot2.Up4', 'Robot2.Up3'],
                 'down2': ['Robot2.Up3', 'Robot2.Up4'],
                 'clockwise2': ['Robot2.Up7', 'Robot2.Up8'],
                 'counterclockwise2': ['Robot2.Up8', 'Robot2.Up7'],
                 'grab2': ['Robot2.Up1', 'Robot2.Up2'],
                 'release2': ['Robot2.Up2', 'Robot2.Up1'],
}

coordinate_dic = {1: [[266, 40],[1, 262, 23]],
                  2: [[250, 24],[2, 250, 10]],
                  3: [[274, 77],[1, 263, 60]],
                  4: [[277, 77],[2, 266, 57]],
                  5: [[210, 162],[1, 188, 135]],
                  6: [[213, 165],[2, 190, 136]],
                  7: [[170, 173],[1, 151, 151]],
                  8: [[123, 182],[1, 105, 159]],
                  9: [[121, 184],[2, 120, 157]],
                  10: [[2, 110],[1, 15, 98]],
                  11: [[2, 110],[2, 2, 95]],
                  12: [[8, 79],[1, 5, 59]],
                  13: [[7, 76],[2, 0, 55]],
}

position_for_coordinate_dic = {
                    1: ['clockwise1', 'forward1', 'down1'],
                    2: ['clockwise1', 'forward1'],
                    3: ['clockwise1', 'down1'],
                    4: ['clockwise1'],
                    5: ['down1'],
                    6: [],
                    7.1: ['forward1', 'down1'],
                    7.2: ['clockwise2', 'forward2', 'down2'],
                    8: ['clockwise2', 'down2'],
                    9: ['clockwise2'],
                    10: ['down2'],
                    11: [],
                    12: ['forward2', 'down2'],
                    13: ['forward2']
}


def move_to_initial_position(direction_dic):
    """
    возвращает роботов в исходное положение
    """
    for  key, value in direction_dic.items():
        if key not in ['grab1', 'release1', 'grab2', 'release2']:
            if cimplicity.point_get(value[0])  == 1 or cimplicity.point_get(value[1]) == 1:
                cimplicity.point_get(value[0])
                cimplicity.point_get(value[1])
                cimplicity.point_set(value[0], 0)
                cimplicity.point_set(value[1], 0)
    cimplicity.point_get('Robot1.Vp1')
    cimplicity.point_get('Robot1.Vp2')
    cimplicity.point_get('Robot1.Vp3')
    cimplicity.point_get('Robot1.Vp4')
    cimplicity.point_get('Robot2.Vp1')
    cimplicity.point_get('Robot2.Vp2')
    cimplicity.point_get('Robot2.Vp3')
    cimplicity.point_get('Robot2.Vp4')
    cimplicity.point_set('Robot1.Vp1', 0)
    cimplicity.point_set('Robot1.Vp2', 0)
    cimplicity.point_set('Robot1.Vp3', 0)
    cimplicity.point_set('Robot1.Vp4', 0)
    cimplicity.point_set('Robot2.Vp1', 0)
    cimplicity.point_set('Robot2.Vp2', 0)
    cimplicity.point_set('Robot2.Vp3', 0)
    cimplicity.point_set('Robot2.Vp4', 0)
    time.sleep(2)

def reset(direction_dic):
    """
    Обнуление переменных
    """
    for  key, value in direction_dic.items():
        if cimplicity.point_get(value[0])  == 1 or cimplicity.point_get(value[1]) == 1:
            cimplicity.point_get(value[0])
            cimplicity.point_get(value[1])
            cimplicity.point_set(value[0], 0)
            cimplicity.point_set(value[1], 0)
    cimplicity.point_get('Robot1.Vp1')
    cimplicity.point_get('Robot1.Vp2')
    cimplicity.point_get('Robot1.Vp3')
    cimplicity.point_get('Robot1.Vp4')
    cimplicity.point_get('Robot2.Vp1')
    cimplicity.point_get('Robot2.Vp2')
    cimplicity.point_get('Robot2.Vp3')
    cimplicity.point_get('Robot2.Vp4')
    cimplicity.point_set('Robot1.Vp1', 0)
    cimplicity.point_set('Robot1.Vp2', 0)
    cimplicity.point_set('Robot1.Vp3', 0)
    cimplicity.point_set('Robot1.Vp4', 0)
    cimplicity.point_set('Robot2.Vp1', 0)
    cimplicity.point_set('Robot2.Vp2', 0)
    cimplicity.point_set('Robot2.Vp3', 0)
    cimplicity.point_set('Robot2.Vp4', 0)
    
def move(direction, direction_dic):
    for key, value in direction_dic.items():
        if key == direction:
            cimplicity.point_get(value[0])
            cimplicity.point_get(value[1])
            cimplicity.point_set(value[0], 1)
            cimplicity.point_set(value[1], 0)
    time.sleep(1)

def calculate_positions(coordinate_dic):
    f = open('E:/data.txt', 'r')
    coordinates = f.read()
    f.close()
    ar = []
    num_str = ''
    start_position = 0
    target_position = 0
    for i in coordinates:
        if i.isdigit():
            num_str += i
        elif i.isdigit() == False and num_str != '':
            ar.append(int(num_str))
            num_str = ''
        else:
            num_str = ''
    for key, value in coordinate_dic.items():
        if value[0][0] in list(range(ar[0] - 15, ar[0] + 15)) and value[0][1] in list(range(ar[1] - 15, ar[1] + 15)) and value[1][1] in list(range(ar[3] - 15, ar[3] + 15)) and value[1][2] in list(range(ar[4] - 15, ar[4] + 15)):
            if value[1][0] == ar[2]:
                start_position = key
                print(start_position)
                break
    if start_position == 0:
        print('Объект не найден')

    for key, value in coordinate_dic.items():
        if  value[1][1] in list(range(ar[6] - 15, ar[6] + 15)) and value[1][2] in list(range(ar[7] - 15, ar[7] + 15)):
            if value[1][0] == ar[5]:
                target_position = key
                print(target_position)
                break
    if target_position == 0:
        print('Место перемещения не найдено')

    return start_position, target_position

    
def main_func(direction_dic, coordinate_dic, position_for_coordinate_dic):

    start_position = calculate_positions(coordinate_dic)[0]
    target_position = calculate_positions(coordinate_dic)[1]

    # если объект не надо переносить на другую сторону
    if (start_position in range(1,7) and target_position in range(1,7)) or (start_position in range(8,14) and target_position in range(8,14)):
        for key, value in position_for_coordinate_dic.items():
            if key == start_position and value != []:
                for direction in value:
                    move(direction, direction_dic)
                    

        if start_position in range(1,7):
            move('grab1', direction_dic)
        else:
            move('grab2', direction_dic)

        move_to_initial_position(direction_dic)

        for key, value in position_for_coordinate_dic.items():
            if key == target_position and value != []:
                for direction in value:
                    move(direction, direction_dic)
                    

        if target_position in range(1,7):
            move('release1', direction_dic)
        else:
            move('release2', direction_dic)

        move_to_initial_position(direction_dic)

    # Если объект надо перенести на другую сторону
    else:
        if start_position in range(1,7):
            swap_pos = 7.1
        else:
            swap_pos = 7.2
            
        for key, value in position_for_coordinate_dic.items():
            if key == start_position and value != []:
                for direction in value:
                    move(direction, direction_dic)
                    

        if start_position in range(1,7):
            move('grab1', direction_dic)
        else:
            move('grab2', direction_dic)

        move_to_initial_position(direction_dic)

        for key, value in position_for_coordinate_dic.items():
            if key == swap_pos:
                for direction in value:
                    move(direction, direction_dic)
                    

        if start_position in range(1,7):
            move('release1', direction_dic)
        else:
            move('release2', direction_dic)

        move_to_initial_position(direction_dic)

        if target_position in range(1,7):
            swap_pos = 7.1
        else:
            swap_pos = 7.2

        for key, value in position_for_coordinate_dic.items():
            if key == swap_pos:
                for direction in value:
                    move(direction, direction_dic)
                    

        if target_position in range(1,7):
            move('grab1', direction_dic)
        else:
            move('grab2', direction_dic)

        move_to_initial_position(direction_dic)

        for key, value in position_for_coordinate_dic.items():
            if key == target_position and value != []:
                for direction in value:
                    move(direction, direction_dic)
                    

        if target_position in range(1,7):
            move('release1', direction_dic)
        else:
            move('release2', direction_dic)

        move_to_initial_position(direction_dic)


    

    



if __name__ == "__main__":
    cimplicity.point_get('Robot1.start01')
    cimplicity.point_get('Robot2.start01')
    cimplicity.point_set('Robot1.start01', 1)
    cimplicity.point_set('Robot2.start01', 1)
    # move(direction_dic=direction_dic)
    # calculate_positions(coordinate_dic)
    reset(direction_dic)
    main_func(direction_dic, coordinate_dic, position_for_coordinate_dic,)
    # camera_reset()
    # start_position(direction_dic)
    
