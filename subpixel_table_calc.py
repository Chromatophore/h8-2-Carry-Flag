
import math
import pprint

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def chunk_print(lst, n):
	l = chunks(lst, n)
	x = 0
	for i in l:
		s = "\t"
		a = x + len(i)
		s = s + ' '.join(i) + " # %d - %d " % (x, a - 1)
		x = a
		print(s)


o = []
print("# Mag table")
print(": mag_table")
for y in range (128):
#	if (y % 8) == 0 and y != 0:
#		o.append("\n")
	o.append("0x%02X" % y)
	#o.append(str(y))

for y in range(128):
#	if (y % 8) == 0 and y != 0:
#		o.append("\n")
	o.append("0x%02X" % (128 - y))
	#o.append(str(128 - y))

chunk_print(o, 8)

subs = []

o = []
print()
print("# Flip Table")
print(": Flip_Table")
for y in range(128):
	o.append(str(-y))
for y in range(128):
	o.append(str(128 - y))

chunk_print(o, 16)

print()
print()
print(":calc table_subpixel_start { HERE }")


for y in range(64):
	subs.clear()
	print("# %d" % y)
	for x in range(64):

		if x < y:
			subpx = 0
			if x != 0:
				subpx = math.ceil((256 * x) / y)
				# subpx = x / y
			subs.append("0x%02X" % subpx)
			#  print("\t%s # %d" % (hex(subpx), x) )
		# else:
		# 	print("\t0 # dummy value to be removed")
	chunk_print(subs, 16)


print("")
print("# Length Table")
print(":calc table_llength_start { HERE }")

print("# We have 3 bytes per entry")

# For each 'on axis values'
for y in range(64):
	subs.clear()

	# For each 'off axis' value
	print("# %d (length)" % y)
	highest_x = 0
	for x in range(66):

		if x <= (y + 2):

			# An entry in this list should be:
			# index X in list Y should be:
			# Reduce X by 1, and Reduce Y by 1
			# Reduce X by 1, and keep Y the same
			# Reduce X by 1, and Increase Y by 1
			# This way by reading up to 2 entries ahead, we get the full compliment

			subpx = 0
			a = x - 1
			b = x + 1

			l = y - 1
			m = y + 1

			scaler = 2.75

			subpx = math.ceil(scaler * math.pow((a * a) + (l * l),0.5))
			subs.append("0x%02X" % subpx)

			subpx = math.ceil(scaler * math.pow((a * a) + (y * y),0.5))
			subs.append("0x%02X" % subpx)

			subpx = math.ceil(scaler * math.pow((a * a) + (m * m),0.5))
			subs.append("0x%02X" % subpx)


				# subpx = x / y
			
			#  print("\t%s # %d" % (hex(subpx), x) )
		# else:
		# 	print("\t0 # dummy value to be removed")

	chunk_print(subs, 18)