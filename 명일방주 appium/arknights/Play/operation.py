# arknights/Pages/start_page.py - OpenCV 기능 통합 버전
import time
import cv2
import numpy as np
import random
import io
import os
from PIL import Image

#피드백
#1. 명시적 대기로 변경할 수 있다면 무조건 하기
#2. 파일 제목 수정 start_page -> 게임이니 그것에 맞게
#3. 영상은 녹화 후 편집해서 2배속 설정
class Operation:
    def __init__(self, driver):
        self.driver = driver
        self.screen_size = self.driver.get_window_size()
        print(f"화면 크기: {self.screen_size}")
        
    def get_screenshot(self):
        """스크린샷을 OpenCV 형식으로 변환"""
        screenshot = self.driver.get_screenshot_as_png()
        img = Image.open(io.BytesIO(screenshot))
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    def check_image_exists(self, template_path, threshold=0.7):
        """화면에서 템플릿 이미지를 찾아 있는지 확인"""
        try:
            screenshot = self.get_screenshot()
            template = cv2.imread(template_path)
            
            if template is None:
                print(f"템플릿 이미지를 로드할 수 없음: {template_path}")
                return False, None
            
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            if max_val >= threshold:
                h, w = template.shape[:2]
                center_x = max_loc[0] + w // 2
                center_y = max_loc[1] + h // 2
                return True, (center_x, center_y)
            
            return False, None
        except Exception as e:
            print(f"이미지 확인 오류: {e}")
            return False, None
    
    def click_image_if_exists(self, template_path, fallback_x, fallback_y, threshold=0.7):
        """이미지를 찾아 클릭하고, 없으면 대체 좌표 클릭"""
        exists, coords = self.check_image_exists(template_path, threshold)
        
        if exists:
            x, y = coords
            print(f"이미지 찾음 ({template_path}) - 좌표: ({x}, {y})")
            self.driver.tap([(x, y)])
            return True
        else:
            print(f"이미지를 찾지 못함 ({template_path}) - 대체 좌표 사용: ({fallback_x}, {fallback_y})")
            self.driver.tap([(fallback_x, fallback_y)])
            return False
    
    def click_first_start(self):
        print("1차 START 클릭")
        time.sleep(30)  # 초기 대기 시간 증가 (게임 리소스 로딩 기다림)
        self.driver.tap([(645, 700)])  # 좌표 기반 클릭
        print("1차 START 버튼 클릭 완료")
        time.sleep(10)  # 충분한 대기 시간
    
    def close_popup(self):
        print("공지 닫기")
        time.sleep(15)  # 화면 준비 대기
        self.driver.tap([(800, 720)])  # '알겠습니다' 버튼 좌표
        print("공지 닫기 완료")
        time.sleep(5)  # 충분한 대기

    def click_second_start(self):
        print("2차 START 클릭")
        time.sleep(15)  # 화면 준비 대기
        self.driver.tap([(800, 700)])  # 두 번째 START 버튼 좌표
        print("2차 START 버튼 클릭 완료")
        time.sleep(20)  # 메인화면 로딩 대기 (20초 → 35초)

        # arknights/Pages/start_page.py에 추가할 코드

    def check_daily_reward_and_collect(self):
        """당일 배급 표시 확인하고 보상 수령"""
        try:
            # 스크린샷 캡처
            screenshot = self.get_screenshot()
        
            # 당일 배급 템플릿 로드
            template_path = "templates/daily_reward.png"
            template = cv2.imread(template_path)
        
            if template is None:
                print(f"당일 배급 템플릿을 로드할 수 없음: {template_path}")
                return False
        
            # 템플릿 매칭 수행
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
            # 임계값 이상이면 당일 배급 존재 및 수령
            if max_val >= 0.5:
                print(f"당일 배급 발견 (신뢰도: {max_val:.2f}), 보상 수령 시도")
            
                # 화면 중앙 클릭 (보상 수령)
                screen_size = self.driver.get_window_size()
                center_x = screen_size['width'] // 2
                center_y = int(screen_size['height'] * 0.75)  
                print(f"보상 수령을 위해 클릭할 좌표: ({center_x}, {center_y})")
                self.driver.tap([(center_x, center_y)])
                time.sleep(15)  # 보상 수령 애니메이션 대기
            
                return True
        
            print(f"당일 배급 없음 (최대 신뢰도: {max_val:.2f})")
            return False
        except Exception as e:
            print(f"당일 배급 확인 중 오류: {e}")
            return False

    def is_attendance_popup_visible(self):
        """템플릿 매칭으로 출석부 팝업 확인"""
        print("템플릿 매칭으로 출석부 팝업 확인 중...")
    
        try:
            # 스크린샷 캡처
            screenshot = self.get_screenshot()
        
            # 출석부 팝업 템플릿 로드
            template_path = "templates/attendance_popup.png"
            template = cv2.imread(template_path)
        
            if template is None:
                print(f"출석부 템플릿을 로드할 수 없음: {template_path}")
                # 템플릿이 없으면 기존 픽셀 기반 방식 사용
                return self._check_attendance_by_pixel_color(screenshot)
        
            # 템플릿 매칭 수행
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
            # 임계값 이상이면 출석부 팝업으로 판단
            if max_val >= 0.8:  # 높은 임계값 설정
                print(f"출석부 팝업 확인됨 (신뢰도: {max_val:.2f})")
                return True
        
            print(f"출석부 팝업 매칭 실패 (최대 신뢰도: {max_val:.2f})")
            return False
        
        except Exception as e:
            print(f"출석부 확인 중 오류: {e}")
            return False

    def check_attendance(self):
        """출석부 팝업 한 번만 확인"""
        print("출석부 확인 시도")
    
        # 출석부 팝업 감지
        if self.is_attendance_popup_visible():
            print("출석부 팝업 감지됨, 처리 시작")
        
            # X 버튼 클릭 (팝업 닫기)
            self.driver.tap([(1520, 89)])
            time.sleep(15)  # 팝업 닫힘 대기
        
            print("출석부 처리 완료")
            return True
    
        print("출석부 팝업이 감지되지 않음")
        return False
    
    def handle_event_popup(self):
        """이벤트 팝업 처리 (전망출석 등)"""
        print("이벤트 팝업 확인 중...")
        screenshot = self.get_screenshot()
    
        # 이벤트 팝업 X 버튼 위치 확인
        x_button_area = screenshot[125, 1560]  # 우상단 X 버튼 위치 (y, x)
    
        # X 버튼이 밝은 색인지 확인
        if x_button_area[0] > 180 and x_button_area[1] > 180 and x_button_area[2] > 180:
            print("이벤트 팝업 감지됨, 닫기 시도")
            self.driver.tap([(1560, 125)])  # X 버튼 클릭
            time.sleep(10)
            return True
    
        return False
    
    def go_to_operation(self):
        """작전 메뉴로 이동"""
        print("작전 메뉴로 이동 중...")
    
        # 작전 버튼 클릭 (화면 중앙 상단의 '작전' 텍스트 버튼)
        self.driver.tap([(1200, 225)])  # 작전 버튼 좌표
        time.sleep(10)  # 화면 전환 대기
    
        print("작전 메뉴 진입 완료")
        return True
    
    def go_to_attention(self):
        """스토리로 이동"""
        print("스토리로 이동 중...")
    
        # 작전 버튼 클릭 (화면 중앙 상단의 '작전' 텍스트 버튼)
        self.driver.tap([(980, 230)])  # 작전 버튼 좌표
        time.sleep(10)  # 화면 전환 대기
    
        print("스토리 진입 완료")
        return True
    
    def select_random_stage(self, swipes=3):
        """랜덤하게 스와이프한 후 스테이지 영역 클릭 (템플릿 매칭 버전)"""
        print("템플릿 매칭으로 스테이지 선택 중...")
 
        # 랜덤하게 좌우 스와이프 수행
        swipe_count = random.randint(1, swipes)
 
        for _ in range(swipe_count):
            direction = random.choice(["left", "right"])
            self.swipe_stage_selection(direction)
 
        # 템플릿 매칭으로 스테이지 찾아 클릭
        success = self.find_and_click_stage_template()
    
        if not success:
            print("스테이지 선택 실패, 중앙 영역 클릭으로 대체")
            # 실패 시 중앙 영역 클릭 (대체 방법)
            screen_size = self.driver.get_window_size()
            center_x = screen_size['width'] // 2
            center_y = screen_size['height'] // 2
            self.driver.tap([(center_x, center_y)])
            time.sleep(5)
        
        return success  # 성공/실패 여부 반환
    
    def swipe_stage_selection(self, direction="right"):
        """스테이지 선택 화면에서 좌우 스와이프"""
        print(f"스테이지 화면 {direction} 방향으로 스와이프...")
    
        screen_size = self.driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']
    
        # 스와이프 시작/종료 지점 계산
        start_x = width * 0.8 if direction == "left" else width * 0.2
        end_x = width * 0.2 if direction == "left" else width * 0.8
        mid_y = height * 0.5
    
        # 스와이프 실행
        self.driver.swipe(start_x, mid_y, end_x, mid_y, 500)
        time.sleep(5)  # 스와이프 후 화면 안정화 대기
    
        print("스와이프 완료")
        return True

    def find_and_click_stage_template(self):
        """템플릿 매칭을 사용하여 스테이지 버튼 찾아 클릭"""
        print("템플릿 매칭으로 스테이지 버튼 찾는 중...")
    
        # 최대 시도 횟수
        max_attempts = 5
    
        for attempt in range(max_attempts):
            # 현재 화면 캡처
            screenshot = self.get_screenshot()
        
            # 디버깅을 위해 스크린샷 저장 (선택사항)
            debug_dir = "debug_images"
            os.makedirs(debug_dir, exist_ok=True)
            cv2.imwrite(os.path.join(debug_dir, f"screen_{attempt}.png"), screenshot)
        
            # 템플릿 디렉토리 확인
            template_dir = "templates"
            if not os.path.exists(template_dir):
                print(f"템플릿 디렉토리가 없음: {template_dir}")
                return False
        
            # 템플릿 목록 가져오기
            template_files = [f for f in os.listdir(template_dir) if f.startswith("stage_") and f.endswith(".png")]
            if not template_files:
                print("템플릿 파일을 찾을 수 없음")
                return False
            
            # 모든 매칭 결과 저장
            matches = []
        
            # 각 템플릿에 대해 매칭 시도
            for template_file in template_files:
                template_path = os.path.join(template_dir, template_file)
                template = cv2.imread(template_path)
            
                if template is None:
                    print(f"템플릿을 로드할 수 없음: {template_file}")
                    continue
                
                # 템플릿 매칭 수행
                result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
                # 신뢰도가 충분히 높은 경우만 저장
                if max_val >= 0.75:  # 신뢰도 임계값
                    h, w = template.shape[:2]
                    center_x = max_loc[0] + w // 2
                    center_y = max_loc[1] + h // 2
                
                    matches.append({
                        'file': template_file,
                        'confidence': max_val,
                        'position': (center_x, center_y)
                    })
                
                    # 디버깅: 매칭 위치 표시
                    debug_img = screenshot.copy()
                    cv2.rectangle(debug_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)
                    cv2.putText(debug_img, f"{template_file}: {max_val:.2f}", 
                            (max_loc[0], max_loc[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.imwrite(os.path.join(debug_dir, f"match_{template_file}_{attempt}.png"), debug_img)
        
            # 중복 제거 및 신뢰도 기준 정렬
            if matches:
                # 중복 매칭 필터링 (거리 기반)
                filtered_matches = self.filter_overlapping_matches(matches)
            
                # 신뢰도 기준 정렬
                filtered_matches.sort(key=lambda x: -x['confidence'])
            
                # 가장 신뢰도 높은 매칭 선택
                best_match = filtered_matches[0]
                x, y = best_match['position']
            
                print(f"스테이지 버튼 발견: {best_match['file']} (신뢰도: {best_match['confidence']:.2f}, 좌표: {x}, {y})")
            
                # 클릭
                self.driver.tap([(x, y)])
                time.sleep(5)  # 스테이지 정보 로딩 대기
            
                # 스테이지 상세 화면이 표시되었는지 확인 (선택사항)
                if self.check_stage_detail_screen():
                    print("스테이지 상세 화면 확인됨")
                    return True
                else:
                    print("스테이지 상세 화면 확인 실패, 다시 시도")
            else:
                print(f"시도 {attempt+1}: 매칭된 스테이지 버튼 없음, 스와이프 시도")
            
            # 다음 시도를 위해 스와이프
            direction = "right" if attempt % 2 == 0 else "left"
            self.swipe_stage_selection(direction)
            time.sleep(3)  # 스와이프 후 안정화 대기
    
        print(f"{max_attempts}회 시도 후에도 스테이지 버튼을 찾지 못함")
        return False

    def filter_overlapping_matches(self, matches, min_distance=50):
        """거리 기반 중복 매칭 필터링"""
        if not matches:
            return []
        
        filtered = []
    
        # 신뢰도 기준 정렬
        sorted_matches = sorted(matches, key=lambda x: -x['confidence'])
    
        for match in sorted_matches:
            # 이미 필터링된 매치들과 거리 확인
            is_duplicate = False
            for filtered_match in filtered:
                # 유클리드 거리 계산
                x1, y1 = match['position']
                x2, y2 = filtered_match['position']
                distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            
                if distance < min_distance:
                    is_duplicate = True
                    break
                
            if not is_duplicate:
                filtered.append(match)
    
        return filtered

    def check_stage_detail_screen(self, threshold=0.7):
        """템플릿 매칭으로 스테이지 상세 화면 확인 (여러 템플릿 사용)"""
        print("템플릿 매칭으로 스테이지 상세 화면 확인 중...")
    
        try:
            # 스크린샷 캡처
            screenshot = self.get_screenshot()
        
            # 여러 템플릿 경로 정의
            template_paths = [
                "templates/stage_detail_screen.png",        # 체크되지 않은 상태
                "templates/stage_detail_screen_checked.png" # 체크된 상태
            ]
        
            # 각 템플릿마다 매칭 시도
            for template_path in template_paths:
                template = cv2.imread(template_path)
            
                if template is None:
                    print(f"템플릿을 로드할 수 없음: {template_path}")
                    continue
                
                # 템플릿 매칭 수행
                result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
                # 임계값 이상이면 스테이지 상세 화면으로 판단
                if max_val >= threshold:
                    print(f"스테이지 상세 화면 확인됨 (템플릿: {template_path}, 신뢰도: {max_val:.2f})")
                    return True
                
                print(f"템플릿과 매칭 실패: {template_path} (신뢰도: {max_val:.2f})")
        
            print("모든 템플릿과 매칭 실패")
            return False
        
        except Exception as e:
            print(f"스테이지 상세 화면 확인 중 오류: {e}")
            return False
    
    def check_proxy_command(self):
        """템플릿 매칭으로 대리 지휘 체크박스 확인 및 체크"""
        print("대리 지휘 체크박스 확인 중...")
    
        # 스크린샷 캡처
        screenshot = self.get_screenshot()
    
        # 체크된 상태와 체크되지 않은 상태의 템플릿 경로
        unchecked_template = "templates/proxy_unchecked.png"
        checked_template = "templates/proxy_checked.png"
    
        # 체크되지 않은 상태 확인
        unchecked_exists, _ = self.check_image_exists(unchecked_template, threshold=0.7)
    
        # 체크된 상태 확인
        checked_exists, _ = self.check_image_exists(checked_template, threshold=0.7)
    
        if unchecked_exists:
            print("대리 지휘 체크박스가 체크되지 않음, 체크 시도")
            self.driver.tap([(1380, 760)])  # 체크박스 위치
            time.sleep(5)
            return True
        elif checked_exists:
            print("대리 지휘 체크박스가 이미 체크됨")
            return True
        else:
            print("대리 지휘 체크박스 상태를 판단할 수 없음, 기본 위치 클릭")
            self.driver.tap([(1380, 760)])  # 체크박스 위치
            time.sleep(5)
            return False

    def start_operation(self):
        """작전 개시 버튼 클릭"""
        print("작전 개시 버튼 클릭 중...")
    
        # 작전 개시 버튼 클릭
        self.driver.tap([(1450, 840)])  # 작전 개시 버튼 위치
        time.sleep(10)  # 전투 준비 화면 로딩 대기
    
        print("작전 개시 버튼 클릭 완료")
        return True
    
    def click_operation_start_button(self):
        """편성 화면에서 작전 개시 버튼 클릭"""
        print("편성 화면에서 작전 개시 버튼 찾는 중...")
    
        # 작전 개시 버튼 템플릿 매칭
        template_path = "templates/operation_start_button.png"
        exists, coords = self.check_image_exists(template_path)
    
        if exists:
            x, y = coords
            print(f"작전 개시 버튼 발견 (좌표: {x}, {y})")
            self.driver.tap([(x, y)])
            time.sleep(10)  # 전투 시작 로딩 대기
            return True
        else:
            print("작전 개시 버튼을 찾지 못함, 오른쪽 하단 클릭 시도")
            # 대체 방법: 화면 오른쪽 하단 클릭
            screen_size = self.driver.get_window_size()
            x = int(screen_size['width'] * 0.9)  # 오른쪽
            y = int(screen_size['height'] * 0.9)  # 하단
            self.driver.tap([(x, y)])
            time.sleep(10)
            return False
    
    def wait_for_auto_battle_completion(self, max_wait_time=300, check_interval=10):
        """전투 완료 화면이 나타날 때까지 대기"""
        print(f"자동 전투 진행 중... (최대 대기 시간: {max_wait_time}초)")
        start_time = time.time()
    
        # 완료 화면 템플릿
        template_path = "templates/battle_complete.png"
    
        while time.time() - start_time < max_wait_time:
            try:
                screenshot = self.get_screenshot()
                template = cv2.imread(template_path)
            
                if template is None:
                    print(f"전투 완료 템플릿을 로드할 수 없음: {template_path}")
                    break
                
                # 템플릿 매칭 수행
                result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
                # 임계값 이상이면 전투 완료로 판단
                if max_val >= 0.8:
                    elapsed_time = int(time.time() - start_time)
                    print(f"전투 완료 화면 감지 (소요 시간: {elapsed_time}초, 신뢰도: {max_val:.2f})")
                    time.sleep(10)  # 결과 화면 안정화 대기
                    return True
                
                elapsed_time = int(time.time() - start_time)
                if elapsed_time % 30 == 0:  # 30초마다 메시지 출력
                    print(f"전투 진행 중... (경과: {elapsed_time}초)")
                
                time.sleep(check_interval)
            except Exception as e:
                print(f"전투 완료 확인 중 오류: {e}")
                time.sleep(check_interval)
    
        print(f"최대 대기 시간({max_wait_time}초) 초과")
        return False
    