# Worker
The workers will be an environment packed with `conda-pack` and started
by a bat script runs `Scripts\ray.exe start --address=<head-ip>:6379`

Tutorial [gist of Packing Conda Environments](https://gist.github.com/pmbaumgartner/2626ce24adb7f4030c0075d2b35dda32)

We better write it in batch script for Windows and shell script for Linux.

With the packed conda enviornment, we unzip it, added `worker.bat` and
pack it again into `zip`/`7z` for users to start conveniently.
A `start.bat` should be included with hardcoded task server IP for users
to start by one click.