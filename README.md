#  PicoCalc Micropython Setup

I am finding embedded development to be an infuriating experience.  Thank you to the community for making this barely understandable for my primitive brain.

## Features

* Libraries:
    * `picocalc.py` : Minor updates to `zenodante`'s API.
    * `turtle.py`   : My start of a turtle API for PicoCalc.
* Tools:
    * `keytest.py` :  Script for logging keyboard inputs


## References:

* [zenodante/PicoCalc-micropython-driver](https://github.com/zenodante/PicoCalc-micropython-driver/tree/main)

## Pre-Setup Notes:

* I chose to not use `zenodante`'s approach to compile the core APIs as frozen files.  This makes it impossible to edit them from my laptop after you setup the PicoCalc.

* I instead only keep the `boot.py` and `main.py` from the filesystem variant. Everything else goes into this `./lib` folder.

* I have copies of the files, latest as of 6/13/2025, in my repo.  I modified them a bit, as a few minor parts if his APIs are non-functional. 

* <span style="color:red"><b><u>TODO: Submit PR to his repo!</u></b></span>


## Setup Pico

I duplicated the effort by doing the following:

### 1. Create a folder to hold the workspace

```bash
mkdir workspace
pushd workspace
```

**Note:** The final structure will look like this:

```bash
tree -L 1 ./workspace
./workspace
├── eigenmath_micropython
├── micropython
└── PicoCalc-micropython-driver
```

### 2. Clone `PicoCalc-micropython-driver` repo into workspace folder. 

```bash
git clone git@github.com:zenodante/PicoCalc-micropython-driver.git
pushd PicoCalc-micropython-driver
git remote update --init --recursive
popd
```

### 3. Clone Micropython repo into workspace folder

```bash
git clone git@github.com:micropython/micropython.git
pushd micropython
git remote update --init --recursive
popd
```

### 4. Clone Eigenmath Repo into workspace folder

```bash
git clone git@github.com:zenodante/eigenmath_micropython.git
pushd eigenmath_micropython
git remote update --init --recursive
popd
```

### 5. Setup Micropython build

<span style="color:red"><b><u>TODO: Write instructions</u></b></span>
```bash

```

### 6. Connect Pico 2W to Thonny

### 7. Create /lib folder

On the terminal, run the following shell command on the repl:

```python
import os
os.makedirs('/lib')
```

### 8. Copy Project files

**Note:** I have the Micropython `logging` and `os-path` sources already added to this folder.   You can skip this if you want ot use Micropython's PIP API in Thonny instead.

**Process:** Copy `./lib` to `/lib` on the Pico.

---

## Libraries

### `turtle.py`

This wraps the `picocalc` API and other tools to create a mildly functional version of turtle. 




---

## Tools

### `browser.py`

### `keytest.py`

This is a simple script to log the values of keys pressed.  This can be clutch when you are writing an app and you want to know what a particular key is.  This will print values to the terminal until you press Escape. The escape value will be printed, and the application will exit.

```python
import keytest as kt
kt.run()
```

In this example, I disabled the `p` character so it would register as unknown.  See how unknown characters get returned...

<center>
 <img src='./docs/images/keytest.jpg' width='50%' />
</center>

<span style="color:red"><b><u>TODO:</u></b></span> Use the turtle display API to allow taking screenshots.

