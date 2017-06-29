# xkcd-bot
### For use with Cisco Spark


##### Usage Examples
xkcd-bot has no functions to call the date and time, it must be invoked from
a crontab or task scheduler to run. Because of this, there is no functionality to
respond to messages targeted at xkcd-bot inside of the Cisco Spark application.

At the top of the file are helper functions to format the calls to the REST API.

It will pull information for all rooms that it is in and post the same XKCD comic to all rooms that it is in.