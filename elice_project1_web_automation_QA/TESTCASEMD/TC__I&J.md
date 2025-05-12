# 📄 Test Cases

## Test Case I

**Test Case ID:** TC_I_001  
**Title:**   개인 피드 페이지 접근 테스트
**Precondition:** 로그인 

### Steps:
1. 테스트 홈페이지 로그인 ( testid@test.com / testpw1! )
2. 홈 화면 우측 하단 '개인 피드' 버튼 클릭
3. 개인 피드 페이지 접근


### Expected Result:
- 홈 화면에서 '개인 피드' 버튼을 클릭 시 개인 피드 페이지에 접근이 되어야 함


### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** 진행중

---

**Test Case ID:** TC_I_002  
**Title:**   후기 작성 페이지 접근 테스트
**Precondition:** 로그인 / 개인 피드 페이지 접근 상태 ( TC_I_001 )

### Steps:
1. TC I_001
2. 내가 먹은 메뉴 옆 '+' 버튼 상호작용
3. 후기 작성 페이지 접근



### Expected Result:
- '+' 버튼을 상호작용 했을 시, 새로운 후기 작성 페이지에 접근이 가능해야 함


### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** 진행중

---


**Test Case ID:** TC_I_003  
**Title:**   식사 유형 선택 기능 테스트
**Precondition:** 로그인 / 개인 피드 -> 후기 작성 페이지 접근 상태 ( TC_I_002 )

### Steps:
1. TC I_002
2. 혼밥, 그룹, 회식 - 선택 (테스트 코드에선 랜덤으로 1개 선택)

### Expected Result:
- 원하는 식사 유형에 맞게 페이지가 나타나야 함(혼밥&회식 동일 , 그룹 같이먹은 사람 선택기능 출력)


### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** 진행중

---

**Test Case ID:** TC_I_004  
**Title:**   후기 사진 등록기능 테스트
**Precondition:** 로그인 / 개인 피드 -> 후기 작성 페이지 접근 상태 ( TC_I_002 )

### Steps:
1. TC I_003
2. 후기 사진 등록 버튼 상호작용
3. 사진 선택

### Expected Result:
- 사용자가 선택한 사진이 후기 사진으로 등록이 되어야 함


### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** 진행중

---

**Test Case ID:** TC_I_005  
**Title:**   후기 메뉴명 등록기능 테스트
**Precondition:** 로그인 / 개인 피드 -> 후기 작성 페이지 접근 상태 ( TC_I_002 )

### Steps:
1.TC I_004
2. 메뉴 명 입력 ( 테스트용 메뉴명 )

### Expected Result:
- 사용자가 입력한 메뉴명이 등록 되어야 함


### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** 진행중

---

**Test Case ID:** TC_I_006  
**Title:**   후기 카테고리 선택기능 테스트
**Precondition:** 로그인 / 개인 피드 -> 후기 작성 페이지 접근 상태 ( TC_I_002 )

### Steps:
1. TC I_005
2. 음식 카테고리 랜덤 선택

### Expected Result:
- 음식 카테고리(한식, 중식, 양식, 일식, 분식, 아시안, 패스트푸드, 기타)가 랜덤으로 1종 선택되어야 함


### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** 진행중

---


**Test Case ID:** TC_I_007  
**Title:**   후기 내용작성 기능 테스트
**Precondition:** 로그인 / 개인 피드 -> 후기 작성 페이지 접근 상태 ( TC_I_002 )

### Steps:
1. TC I_006
2. 후기 내용 작성 ( 테스트용 음식 후기입니다.)


### Expected Result:
- 사용자가 입력한 메뉴명이 등록 되어야 함


### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** 진행중

---

**Test Case ID:** TC_I_008  
**Title:**   별점 추가 기능 테스트 
**Precondition:** 로그인 / 개인 피드 -> 후기 작성 페이지 접근 상태 ( TC_I_002 )

### Steps:
1. TC I_007
2. 후기 내용 작성란 아래, 별점부여( 자동화 테스트 시 1~5점 랜덤 부여 )


### Expected Result:
- 사용자가 원하는 별점의 갯수가 활성화 되어야 함


### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** 진행중

---

**Test Case ID:** TC_I_009  
**Title:**   후기 작성 완료기능 테스트 
**Precondition:** 로그인 / 개인 피드 -> 후기 작성 페이지 접근 상태 ( TC_I_002 )

### Steps:
1. TC I_008
2. '후기 작성 완료' 버튼으로 마우스 이동
3. '후기 작성 완료' 버튼 클릭


### Expected Result:
- 개인 피드 페이지 - 내가 먹은 메뉴 리스트에 후기가 등록되어야 함


### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** 진행중


---
---
---

## Test Case J  

**Test Case ID:** TC J_001 
**Title:** 프로필 수정 페이지 접근기능 테스트 
**Precondition:** 로그인 / 개인 피드 페이지 접근 상태 ( TC_I_001 )  

