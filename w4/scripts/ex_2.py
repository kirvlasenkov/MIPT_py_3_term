import sys
import platform 

print("version is ", sys.version)
print("OS core is ", sys.platform)

# or with using platform:
print("system name is", platform.system(), 
		"with release version", platform.release())