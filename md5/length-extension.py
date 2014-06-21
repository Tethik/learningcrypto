import md5py
import struct

def hexdump(s):
	for b in xrange(0, len(s), 16):
		lin = [c for c in s[b : b + 16]]
		#~ if sum([ord(l) for l in lin]) == 0:
			#~ continue
		hxdat = ' '.join('%02X' % ord(c) for c in lin)
		pdat = ''.join((c if 32 <= ord(c) <= 126 else '.' )for c in lin)
		print('  %04x: %-48s %s' % (b, hxdat, pdat))
	print

secret = b"secret"
original = b"data"
append = b"append"

def pad(s):
	padlen = 64 - ((len(s) + 8) % 64)
	bit_len = 8*len(s)
	if(padlen < 64):
		s += '\x80' + '\000' * (padlen - 1)
	return s + struct.pack('<q', bit_len)

val = md5py.new(secret+original)
print "Original payload:", val.hexdigest()

payload = pad(secret+original)+append
hexdump(payload)

legit = md5py.new(payload)
print "Legit digest:", legit.hexdigest()

not_legit = md5py.new("A"*64)
not_legit.A, not_legit.B, not_legit.C, not_legit.D = md5py._bytelist2long(val.digest())
not_legit.update(append)
print "Illicit digest:", not_legit.hexdigest()

if legit.hexdigest() == not_legit.hexdigest():
	print "Success!"
else:
	print "Fail!"
