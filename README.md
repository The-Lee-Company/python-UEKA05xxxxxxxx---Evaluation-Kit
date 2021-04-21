# python-EK-M-015
This repository contains a Python code snippet library for our Disc Pump Evaluation Kit - EK-M-015.

## Repository contents
* **1s-pulse.py** - Turn the pump on at 1W for 1 second, then turn it off.
* **inflate-and-plot-pressure.py** - Enable and capture the streaming output from the pump. Drive the pump at 1W for 3 seconds, then plot the captured pressure output.
* **power-sine.py** - Send a sequence of target powers to the driver, so that its power output follows a sine-wave
* **pressure-sine.py** - Setup a PID loop on the driver board to control the output pressure. Then send a sequence of target pressures to the board so that the output pressure follows a sine-wave.
* **target-pressure-dial.py** - Setup a PID loop so that the dial controls the target output pressure.
* **target-pressure.py** - Setup a PID loop to control to pressure, and set a target pressure.

## Contact us

For additional support, please visit www.ttpventus.com/support or email the TTP Ventus Support Team at [support@ttpventus.com](mailto:support@ttpventus.com). 

We welcome suggestions for how we can improve and build upin this repository; please feel free to share your ideas, feature requests and any bugs you identify with us using the email address above. 
