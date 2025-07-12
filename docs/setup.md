# Setup MicroPython


## Pre-Setup Notes:

* I chose to not use `zenodante`'s approach to compile the core APIs as frozen files.  This makes it impossible to edit them from my laptop after you setup the PicoCalc.
    * For newbies like me, `frozen` files are Python sources you `compile` into bytecode.  This makes them exist in the filesystem, but not using the built-in filesystem.  Aka:  Consider it a *magical* filesystem.

* I instead only keep the `boot.py` and `main.py` from the filesystem variant. Everything else goes into this `./lib` folder.

* I have copies of the files, latest as of 6/13/2025, in my repo.  I modified them a bit, as a few minor parts if his APIs are non-functional.

* <span style="color:red"><b><u>TODO: Submit PR to zenodante's repo with relvent changes!</u></b></span>


## Setup Pico

<span style="color:red"><b><u>TODO: Make these dependencies submodules</u></b></span>

I duplicated the effort by doing the following steps:

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
├── micropython-ulab
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

### 4. Clone Micropython-ULAB repo into workspace folder

```bash
git clone git@github.com:v923z/micropython-ulab.git
```


### 5. Clone Eigenmath Repo into workspace folder

```bash
git clone git@github.com:zenodante/eigenmath_micropython.git
pushd eigenmath_micropython
git remote update --init --recursive
popd
```

### 6. Setup Micropython build

<span style="color:red"><b><u>TODO: Cleanup Script!</u></b></span>

```bash
pushd micropython/ports/rp2
mkdir build
pushd build

# Where you cloned this repo, where this README lives
cp <repo-path>/scripts/build-micropython.sh .
./build-micropython

# Go back to workspace folder
popd
popd
```

### 7. Connect Pico 2W to Thonny


### 8. Create /lib folder

On the terminal, run the following shell command on the repl:

```python
import os
os.makedirs('/lib')
```

### 9. Copy Project files

**Note:** I have the Micropython `logging` and `os-path` sources already added to this folder.   You can skip this if you want ot use Micropython's PIP API in Thonny instead.

**Process:** Copy `./lib` to `/lib` on the Pico.

### 10. Setup WebREPL Server

On the device, enter the following command to setup the WebREPL server.

```python
import webrepl_setup
```