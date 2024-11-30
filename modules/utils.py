def resolve_source(source):
	try:
		return int(source)
	except Exception:
		return source
