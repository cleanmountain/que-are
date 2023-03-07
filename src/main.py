import cv2
from pyzbar.pyzbar import decode
from dataclasses import dataclass


FILEPATH: str = ""


@dataclass
class QrCode:
    """Class for reading and decoding text from QR code from image file"""
    image_path: str

    
    # kinda the "main" method for now
    def decode_qr(self) -> None:
        image_data: list = self.__read_image()

        # temp
        self.__print_image_data(image_data)


    def __read_image(self) -> list:
        image = cv2.imread(self.image_path, 0)
        image_data: list = decode(image)
        return image_data


    def __print_image_data(self, image_data: list) -> None:        
        for data in image_data:
            line: str = data.data.decode("utf-8")
            print(line)


if __name__ == "__main__":
    qr = QrCode(FILEPATH)
    qr.decode_qr()
