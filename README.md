# Publicardo

Batch image processing tool before image publication in the internet.

### General requirements
touch
* Resize images proportionally
* Decide which EXIF and IPTC info should be present in final file
* Add watermark
* Pick from different watermark styles and watermark texts
* GUI for Windows and Mac


### TODO

* Use shelf (http://docs.python.org/library/shelve.html) lib to store user data
* Support not only JPG files

### Internal

Libs save command: pip freeze > requirements.txt
Libs load command: pip install -r requirements.txt