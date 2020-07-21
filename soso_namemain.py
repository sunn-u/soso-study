# soso_namemain.py 를 직접 실행할 경우에 실행될 함수
def hello():
    print("Hello World!")

# 모듈로서 사용될 경우에 실행될 함수
def bye():
    print("Bye!")

if __name__ == "__main__":
    hello()
else:
    bye()