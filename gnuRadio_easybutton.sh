#!/usr/bin/bash
#Make sure the dependencies has been satisfied. Please go through this http://gnuradio.org/doc/doxygen/build_guide.html

apt-get install gnuradio libgnuradio-dev cmake libusb-1.0-0-dev libpulse-dev gnuradio-companion

#The install shell script assumes the gnuradio modules to be already available in your aptitude repository.
#However, this may not always be true. Then uncomment the script below
wget http://www.sbrac.org/files/build-gnuradio && chmod a+x ./build-gnuradio && ./build-gnuradio

#Warning: This script is quite out of date and I have just merged 2 one line commands. Would seem better to manually try.
