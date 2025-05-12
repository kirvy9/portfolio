# 📄 Test Case A 로그인

## Test Case A_01

**Test Case ID:** TC_A_01

**Title:** 로그인 시나리오

**Precondition:** 회원가입이 완료된 상태

### Steps:
1. 로그인 페이지로 이동한다.
2. 유효한 ID/PW를 입력한다.
3. 로그인 버튼을 클릭한다.

### Expected Result:
1. 로그인 성공 후 메인 페이지로 이동

### Actual Result: (테스트 실행 후 기록)

**Status:** Pass / Fail


## Test Case A_02

**Test Case ID:** TC_A_02

**Title:** 로그인 비밀번호 찾기

**Precondition:** 로그인 페이지 접근 상태

### Steps:
1. '비밀번호를 잊으셨나요?' 버튼으로 마우스 포인터 이동
2. '비밀번호를 잊으셨나요?' 버튼 클릭
3. 이메일 입력
4. '계속' 버튼 클릭

### Expected Result:
1. 입력한 이메일로 비밀번호 재설정 메일 발송 안내

### Actual Result: (테스트 실행 후 기록)

**Status:** Pass / Fail


# 📄 Test Case B 회원가입

## Test Case B_01

**Test Case ID:** TC_B_01
**Title:** 회원가입 버튼 클릭
**Precondition:** 회원가입 페이지 진입 상태

### Steps:
1. 로그인 페이지 접속
2. 마우스 포인터를 '회원가입' 버튼으로 이동

### Expected Result:
1. 버튼의 UI가 흰색 바탕이 생성
2. 회원가입 페이지로 이동

### Actual Result: (테스트 실행 후 기록)

**Status:** Pass / Fail


## Test Case B_2

**Test Case ID:** TC_B_02
**Title:** 회원가입 비밀번호 특정조건 확인
**Precondition:** 회원가입 페이지 진입 상태

### Steps:
1. 이메일, 조건이 충족되는 비밀번호 기입(1. 최소8자, 2. 다음 최소 3개 이상 포함 - 소문자, 대문자, 숫자, 특수문자)

### Expected Result:
1. 비밀번호 생성 조건 UI가 충족하는 비밀번호가 입력 될 때 조건 박스에 ●표시에서 √표시로 변화
2. 마우스 포인터가 '계속하기' 버튼 위로 이동 시 빨간색 버튼의 색상에 검정색이 추가

### Actual Result: (테스트 실행 후 기록)

**Status:** Pass / Fail


## Test Case B-3

**Test Case ID:** TC_B_03
**Title:** 회원가입 앱 승인 버튼 클릭
**Precondition:** 회원가입 페이지에서 이메일, 비밀번호 입력 완료, 앱 승인 페이지 진입 상태

### Steps:
1. '계속하기' 버튼으로 마우스 포인터 이동
2. '계속하기' 버튼 클릭
3. 마우스 포인터를 'Accept' 버튼으로 이동

### Expected Result:
1. 사용자의 이메일 앞2글자가 표시된 프로필이 생성된 앱 승인 페이지로 이동
2. 'Accept' 버튼 위로 마우스 포인터가 위치하면 빨간색 박스에 검정색 컬러가 추가

### Actual Result: (테스트 실행 후 기록)

**Status:** Pass / Fail


## Test Case B-4

**Test Case ID:** TC_B_04
**Title:** 회원가입 인적사항 정보 기입
**Precondition:** 앱 승인 페이지에서 승인 완료, 인적사항 페이지 접근 상태

### Steps:
1. 앱 승인
2. 인적사항 페이지 이동

### Expected Result:
1. 인적사항(이름, 팀 - 소속 팀 선택, 성향 수치 - 최소 1 이상, 추가 성향 - 10자 이상 100자 이내) 기입

### Actual Result: (테스트 실행 후 기록)

**Status:** Pass / Fail


## Test Case B-5

**Test Case ID:** TC_B_05
**Title:** 인적사항 팀 선택
**Precondition:** 인적사항 기입 페이지 입장 상태

### Steps:
1. 이름 작성
2. 마우스 포인터가 '팀 선택' 버튼으로 이동
3. '팀 선택' 버튼 클릭

### Expected Result:
1. 드롭다운 메뉴가 나타남
2. 본인이 소속된 팀을 선택가능

### Actual Result: (테스트 실행 후 기록)

**Status:** Pass / Fail


## Test Case B-6

**Test Case ID:** TC_B_06
**Title:** 인적사항 음식 성향
**Precondition:** 인적사항 기입 페이지 입장 상태

### Steps:
1. 이름 작성
2. 소속 팀 선택
3. 슬라이더UI 로 마우스 포인터 이동
4. 원하는 위치에 마우스 포인터로 슬라이더 UI 클릭

### Expected Result:
1. 슬라이더UI 위에서 마우스 포인터가 클릭된 위치로 핸들 이동
2. 핸들의 이동 범위에 따라 회색바탕이였던 슬라이더가 녹색으로 컬러 변경
3. 이동한 만큼 숫자로 표시

### Actual Result: (테스트 실행 후 기록)

**Status:** Pass / Fail


## Test Case B-7

**Test Case ID:** TC_B_07
**Title:** 제출하기 버튼 클릭
**Precondition:** 인적사항 페이지 접근 상태, 인적사항 작성 완료

### Steps:
1. '제출하기' 버튼으로 마우스 포인터 이동

### Expected Result:
1. 마우스 포인터가 '제출하기' 버튼 위로 위치하면 버튼의 UI가 빨간색에 하얀색 바탕이 추가

### Actual Result: (테스트 실행 후 기록)

**Status:** Pass / Fail


## Test Case B-8

**Test Case ID:** TC_B_08
**Title:** 회원가입 완료
**Precondition:** 인적사항 페이지 접근 상태, 인적사항 작성 완료

### Steps:
1. 로그인 페이지 접속
2. 회원가입 버튼 클릭
3. 이메일, 비밀번호 작성
4. 앱 승인
5. 인적사항 입력
6. '제출하기' 버튼으로 마우스 포인터 이동
7. '제출하기' 버튼 클릭

### Expected Result:
1. 회원 가입 완료 후 메인 페이지로 이동 

### Actual Result: (테스트 실행 후 기록)

**Status:** Pass / Fail