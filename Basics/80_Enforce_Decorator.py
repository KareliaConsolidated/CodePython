def enforce(*types):
	def decorator(fn):
		def new_func(*args, **kwargs):
			# Converts args into something mutable
			newargs = []
			for (a,t) in zip(args, types):
				newargs.append(t(a))
			return fn(*newargs, **kwargs)
		return new_func
	return decorator

@enforce(str, int)
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

repeat_msg("Hello", "3")

@enforce(float, float)
def divide(a, b):
	return a/b

print(divide('1', '4'))