#include <fstream>
#include <sstream>
#include "AnalogIn.h"

#define ADC_PATH "/sys/bus/iio/devices/iio:device0/in_voltage"

using namespace std;

AnalogIn::AnalogIn() {
}

AnalogIn::AnalogIn(unsigned int n) {
  number = n;
}

// getNumber already implemented in AnalogIn.h

void AnalogIn::setNumber(unsigned int n) {
  number = n;
}

int AnalogIn::readAdcSample() {
  int reading;
  stringstream ss;
  ss << ADC_PATH << number << "_raw";
  
  fstream fs;
  fs.open(ss.str().c_str(), fstream::in);
  fs >> reading;
  fs.close();

  return reading;
}

AnalogIn::~AnalogIn() {
}
