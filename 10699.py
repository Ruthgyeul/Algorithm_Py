from datetime import datetime, timedelta, timezone

timeZone = timezone(timedelta(hours=9))
timeSet = datetime.now().astimezone(timeZone)
date = timeSet.strftime('%Y-%m-%d')

print(date)
