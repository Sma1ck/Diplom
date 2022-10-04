# Untitled - By: apci.student - Чт июн 16 2022

import sensor, image, time, pyb, math

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking

clock = time.clock()

red = (30, 100, 15, 127, 15, 127)
green = (45, 128, -10, 5, 25, 45)
blue = (40, 80, -10, 15, -57, -33)
thresholds = [red, green, blue]

place = [0, 0, 0]

while(True):
    clock.tick()
    img = sensor.snapshot()

    r = (pyb.rng() % 127) + 128
    g = (pyb.rng() % 127) + 128
    b = (pyb.rng() % 127) + 128


    for i in range(len(thresholds)):
        try:
            for blob in img.find_blobs([thresholds[i]], pixels_threshold=200, area_threshold=100):
                # These values depend on the blob not being circular - otherwise they will be shaky.
                if blob.elongation() > 0.5:
                    img.draw_edges(blob.min_corners(), color=(255,0,0))
                    img.draw_line(blob.major_axis_line(), color=(0,255,0))
                    img.draw_line(blob.minor_axis_line(), color=(0,0,255))
                # These values are stable all the time.
                img.draw_rectangle(blob.rect())
                img.draw_cross(blob.cx(), blob.cy())
                # Note - the blob rotation is unique to 0-180 only.
                img.draw_keypoints([(blob.cx(), blob.cy(), int(math.degrees(blob.rotation())))], size=20)
                if thresholds[i] == (30, 100, 15, 127, 15, 127):
                    place[0] = [blob[0], blob[1]]
                if thresholds[i] == (45, 128, -10, 5, 25, 45) and math.fabs(blob[1] - place[0][1]) < 50 and math.fabs(blob[0] - place[0][0]) < 50:
                    place[1] = [1, blob[0], blob[1]]
                if thresholds[i] == (40, 80, -10, 15, -57, -33) and math.fabs(blob[1] - place[0][1]) < 30 and math.fabs(blob[0] - place[0][0]) < 30:
                    place[1] = [2,  blob[0], blob[1]]
                elif thresholds[i] != (30, 100, 15, 127, 15, 127):
                    if thresholds[i] == (45, 128, -10, 5, 25, 45):
                        place[2] = [1, blob[0], blob[1]]
                    if thresholds[i] == (40, 80, -10, 15, -57, -33):
                        place[2] = [2,  blob[0], blob[1]]
        except TypeError:
            place = [[2,110], 0, 0]



    if (place[0] != 0 and place[1] != 0 and place[2] != 0):
       print(place)
       data = str(place)
       with open('data.txt', 'w') as f:
        f.write(data)
       break

