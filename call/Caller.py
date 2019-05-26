class sampleCaller:
	def caller(self):
		import calledFile.Called
		test = calledFile.Called.sampleCalled()
		test.called()

if __name__ == '__main__':
	b = sampleCaller()
	b.caller()