import pygame

pygame.init()
running = True

joysticks = []

for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print("Detected joystick '" + joysticks[-1].get_name() + "'")

while True:
    for event in pygame.event.get():
        # buttons, bumpers, and menu/view buttons
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                # a button
                print('a')
            if event.button == 1:
                # b button
                print('b')
            if event.button == 2:
                # x button
                print('x')
            if event.button == 3:
                # y button
                print('y')
            if event.button == 4:
                # left bumper
                print('LB')
            if event.button == 5:
                # right bumper
                print('RB')
            if event.button == 6:
                # view button
                print('View')
            if event.button == 7:
                # menu button
                print('Menu')
            if event.button == 8:
                # left joystick button
                print('LJB')
            if event.button == 9:
                # right joystick button
                print('RJB')

        # D-pad
        if event.type == pygame.JOYHATMOTION:
            if event.value[0] == 1:
                # right d-pad
                print('RDP')
            if event.value[0] == -1:
                # left d-pad
                print('LDP')
            if event.value[1] == 1:
                # up d-pad
                print('UDP')
            if event.value[1] == -1:
                # down d-pad
                print('DDP')

        # triggers and joystick
        if event.type == pygame.JOYAXISMOTION:
        #there was trouble mapping the joysticks, but included is the basics
            '''if event.axis == 0:
                #vertical movement on left joystick
                print('Vertical left')
            if event.axis == 1:
                #horizontal on left joystick
                print('Horizontal left')
            if event.axis == 2:
                #right on right joystick
                print('Horizontal right')
            if event.axis == 3:
                #horizontal movement right joystick
                print('Vertical right')'''
            if event.axis == 4:
                # left trigger
                print('Lt')
            if event.axis == 5:
                # right trigger
                print('RT')

pygame.quit()
