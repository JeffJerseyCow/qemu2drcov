# qemu2drcov
This tool contains a patch to QEMU which adds basic block size to the output of its debugging information, a bug fix to the IDA lighthouse plugin and a converter from the QEMU format to drcov.

## Usage
1. ```git clone https://github.com/qemu/qemu.git```
2. ```git clone https://github.com/JeffJerseyCow/qemu2drcov.git```
3. From the QEMU directory ```git apply ../qemu2drcov/patch/qemu.diff```
4. ```./configure && make && make install```
5. From the qemu2drcov directory ```pip3 install . --upgrade .```
6. Run any binary under the appropriate qemu instance -- this method works with 32bit and 64bit for any architecture
  - ```qemu-x86 -d page,exec -- /bin/ls 2>&1 | qemu2drcov -n ls > ls.drcov.trace```

~Note that statically compiled binaries only work with the patched version of lighthouse in this project~

