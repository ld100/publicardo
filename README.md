# Publicardo

Batch image processing tool before image publication in the internet.
Features:

* Resize images proportionally
* Preserves EXIF information
* Adds beautiful non-disturbing watermark
* Works on Mac, Linux and Windows


### Installation

Clone git repository, run:
`make init`

### Usage

Copy source jpegs to 'source' folder. Edit watermark text/font and desired
image sizes in config/settings.yml. Run:
`make process`

And get watermarked resized versions of photos in 'destination' folder.

Run `make clean` to clean up 'destination' directory and any unneeded caches.

### TODO

* Support not only JPG files
* Pick from different watermark styles and watermark texts
* GUI for Windows and Mac

### Internal Dev Info

Libs save command: `pip freeze > requirements.txt` or `make freeze`
Libs load command: `pip install -r requirements.txt`
