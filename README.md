# Distributed-PM-Predict
A fork of [Project-PM-Predict](https://github.com/NewJerseyStyle/Project-PM-Predict) but faster
crawling with distributed workers.

I plan to build it in server-client architecture with RESTful APIs.
- Each worker will ask if server has any data is out dated. Worker will then crawl and analysis,
return crawling timestamp and analysis result to server.
  - A heartbeat API and a update API will be implemented for worker to receive connection from
  server.
  - A Graphic in CLI will be implemented to display the crawling tasks and its progress, also
  the latest conclusion update from server.
- Server will manage the database of data index and timestamp, worker list and their duties.
  - A task list API will be implemented for server to announce tasks needs to be finished.
  - A update API will be implemented for server to receive analysis result from workers.
  - A Graphic in CLI will be implemented to display the worker list and the current conclusion.
  - The server shall start a worker process on the machine.
