import time
import os.path

# timer for speed testing of program logic
def run_timer():
	tests = 30
	start_time = time.time() # start
	for i in xrange(tests):
		run_tests()
	end_time = time.time()
	total_time = (end_time - start_time) / tests # end
	print("Runtime: %.10f seconds" % total_time)
	# save results
	file_name = "speed.csv"
	if os.path.isfile(file_name) is False:
		with open(file_name, "a") as results:
			results.write("time,tests\n")
	with open(file_name, "a") as results:
		results.write("%.10f" % total_time)
		results.write(",%s\n" % tests)

# program logic
def base(the_input):
	return the_input

# test cases
def run_tests():
	print base('hello world')

run_tests()
# run_timer()
