# Disc pump Eval kit Python control - UEKA05xxxxxxxx
This repository contains a Python code snippet library for The Lee Company Disc Pump Evaluation Kit - UEKA05xxxxxxxx (previously EK-M-015).

## Repository contents
* **1s-pulse.py** - Turn the pump on at 1W for 1 second, then turn it off.
* **inflate-and-plot-pressure.py** - Enable and capture the streaming output from the pump. Drive the pump at 1W for 3 seconds, then plot the captured pressure output.
* **power-sine.py** - Send a sequence of target powers to the driver, so that its power output follows a sine-wave
* **pressure-sine.py** - Setup a PID loop on the driver board to control the output pressure. Then send a sequence of target pressures to the board so that the output pressure follows a sine-wave.
* **target-pressure-dial.py** - Setup a PID loop so that the dial controls the target output pressure.
* **target-pressure.py** - Setup a PID loop to control to pressure, and set a target pressure.

**Take note of the libraries dependencies in each script. Please ensure you have the relevant libraries installed. For setting up a python environment you can visit https://www.jetbrains.com/help/pycharm/getting-started.html**

## Contact us

For additional support, please visit https://www.theleeco.com/contact/ or you can call our Technical Support Line on 1-800-LEE-PLUG.

We welcome suggestions for how we can improve and build upon this repository; please feel free to share your ideas, feature requests and any bugs you identify with us using the email address above. 

## DISCLAIMER 
These Python demos are provided "as is" and without any warranty of any kind, and their use is at your own risk. LEE Ventus does not warrant the performance or results that you may obtain by using these Arduino demos. LEE Ventus makes no warranties regarding these Arduino demos, express or implied, including as to non-infringement, merchantability, or fitness for any particular purpose. To the maximum extent permitted by law LEE Ventus disclaims liability for any loss or damage resulting from use of these Arduino demos, whether arising under contract, tort (including negligence), strict liability, or otherwise, and whether direct, consequential, indirect, or otherwise, even if LEE Ventus has been advised of the possibility of such damages, or for any claim from any third party.
