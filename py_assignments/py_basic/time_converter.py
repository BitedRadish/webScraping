def time_converter(seconds):
    hour,res=seconds//3600,seconds%3600
    minutes,second=res//60,res%60

    print(f"{seconds}초는 {hour}시간 {minutes}분 {second}초입니다.")

time_converter(12345)
    