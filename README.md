# Distributed-PM-Predict
A fork of [Project-PM-Predict](https://github.com/NewJerseyStyle/Project-PM-Predict) but faster
crawling with distributed workers.

Some problem when setting up the server, troubleshoot with: 
[Troubleshoot on Linux server/Docker](https://github.com/NewJerseyStyle/Project-PM-Predict#troubleshoot)

In case cannot identify the problem, turn on debug mode of Pyppeteer with
[rederence](https://github.com/miyakogi/pyppeteer/issues/122)
```bash
pip install -U git+https://github.com/pyppeteer/pyppeteer@dev
```
> :warning: The link in `reference` is incorrect.
[The link to latest repository](https://stackoverflow.com/questions/69257248/module-websockets-has-no-attribute-client)

```py3
import logging
logging.getLogger('pyppeteer').setLevel(logging.DEBUG)
```

The system now split into two parts:
1. A Ray remote function for workers download data and analysis data to produce supportness
	The remote function will be executed by worker
	(packed conda environment with a starting script)
	distributed among volunteers contributing their computer to the project.
2. A Python script serve as Ray server and collect analysis result of each workers to
produce conclusion.
