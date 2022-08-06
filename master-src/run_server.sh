pip install -r requirements.txt
ray start --num-cpus 1 --head
python server.py --loop
