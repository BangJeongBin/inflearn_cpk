import time

# 타이머 함수 (분 단위로 받음)
def start_timer(minutes, message):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # 분, 초 계산
        timer_display = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ {timer_display}", end="")  # 같은 줄에서 시간 갱신
        time.sleep(1)
        seconds -= 1
    print(f"\n✅ {message}")  # 타이머 종료 후 알림 메시지 출력


def pomodoro_cycle():
    focus_time = 25  # 집중 25분
    short_break = 5  # 짧은 휴식 5분
    long_break = 15  # 긴 휴식 15분

    cycle_count = 4  # 4번 반복

    for i in range(1, cycle_count + 1):
        print(f"\n=== 집중 세션 {i} 시작! ===")
        start_timer(focus_time, "집중 시간 종료! 잠깐 휴식하세요.")

        if i < cycle_count:  # 마지막 사이클 전까진 짧은 휴식
            print(f"\n=== 짧은 휴식 {i} 시작! ===")
            start_timer(short_break, "짧은 휴식 종료! 다시 집중 시작!")
        else:  # 마지막 사이클 후엔 긴 휴식
            print("\n=== 긴 휴식 시작! ===")
            start_timer(long_break, "긴 휴식 종료! 오늘도 수고하셨습니다!")


if __name__ == "__main__":
    input("🎯 포모도로 타이머를 시작하려면 Enter 키를 누르세요...")
    pomodoro_cycle()
