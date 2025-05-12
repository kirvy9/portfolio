## 📄 Test Cases

### Test Case G_01
- **Test Case ID**: TC_G_01
- **Title**: 메뉴 추천 리스트 페이지 새로고침 기능 테스트(자동화)
- **Precondition**: 로그인, '개발2팀' 선택, 혼자먹기 선택, 음식 카테고리 무작위 선택, 메뉴추천 페이지 진입 상태
- **Steps**:
  1. 현재 추천 메뉴 확인
  2. 새로 고침 버튼 클릭
  3. 변경된 추천 메뉴 확인
  
- **Expected Result**:  
  - 처음 추천 메뉴와 새로 고침 후 추천 메뉴가 다름
- **Actual Result**: 처음 추천 메뉴와 새로 고침 후 추천 메뉴가 다름
- **Status**: 완료

### Test Case G_02
- **Test Case ID**: TC_G_02
- **Title**: 맛집 추천 기능 테스트(자동화)
- **Precondition**: 로그인, '개발2팀' 선택, 혼자먹기 선택, 음식 카테고리 무작위 선택, 메뉴추천 페이지 진입 상태
- **Steps**:
  1. 맛집 리스트 여부 확인
  2. 맛집 리스트 결과가 '검색 결과가 없습니다.' 혹은 swipe 가능한 페이지가 2페이지 이하.
  3. 새로 고침 버튼 클릭
  4. swipe 가능한 페이지가 2페이지 이상 될 때 까지 새로고침 반복
 
- **Expected Result**:  
  - 2페이지 이상의 맛집 리스트가 추천된다.
- **Actual Result**: 2페이지 이상의 맛집 리스트가 추천된다.
- **Status**: 완료



### Test Case G_03
- **Test Case ID**: TC_G_03
- **Title**: 맛집 리스트의 스와이프 기능 테스트(자동화)
- **Precondition**: 로그인, '개발2팀' 선택, 혼자먹기 선택, 음식 카테고리 무작위 선택, 메뉴추천 페이지 진입 상태 ,TC_G_02
- **Steps**:
  1. 맛집 리스트 여부 확인
  2. 맛집 리스트 스와이프(swipe 버튼 클릭)
 
- **Expected Result**:  
  - swipe 버튼 클릭시 맛집 리스트 페이지가 넘어간다.
- **Actual Result**: swipe 버튼 클릭시 맛집 리스트 페이지가 넘어간다.
- **Status**: 완료



### Test Case G_04
- **Test Case ID**: TC_G_04
- **Title**: 맛집 리스트 메뉴 확인(수동)
- **Precondition**: 로그인, '개발2팀' 선택, 혼자먹기 선택, 음식 카테고리 무작위 선택, 메뉴추천 페이지 진입 상태
- **Steps**:
  1. 맛집 리스트 여부 확인
  2. 맛집 리스트 클릭
  3. 맛집 리스트 메뉴 중 추천 메뉴 존재 확인
 
- **Expected Result**:  
  - 추천 메뉴가 존재 한다.
- **Actual Result**: 추천 메뉴랑 이름이 다른 경우도 많고 존재하지 않는 경우도 있다.
- **Status**: 완료





### Test Case G_05
- **Test Case ID**: TC_G_05
- **Title**: ai 적합도 테스트(자동화)
- **Precondition**: 로그인, '개발2팀' 선택, 혼자먹기 선택, 음식 카테고리 무작위 선택, 메뉴추천 페이지 진입 상태
- **Steps**:
  1. ai 적합도 수치 확인
  2. 45% 이하 일 시 새로고침
  3. 45 이상일 시 새록고침 중단
  
- **Expected Result**:  
  - ai 적합도가 45% 이상이 되면 새로고침이 중단된다.
- **Actual Result**: ai 적합도가 45% 이상이 되면 새로고침이 중단된다.
- **Status**: 완료



### Test Case G_06
- **Test Case ID**: TC_G_05
- **Title**: 수락하기 버튼 클릭(자동화)
- **Precondition**: 로그인, '개발2팀' 선택, 혼자먹기 선택, 음식 카테고리 무작위 선택, 메뉴추천 페이지 진입 상태
- **Steps**:
  1. 수락하기 버튼 클릭
  2. 히스토리 페이지로 이동 확인
  3. 수락한 메뉴와 히스토리 메뉴 일치 확인
  
- **Expected Result**:  
  - 수락한 메뉴와 히스토리 메뉴 일치한다.
- **Actual Result**: 수락한 메뉴와 히스토리 메뉴 일치한다.
- **Status**: 완료



### Test Case H_01
- **Test Case ID**: TC_H_01
- **Title**: 팀 피드 진입시 내 소속 팀 표시 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 팀 피드 페이지 진입 상태
- **Steps**:
  1. 자동으로 내 소속 팀으로 진입 확인

 - **Expected Result**:  
  - 개발 2팀 선택
