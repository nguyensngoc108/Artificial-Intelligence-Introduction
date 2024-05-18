# check the platform of the system(kiem tra platform minh dang xai)
import platform

system = platform.system()

if system == "Darwin":
    print("You are using macOS")
elif system == "Windows":
    print("You are using Windows")
elif system == "Linux":
    print("You are using Linux")
else:
    print("Unknown platform")
