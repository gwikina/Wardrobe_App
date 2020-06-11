"""
Author: Gideon Wikina
Date: 6/11/2020
Language: Python
"""
import os
import random

import tkinter as tk
from PIL import Image, ImageTk

# change any of these constants to style and make it your own!
WINDOW_TITLE = 'Giddy Clothing Services'
WINDOW_WIDTH = 220
WINDOW_HEIGHT = 700
IMG_HEIGHT = 200
IMG_WIDTH = 200
BEIGE_COLOR_HEX = '#f2f2f2'

# dynamically open folders and make a list, while ignoring any hidden files that start with "."
ALL_TOPS = [str("tops/") + file for file in os.listdir("tops/") if not file.startswith('.')]
ALL_BOTTOMS = [str("bottoms/") + file for file in os.listdir("bottoms/") if not file.startswith('.')]
ALL_SHOES = [str("shoes/") + file for file in os.listdir("shoes/") if not file.startswith('.')]


class WardrobeApp:

    def __init__(self, root):
        """
        Method intends to initialize the scene for the GUI.
        Here colors, frames, roots, buttons, and images are set up in order to give the program life.

        :return: none
        """
        self.root = root

        # defines a collection of all clothing items
        self.top_images = ALL_TOPS
        self.bottom_images = ALL_BOTTOMS
        self.shoe_images = ALL_SHOES

        # first pictures for tops, bottoms, and shoes
        self.tops_image_path = self.top_images[0]
        self.bottom_image_path = self.bottom_images[0]
        self.shoe_image_path = self.shoe_images[0]

        # creates three frames for the GUI
        self.tops_frame = tk.Frame(self.root, bg=BEIGE_COLOR_HEX)
        self.bottoms_frame = tk.Frame(self.root, bg=BEIGE_COLOR_HEX)
        self.shoe_frame = tk.Frame(self.root, bg=BEIGE_COLOR_HEX)

        # adding top to the screen
        self.top_image_label = self.create_photo(self.tops_image_path, self.tops_frame)
        self.top_image_label.pack(side=tk.TOP)

        # adding bottom to the screen
        self.bottom_image_label = self.create_photo(self.bottom_image_path, self.bottoms_frame)
        self.bottom_image_label.pack(side=tk.TOP)

        # adding shoes to the screen
        self.shoe_image_label = self.create_photo(self.shoe_image_path, self.shoe_frame)
        self.shoe_image_label.pack(side=tk.TOP)

        self.create_background()

    def create_background(self):
        """
        Creates objects such as buttons, modifies the window's information along with its dimensions, and
        packs the frames in order to populate the background.

        :return: none
        """
        # title and resize the window
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))

        # create buttons
        self.create_buttons()

        # add the initial clothes onto the screen
        self.tops_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.bottoms_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.shoe_frame.pack(fill=tk.BOTH, expand=tk.YES)

    def create_buttons(self):
        """
        Initializes and creates all the buttons that will be used in this GUI

        :return: none
        """
        # initializes previous button for the tops
        top_prev_button = tk.Button(self.tops_frame, text="Prev", command=self.get_prev_top)
        top_prev_button.pack(side=tk.LEFT)

        # initializes create outfit button
        create_outfit_button = tk.Button(self.tops_frame, text="Create Outfit", command=self.create_outfit)
        create_outfit_button.pack(side=tk.LEFT)

        # initializes next button for the tops
        top_next_button = tk.Button(self.tops_frame, text="Next", command=self.get_next_top)
        top_next_button.pack(side=tk.RIGHT)

        # initializes previous button for the bottoms
        bottom_prev_button = tk.Button(self.bottoms_frame, text="Prev", command=self.get_prev_bottom)
        bottom_prev_button.pack(side=tk.LEFT)

        # initializes next button for the bottoms
        bottom_next_button = tk.Button(self.bottoms_frame, text="Next", command=self.get_next_bottom)
        bottom_next_button.pack(side=tk.RIGHT)

        # initializes previous button for the shoes
        shoe_prev_button = tk.Button(self.shoe_frame, text="Prev", command=self.get_prev_shoe)
        shoe_prev_button.pack(side=tk.LEFT)

        # initializes next button for the shoes
        shoe_next_button = tk.Button(self.shoe_frame, text="Next", command=self.get_next_shoe)
        shoe_next_button.pack(side=tk.RIGHT)

    def create_photo(self, image, frame):
        """
        :param image: the image that will be resized and formatted
        :param frame: the frame (1-3) that the image will be categorized in
        :return: image_label, the label used to describe the image
        """
        top_image_file = Image.open(image)
        image = top_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo, anchor=tk.CENTER)
        image_label.image = photo

        return image_label

    def update_photo(self, new_image, image_label):
        """
        The size of the new image is adjusted and this new photo is configured
        :param new_image: the image that is in question (next or previous image in the list)
        :param image_label: the label used the describe the image
        :return: none
        """
        new_image_file = Image.open(new_image)
        image = new_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo

    def _get_next_item(self, current_item, category, increment=True):
        """ Gets the Next Item In a Category depending on if you hit next or prev
        Args:
            current_item, str
            category, list
            increment, boolean
        """
        item_index = category.index(current_item)
        final_index = len(category) - 1
        next_index = 0

        if increment and item_index == final_index:
            next_index = 0  # cycle back to the beginning
        elif not increment and item_index == 0:
            next_index = final_index  # cycle back to the end
        else:
            incrementor = 1 if increment else -1
            next_index = item_index + incrementor

        next_image = category[next_index]

        # reset the image object
        if current_item in self.top_images:
            image_label = self.top_image_label
            self.tops_image_path = next_image
        elif current_item in self.bottom_images:
            image_label = self.bottom_image_label
            self.bottom_image_path = next_image
        else:
            image_label = self.shoe_image_label
            self.shoe_image_path = next_image

        # update the photo
        self.update_photo(next_image, image_label)

    def get_next_top(self):
        """
        Increment the index of the ALL_TOPS' list, revealing the next photo in the
        list.
        :return: none
        """
        self._get_next_item(self.tops_image_path, self.top_images, increment=True)

    def get_prev_top(self):
        """
        Decrement the index of the ALL_TOPS' list, revealing the previous photo in the
        list.
        :return: none
        """
        self._get_next_item(self.tops_image_path, self.top_images, increment=False)

    def get_prev_bottom(self):
        """
        Decrement the index of the ALL_BOTTOMS' list, revealing the previous photo in the
        list.
        :return: none
        """
        self._get_next_item(self.bottom_image_path, self.bottom_images, increment=False)

    def get_next_bottom(self):
        """
        Increment the index of the ALL_BOTTOMS' list, revealing the next photo in the
        list.
        :return: none
        """
        self._get_next_item(self.bottom_image_path, self.bottom_images, increment=True)

    def get_prev_shoe(self):
        """
        Decrement the index of the ALL_SHOES' list, revealing the previous photo in the
        list.
        :return: none
        """
        self._get_next_item(self.shoe_image_path, self.shoe_images, increment=False)

    def get_next_shoe(self):
        """
        Increment the index of the ALL_SHOES' list, revealing the next photo in the
        list.
        :return: none
        """
        self._get_next_item(self.shoe_image_path, self.shoe_images, increment=True)

    def create_outfit(self):
        """
        Randomizes the clothes in all 3 frames in order to generate a random outfit
        :return: none
        """
        # randomly select an outfit
        new_top_index = random.randint(0, len(self.top_images)-1)
        new_bottom_index = random.randint(0, len(self.bottom_images)-1)
        new_shoe_index = random.randint(0, len(self.bottom_images) - 1)

        # add the clothes onto the screen
        self.update_photo(self.top_images[new_top_index], self.top_image_label)
        self.update_photo(self.bottom_images[new_bottom_index], self.bottom_image_label)
        self.update_photo(self.shoe_images[new_shoe_index], self.shoe_image_label)


if __name__ == '__main__':
    root = tk.Tk()
    app = WardrobeApp(root)

    root.mainloop()