# arknights/tests/test_game_entry.py
import time
from arknights.Base.desired_caps import get_driver
from arknights.Play.operation import Operation


def test_game_entry():
    driver = get_driver()
    start = Operation(driver)
    
    try:
        print("--- 게임 실행 ---")
        time.sleep(10)

        # 게임 실행 및 로그인 과정
        print("--- 첫 번째 START 버튼 클릭 시도 ---")
        start.click_first_start()
        
        print("--- 공지 닫기 시도 ---")
        start.close_popup()
        
        print("--- 두 번째 START 버튼 클릭 시도 ---")
        start.click_second_start()
        
        print("--- 메인화면 진입 ---")
        # 메인화면 진입 후 필요한 작업 추가

        # 출석부 팝업 처리 (한 번만 시도)
        print("--- 출석부 팝업 처리 시도 ---")
        time.sleep(10)  # 화면 로딩 대기

        # 1. 먼저 당일 배급 확인 및 수령
        start.check_daily_reward_and_collect()
        time.sleep(10)

        # 2. 출석부 팝업 확인 및 닫기
        start.check_attendance()

        # 이벤트 팝업 처리
        print("--- 이벤트 팝업 처리 시도 ---")
        start.handle_event_popup()
        
        # 여기에 작전 페이지 이동 등 다음 단계 코드 추가
        print("--- 다음 단계 진행 ---")

        # 팝업 처리 후 작전 메뉴로 이동
        start.go_to_operation()

        # 스토리 메뉴로 이동
        start.go_to_attention()

        # 스토리 메뉴 진입 후, 랜덤 스테이지 선택
        print("--- 랜덤 스테이지 선택 ---")
        stage_selected = start.select_random_stage()

        if stage_selected:
            # 대리 지휘 체크
            print("--- 대리 지휘 설정 ---")
            start.check_proxy_command()
    
            # 작전 개시
            print("--- 작전 개시 ---")
            start.start_operation()

            # 편성 화면에서 작전 개시 버튼 클릭
            print("--- 편성 화면에서 작전 개시 ---")
            start.click_operation_start_button()

            # 자동 전투 완료 대기
            print("--- 자동 전투 대기 중 ---")
            battle_completed = start.wait_for_auto_battle_completion(max_wait_time=600)  # 최대 10분 대기

            if battle_completed:
                print("전투가 성공적으로 완료되었습니다")
                # 여기에 전투 완료 후 추가 작업 구현
        else:
            print("전투 완료를 감지하지 못했습니다")

    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    test_game_entry()