### Steps:
1. TC I_001 (개인 피드 페이지 접근) 
2. 프로필 수정 버튼 🖊 으로 마우스 이동
3. 프로필 수정 버튼 상호작용
4. 프로필 수정 페이지 접근


### Expected Result:
- 프로필 정보 수정 페이지로 접근이 되어야 함

### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** Pass / Fail  

---

**Test Case ID:** TC J_002 
**Title:** 프로필 이미지 수정 기능 테스트 
**Precondition:** 로그인 / 개인 피드 -> 프로필 수정 페이지 ( TC_J_001 )

### Steps:
1. TC J_001
2. 프로필 이미지 수정 버튼 클릭
3. 임의의 사진 등록
4. 페이지 하단 ' 프로필 수정 완료 ' 버튼 상호작용
5. 개인 피드 페이지로 복귀


### Expected Result:
- 사용자가 원하는 사진으로 프로필 사진이 변경되어야 함

### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** Pass / Fail  

---

**Test Case ID:** TC J_003 
**Title:** 음식 성향 수치기능 조절 테스트 ( 단맛 ) 
**Precondition:** 로그인 / 개인 피드 -> 프로필 수정 페이지 ( TC_J_001 ) 

### Steps:
1. TC J_001
2. 음식 성향 중, '단맛' 슬라이더의 값 변경 ( 자동화 테스트 시 '3' 으로 변경)
3. 페이지 하단 ' 프로필 수정 완료 ' 버튼 상호작용
4. 개인 피드 페이지로 복귀


### Expected Result:
- 사용자가 원하는 수치로 단맛 슬라이더의 값이 변경되어야 함

### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** Pass / Fail  

---

**Test Case ID:** TC J_004 
**Title:** 음식 성향 수치기능 조절 테스트 ( 짠맛 ) 
**Precondition:** 로그인 / 개인 피드 -> 프로필 수정 페이지 ( TC_J_001 ) 

### Steps:
1. TC J_001
2. 음식 성향 중, '짠맛' 슬라이더의 값 변경 ( 자동화 테스트 시 '2' 으로 변경)
3. 페이지 하단 ' 프로필 수정 완료 ' 버튼 상호작용
4. 개인 피드 페이지로 복귀


### Expected Result:
- 사용자가 원하는 수치로 짠맛 슬라이더의 값이 변경되어야 함

### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** Pass / Fail  

---

**Test Case ID:** TC J_005 
**Title:** 음식 성향 수치기능 조절 테스트 ( 매운맛 ) 
**Precondition:** 로그인 / 개인 피드 -> 프로필 수정 페이지 ( TC_J_001 ) 

### Steps:
1. TC J_001
2. 음식 성향 중, '매운맛' 슬라이더의 값 변경 ( 자동화 테스트 시 '4' 으로 변경)
3. 페이지 하단 ' 프로필 수정 완료 ' 버튼 상호작용
4. 개인 피드 페이지로 복귀


### Expected Result:
- 사용자가 원하는 수치로 매운맛 슬라이더의 값이 변경되어야 함

### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** Pass / Fail  

---

**Test Case ID:** TC J_006 
**Title:** 음식 성향 중, 이런 음식은 좋아요! 텍스트 수정 기능 테스트
**Precondition:** 로그인 / 개인 피드 -> 프로필 수정 페이지 ( TC_J_001 ) 

### Steps:
1. TC J_001
2. 음식 성향 중, ' 이런 음식은 좋아요! ' 부분의 텍스트 수정 ( 자동화 테스트에선 '좋아하는 음식 테스트 입니다.' 로 적용)
3. 페이지 하단 ' 프로필 수정 완료 ' 버튼 상호작용
4. 개인 피드 페이지로 복귀


### Expected Result:
- 사용자가 원하는 텍스트가 이런 음식은 좋아요! 텍스트 박스에 담겨야 함

### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** Pass / Fail  

---

**Test Case ID:** TC J_007 
**Title:** 음식 성향 중, 이런 음식은 싫어요! 텍스트 수정 기능 테스트
**Precondition:** 로그인 / 개인 피드 -> 프로필 수정 페이지 ( TC_J_001 ) 

### Steps:
1. TC J_001
2. 음식 성향 중, ' 이런 음식은 싫어요! ' 부분의 텍스트 수정 ( 자동화 테스트에선 '싫어하는 음식 테스트 입니다.' 로 적용)
3. 페이지 하단 ' 프로필 수정 완료 ' 버튼 상호작용
4. 개인 피드 페이지로 복귀


### Expected Result:
- 사용자가 원하는 텍스트가 이런 음식은 싫어요! 텍스트 박스에 담겨야 함

### Actual Result:  
*(테스트 실행 후 기록)*  

**Status:** Pass / Fail  

---