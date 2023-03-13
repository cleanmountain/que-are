from flask import Flask, render_template, request
import numpy as np
from src.qr import QrCode

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/", methods=["GET", "POST"])
def upload_file():
    uploaded_image_filestorage = request.files["file"]
    uploaded_image_bytes = np.fromfile(uploaded_image_filestorage, np.uint8)

    qr = QrCode(uploaded_image_bytes)
    csv: list[list[str]] = qr.decode_qr(print_output=True)

    return csv

# supported files
# Windows bitmaps - *.bmp, *.dib (always supported)
# JPEG files - *.jpeg, *.jpg, *.jpe (see the *Note* section)
# JPEG 2000 files - *.jp2 (see the *Note* section)
# Portable Network Graphics - *.png (see the *Note* section)
# WebP - *.webp (see the *Note* section)
# Portable image format - *.pbm, *.pgm, *.ppm *.pxm, *.pnm (always supported)
# PFM files - *.pfm (see the *Note* section)
# Sun rasters - *.sr, *.ras (always supported)
# TIFF files - *.tiff, *.tif (see the *Note* section)
# OpenEXR Image files - *.exr (see the *Note* section)
# Radiance HDR - *.hdr, *.pic (always supported)
# Raster and Vector geospatial data supported by GDAL (see the *Note* section)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)