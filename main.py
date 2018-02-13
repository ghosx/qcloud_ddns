from ddns import *

def main():
	ddns=DDNS("LOGIN_ID","LOGIN_TOKEN")
	ddns.update()

if __name__ == '__main__':
	main()