- **Actual Result**: 개발 2팀 선택
- **Status**: 완료



### Test Case H_02
- **Test Case ID**: TC_H_02
- **Title**: 팀 피드 내 팀 선택 버튼 작동 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 팀 피드 페이지 진입 상태
- **Steps**:
  1. 팀 선택 버튼 클릭
  2. 랜덤으로 팀 선택
  3. 선택 된 팀 반영 확인

 - **Expected Result**:  
  - 선택된 팀에 따른 페이지가 변경 된다.
- **Actual Result**: 선택된 팀에 따른 페이지가 변경 된다.
- **Status**: 완료


### Test Case H_03
- **Test Case ID**: TC_H_03
- **Title**: 팀 피드 내 '같은 메뉴 먹기' 버튼 활성화 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 팀 피드 페이지 진입 상태
- **Steps**:
  1. 팀 선택 버튼 클릭
  2. 랜덤으로 팀 선택 (소속팀 제외)
  3. '같은 메뉴 먹기' 버튼 비활성화 확인(숨김)
  4. 팀 선택 버튼 클릭
  5. 본인 소속팀 선택
  6. '같은 메뉴 먹기' 활성화 확인

 - **Expected Result**:  
  - 본인 소속팀 일 때만 '같은 메뉴 먹기' 버튼이 활성화 된다.
- **Actual Result**: 본인 소속팀 일 때만 '같은 메뉴 먹기' 버튼이 활성화 된다.
- **Status**: 완료


### Test Case H_04
- **Test Case ID**: TC_H_04
- **Title**: 팀 피드 내 팀이 먹은 메뉴 '+' 버튼 클릭 후 후기 작성 페이지 진입 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 팀 피드 페이지 진입 상태
- **Steps**:
  1. 팀이 먹는 메뉴 옆 '+' 버튼 클릭
  2. 새로운 후기 등록하기 페이지 열림

 - **Expected Result**:  
  - 새로운 후기 등록하기 페이지 진입
- **Actual Result**: 새로운 후기 등록하기 페이지 진입
- **Status**: 완료


### Test Case H_05
- **Test Case ID**: TC_H_05
- **Title**: 새로운 후기 등록하기 페이지 내 식사 유형 선택 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 새로운 후기 등록하기 페이지 진입
- **Steps**:
  1. 식사 유형 선택 (혼밥, 그룹, 회식)
  2. '그룹' 선택 시 같이먹은 사람 칸 활성화

 - **Expected Result**:  
  - 정상적으로 식사 유형이 선택되고 그룹 선택시 같이먹은 사람 칸이 추가된다.
- **Actual Result**: 정상적으로 식사 유형이 선택되고 그룹 선택시 같이먹은 사람 칸이 추가된다.
- **Status**: 완료



### Test Case H_06
- **Test Case ID**: TC_H_06
- **Title**: 새로운 후기 등록하기 페이지 내 사진 등록 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 새로운 후기 등록하기 페이지 진입
- **Steps**:
  1. 사진 이미지 버튼 클릭
  2. 경로에 있는 사진 선택
  3. 사진 등록

 - **Expected Result**:  
  - 경로에 있는 사진이 올바르게 등록된다.
- **Actual Result**: 경로에 있는 사진이 올바르게 등록된다.
- **Status**: 완료



### Test Case H_07
- **Test Case ID**: TC_H_07
- **Title**: 새로운 후기 등록하기 메뉴명, 후기 입력 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 새로운 후기 등록하기 페이지 진입
- **Steps**:
  1. 메뉴 명 칸에 메뉴를 입력한다.
  2. 후기 칸에 후기를 입력한다.
 - **Expected Result**:  
  - 메뉴와 후기가 올바르게 입력된다.
- **Actual Result**: 메뉴와 후기가 올바르게 입력된다.
- **Status**: 완료


### Test Case H_08
- **Test Case ID**: TC_H_08
- **Title**: 새로운 후기 등록하기 음식 카테고리 선택 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 새로운 후기 등록하기 페이지 진입
- **Steps**:
  1. 음식 카테고리 버튼 클릭
  2. 카테고리 중 하나 선택
 - **Expected Result**:  
  - 선택한 카테고리가 올바르게 선택된다.
- **Actual Result**: 선택한 카테고리가 올바르게 선택된다.
- **Status**: 완료


### Test Case H_09
- **Test Case ID**: TC_H_09
- **Title**: 새로운 후기 등록하기 별점 입력 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 새로운 후기 등록하기 페이지 진입
- **Steps**:
  1. 주고싶은 별점의 별을 클릭한다
 - **Expected Result**:  
  - 주고싶은 별점만큼 별의 색이 표시된다.
- **Actual Result**: 주고싶은 별점만큼 별의 색이 표시된다.
- **Status**: 완료


