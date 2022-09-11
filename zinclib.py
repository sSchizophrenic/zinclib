import colored, json, asyncio, requests, os, tasksio, time, datetime 
from colored import fg
from os import system, get_terminal_size as tspace
from datetime import datetime   # Why is importing things so ugly in python?

class log(object):
	def ok(content: str):
		lime                  = fg('#2fff00')
		white                 = fg('#fff')
		purple                = fg('#a200ff')
		cyan 				  = fg('#0de7ff')
		ctime                 = datetime.now()
		ctime                 = ctime.strftime("%X")
		status 				  = f"{white}[   {cyan}OK   {white}]"
		time_format           = f"{white}[{purple}{ctime}{white}]  {lime}{content}"
		cols = tspace().columns
		get_content_length = len(content)
		get_status_length  = len(status)
		total = get_content_length + get_status_length - 18
		get_col_spaces = cols - total
		print(time_format + " " * get_col_spaces + status)
		"""< INFO >

		code works - ugly ass code,
		needs to be put into functions as it would look neater.

		 """
	def info(content: str):
		lime                  = fg('#2fff00')
		grey 				  = fg("#baa0a1")
		white                 = fg('#fff')
		purple                = fg('#a200ff')
		cyan 				  = fg('#0de7ff')
		ctime                 = datetime.now()
		ctime                 = ctime.strftime("%X")
		status 				  = f"{white}[  {cyan}INFO  {white}]"
		time_format           = f"{white}[{purple}{ctime}{white}]  {grey}{content}"
		cols = tspace().columns
		get_content_length = len(content)
		get_status_length  = len(status)
		total = get_content_length + get_status_length - 18
		get_col_spaces = cols - total
		print(time_format + " " * get_col_spaces + status)
	

	def error(content: str):
		red 				  = fg('#fa0c14')
		lime                  = fg('#2fff00')
		white                 = fg('#fff')
		purple                = fg('#a200ff')
		cyan 				  = fg('#0de7ff')
		ctime                 = datetime.now()
		ctime                 = ctime.strftime("%X")
		status 				  = f"{white}[  {cyan}ERROR {white}]"
		time_format           = f"{white}[{purple}{ctime}{white}]  {red}{content}"
		cols = tspace().columns
		get_content_length = len(content)
		get_status_length  = len(status)
		total = get_content_length + get_status_length - 18
		get_col_spaces = cols - total
		print(time_format + " " * get_col_spaces + status)

