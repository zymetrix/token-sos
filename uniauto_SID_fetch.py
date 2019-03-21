# 
from webbot import Browser
import time

sos_login = "IzaEne14427"
sos_pwd = "UniTest99"
sos_system_url = "https://test146.unilink.pl/system"
uniauto_url = "http://ns01131-dev.noma.lan/?sid="
# if true, only SOS ID is returned, if false browser window is opened for manual user testing
quiet_mode = False

TEXT_NORMAL = "\033[0;37;40m"
TEXT_WAITING = "\033[;0;32;40m"
TEXT_SID = "\033[;0;31;40m"

print(TEXT_NORMAL + "Creating browser process")
browser = Browser(showWindow = not quiet_mode)
browser.go_to("https://test146.unilink.pl/logowanie/")
print("Logging to SOS as " + sos_login)
browser.type(sos_login, into = "login")
browser.type(sos_pwd, into = "password")
browser.click("Zaloguj", id = "submit")

current_url = browser.get_current_url()
print(f"Current URL is {current_url} ")
print("Waiting for SOS main page")

# Wait until user is redirected to SOS
while current_url != sos_system_url:
	print(TEXT_WAITING + "Waiting..." + TEXT_NORMAL)
	time.sleep(1)
	current_url = browser.get_current_url()

print(TEXT_NORMAL + "Page loaded. Navigating to Uniauto menu...")
browser.click("Obsługa")
browser.click("Kalkulatory/Produkty")
browser.click("Dostęp do sprzedaży")
browser.click("UniAuto")

print("Switching to Uniauto tab...")
browser.switch_to_tab(2);

current_url = browser.get_current_url()
print(f"Current URL is {current_url} ")
assumed_sid = current_url[-40::]
print("SID = " + TEXT_SID + assumed_sid + TEXT_NORMAL)


if quiet_mode == False:
# Wait until DEV server is open and close SOS tab otherwise close browser process
	print("Opening dev server...")
	time.sleep(5)
	browser.go_to(uniauto_url+ assumed_sid)
	print("Done.")
	browser.switch_to_tab(1)
	browser.close_current_tab()
else:
	print("Closing browser process.")
	browser.quit()