### Test Case H_10
- **Test Case ID**: TC_H_10
- **Title**: 새로운 후기 등록하기 '후기 작성 완료' 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 새로운 후기 등록하기 페이지 진입 , TC_H_05, TC_H_06, TC_H_07, TC_H_08, TC_H_09
- **Steps**:
  1. '후기 작성 완료' 버튼을 클릭한다.
  2. 개인 피드에 적용 되었는지 확인한다.
 - **Expected Result**:  
  - 후기 작성한 메뉴,카테고리 등 개인 피드에 옳바르게 반영된다.
- **Actual Result**: 후기 작성한 메뉴,카테고리 등 개인 피드에 옳바르게 반영된다.
- **Status**: 완료



### Test Case H_11
- **Test Case ID**: TC_H_11
- **Title**: '같은 메뉴 먹기' 버튼 클릭 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 팀 피드 진입
- **Steps**:
  1. '같은 메뉴 먹기' 버튼을 클릭한다.
  2. '또 먹은 후기' 등록하기 페이지 진입.
  3. 식사 유형, 후기 사진 ,같이 먹은 사람 동일 비교.
 - **Expected Result**:  
  - 또 먹은 후기 페이지에 진입하고 식사 유형 등 선택한 메뉴와 같다.
- **Actual Result**: 또 먹은 후기 페이지에 진입하고 식사 유형 등 선택한 메뉴와 같다.
- **Status**: 완료


### Test Case H_12
- **Test Case ID**: TC_H_12
- **Title**: '또 먹은 후기' 페이지 내 후기, 별점 입력 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, TC_H_11
- **Steps**:
  1. 후기 칸에 후기 입력한다.
  2. 주고 싶은 별점을 클릭한다.
 - **Expected Result**:  
  - 후기가 옳바르게 입력되고 별점이 활성화 된다.
- **Actual Result**: 후기가 옳바르게 입력되고 별점이 활성화 된다.
- **Status**: 완료



### Test Case H_13
- **Test Case ID**: TC_H_13
- **Title**: '또 먹은 후기' 후기 작성 완료 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, TC_H_11, TC_H_12
- **Steps**:
  1. '후기 작성 완료' 버튼 클릭한다.
  2. 개인 피드에 적용 되었는지 확인한다.
 - **Expected Result**:  
  - 후기 작성한 메뉴,카테고리 등 개인 피드에 옳바르게 반영된다.
- **Actual Result**: 후기 작성한 메뉴,카테고리 등 개인 피드에 옳바르게 반영된다.
- **Status**: 완료


### Test Case H_14
- **Test Case ID**: TC_H_14
- **Title**: 팀 피드 내 음식 성향 수정 버튼 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 팀 피드 페이지 진입
- **Steps**:
  1. '음식 성향' 수정 버튼
  2. 프로필 정보 수정 페이지 열림
 - **Expected Result**:  
  - 수정 버튼 클릭 후 프로필 정보 수정 페이지가 열린다.
- **Actual Result**: 수정 버튼 클릭 후 프로필 정보 수정 페이지가 열린다.
- **Status**: 완료


### Test Case H_15
- **Test Case ID**: TC_H_15
- **Title**: 음식 성향 스크롤 설정 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 팀 피드 페이지 진입 , TC_H_14
- **Steps**:
  1. 단맛, 짠맛, 매운 맛 원하는 수치 만큼 스크롤
 - **Expected Result**:  
  - 원하는 수치만큼 스크롤이 반영 된다.
- **Actual Result**: 원하는 수치만큼 스크롤이 반영 된다.
- **Status**: 완료


### Test Case H_16
- **Test Case ID**: TC_H_16
- **Title**: 음식 성향 입력 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 팀 피드 페이지 진입 , TC_H_14
- **Steps**:
  1. 좋아하는 음식 성향 칸 입력
  2. 싫어하는 음식 성향 칸 입력
 - **Expected Result**:  
  - 입력한 대로 적용된다.
- **Actual Result**: 입력한 대로 적용된다.
- **Status**: 완료


### Test Case H_17
- **Test Case ID**: TC_H_17
- **Title**: 프로필 수정 완료 테스트
- **Precondition**: 로그인 , 개발 2팀 선택, 팀 피드 페이지 진입 , TC_H_14,  TC_H_15 , TC_H_16
- **Steps**:
  1. 프로필 수정 완료 버튼 클릭한다.
  2. 성향 점수가 1점 미만일 때 "맛에 대한 성향은 최소 1 이상 설정해주세요" 문구가 뜬다.
  3. 성향 칸 내용이 10자 미만일 경우 "10자 이상 입력해주세요" 문구가 뜬다.
  4. 모두 만족 시 창이 종료 되고 팀 피드에 반영된다.
 - **Expected Result**:  
  - 상황에 맞는 문구가 발생하고 팀 피드에 반영된다.
- **Actual Result**: 상황에 맞는 문구가 발생하고 팀 피드에 반영된다.
- **Status**: 완료