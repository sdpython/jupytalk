"""
@file
@brief Record a couple of seconds and returns the raw stream.
"""


def take_picture(filename, size=(640, 480), module="pygame"):
    """
    Take a picture with the camera.

    @param          filename        picture to save
    @param          module          module to use (look at the code).

    We use the examples from
    `Capturing a single image from my webcam in Java or Python <http://stackoverflow.com/questions/11094481/capturing-a-single-image-from-my-webcam-in-java-or-python>`_.
    """

    if module == "pygame":
        import pygame
        import pygame.camera
        pygame.camera.init()
        # pygame.camera.list_camera()
        cam = pygame.camera.Camera(0, size)
        cam.start()
        img = cam.get_image()
        pygame.image.save(img, filename)
    elif module == "cv2":
        from cv2 import VideoCapture, imwrite
        # initialize the camera
        cam = VideoCapture(0)   # 0 -> index of camera
        s, img = cam.read()
        imwrite(filename, img)
    else:
        raise ImportError("No module '{0}'".format(module))
