class sampleCaller:
	def caller(self):
		import calledFile.called
		test = calledFile.called.sampleCalled()
		test.called()

if __name__ == '__main__':
	b = sampleCaller()
	b.caller()