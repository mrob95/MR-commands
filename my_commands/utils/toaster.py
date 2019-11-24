from win10toast import ToastNotifier
import sys

def notify(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title=title,
                        msg=message,
                        duration=10)

notify(sys.argv[1], sys.argv[2])