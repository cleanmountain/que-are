from __future__ import annotations
import cv2
import csv
import numpy as np
from pyzbar.pyzbar import decode
from dataclasses import dataclass


PATH: str = ""
FILEPATH: str = PATH + ""


@dataclass
class QrCode:
    """Class for reading and decoding text from QR code from image file"""
    image_path: str

    
    # kinda the "main" method for now
    def decode_qr(self) -> None:
        image_data: np.ndarray = self.__read_image()
        decoded_image_data: list = self.__decode_image(image_data)

        # temp
        self.__print_image_data(decoded_image_data)

        return decoded_image_data


    def __read_image(self) -> np.ndarray:
        image = cv2.imread(self.image_path, 0)
        return image
    

    def __decode_image(self, image_data: np.ndarray) -> list:
        image_data: list = decode(image_data)
        return image_data


    def __print_image_data(self, decoded_image_data: list) -> None:        
        for data in decoded_image_data:
            line: str = data.data.decode("utf-8")
            print(line)


if __name__ == "__main__":
    qr = QrCode(FILEPATH)
    qr.decode_qr()
