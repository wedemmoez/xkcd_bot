# xkcd-bot
### For use with Cisco Spark


#### Usage Examples
xkcd-bot has no functions to call the date and time, it must be invoked from
a crontab or task scheduler to run. Because of this, there is no functionality to
respond to messages targeted at xkcd-bot inside of the Cisco Spark application.

At the top of the file are helper functions to format the calls to the REST API.

It will pull information for all rooms that it is in and post the same XKCD comic to all rooms that it is in.

#### Crontab
the crontab configuration included is what we chose to run within our organization. Since a new XKCD comic is posted on Mondays, Wednesdays, and Fridays, the bot will post the latest comic on those days. For Tuesdays and Thursdays, the bot will post a random comic using the the random function to select a comic between 0 and the number of the current comic.

#### Contact  
For questions about the code please create an Issue. 

#### License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

For more information, please refer to <http://unlicense.org/>
