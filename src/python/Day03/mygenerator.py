from sys import stderr as err

class MyError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
print(MyError(Exception))