from ddns import *

def main():
	ddns=Ddns("LOGIN_ID","LOGIN_TOKEN")
	ddns.update()

if __name__ == '__main__':
	main()