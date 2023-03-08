from __future__ import annotations
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from dataclasses import dataclass

# temporary
PATH: str = "x"
FILEPATH: str = PATH + "samplecsv-qr.png"


@dataclass
class QrCode:
    """Class for reading and decoding CSV from QR code from image file"""
    image_path: str

    
    # kinda the "main" method for now
    def decode_qr(self, print_output: bool = False, replace_empty_with: str = "NONE") -> None:
        raw_image_data: np.ndarray = self.__read_image()
        qr_data: list = self.__decode_qr(raw_image_data)
        useful_qr_data: list = self.__extract_useful_qr_data(qr_data)
        parsed_csv: list[list[str]] = self.__parse_csv(useful_qr_data, replace_empty_with)

        if print_output:
            self.__print_qr_data(useful_qr_data)

        return parsed_csv


    def __parse_csv(self, useful_image_data: list, replace_empty_with: str) -> list[list[str]]:
        output: list = []

        for line in useful_image_data:
            line_data: list = line.split(",")
            line_data = self.__replace_empty_elements(line_data, replace_empty_with)
            output.append(line_data)

        return output


    def __read_image(self) -> np.ndarray:
        image = cv2.imread(self.image_path, 0)
        return image


    def __decode_qr(self, image_data: np.ndarray) -> list:
        image_data: list = decode(image_data)
        return image_data


    def __extract_useful_qr_data(self, decoded_image_data: list) -> None:
        return decoded_image_data[0].data.decode("utf-8").split("\n")


    def __print_qr_data(self, image_data: list) -> None:        
        for line in image_data:
            print(line)


    def __replace_empty_elements(self, line_data: list, replace_empty_with: str) -> list:
        return [replace_empty_with if not element else element for element in line_data]


if __name__ == "__main__":
    qr = QrCode(FILEPATH)
    qr.decode_qr()
