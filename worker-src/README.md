# Worker
The workers will be an environment packed with `conda-pack` and started
by a bat script runs `Scripts\ray.exe start --address=<head-ip>:6379`

tutorial [gist of Packing Conda Environments](https://gist.github.com/pmbaumgartner/2626ce24adb7f4030c0075d2b35dda32)

The starting script would be similar to
```py3
import argparse
import subprocess
# import ray

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('head', type=str, help='IP address of task server.')
	args = parser.parse_args()

	subprocess.run(["dev.tar\\Scripts\\ray.exe", "start", "--num-cpus", "1" , f"--address={args.head}:6379"])

	s = ""
	while s.lower() != "stop":
		print('\n\n\n')
		print('Input options:')
		print('"stop" : to disconnect from server and quit the program')
		print('"status" : to list tasks and resources connect to server')
		s = input('> ')
		if s.lower() == 'status':
			subprocess.run(["dev.tar\\Scripts\\ray.exe", "status"])

	subprocess.run(["dev.tar\\Scripts\\ray.exe", "stop"])
```

We better write it in batch script for Windows and shell script for Linux.