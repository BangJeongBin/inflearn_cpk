import random

def up_and_down_game():
    # 1~100 사이에서 컴퓨터가 무작위 숫자를 선택
    answer = random.randint(1, 100)
    attempts = 0  # 시도 횟수 기록

    print("🎮 업앤다운 게임을 시작합니다!")
    print("1부터 100 사이의 숫자를 맞혀보세요.")

    while True:
        try:
            guess = int(input("👉 숫자를 입력하세요: "))  # 사용자 입력
            attempts += 1  # 시도 횟수 증가

            # 범위 검사
            if guess < 1 or guess > 100:
                print("⚠️ 1~100 사이의 숫자를 입력하세요.")
                continue

            # 정답 비교
            if guess < answer:
                print("🔼 UP!")
            elif guess > answer:
                print("🔽 DOWN!")
            else:
                print(f"🎉 정답입니다! {attempts}번 만에 맞히셨네요!")
                break  # 정답을 맞히면 게임 종료

        except ValueError:
            # 숫자가 아닌 값이 들어왔을 경우 예외 처리
            print("⚠️ 정수 숫자만 입력 가능합니다.")

if __name__ == "__main__":
    up_and_down_game()
