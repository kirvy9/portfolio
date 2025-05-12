# 🧪 RealWorld QA 자동화 프로젝트

이 프로젝트는 [RealWorld](https://github.com/gothinkster/realworld) 애플리케이션을 대상으로 테스트 자동화를 수행하기 위한 QA 프로젝트입니다.  
해당 애플리케이션은 Medium.com의 클론 형태로, 실제 웹 애플리케이션 개발과 QA 테스트 전략 수립에 필요한 지식을 실습하기 위한 목적으로 사용됩니다.

---

## 📌 프로젝트 구성

- **대상 서비스:** RealWorld (Conduit) - https://demo.realworld.io
- **프론트엔드:** React + Redux
  - https://github.com/gothinkster/react-redux-realworld-example-app
- **백엔드:** Node.js + Express
  - https://github.com/gothinkster/node-express-realworld-example-app
- **인증 방식:** JWT 기반 인증 (헤더에 토큰 포함)

---

## ✅ 테스트 대상 핵심 기능

- 회원가입 / 로 / 로그아웃
- 사용자 프로필 조회 및 수정
- 게시글 작성, 수정, 삭제
- 댓글 작성, 삭제
- 태그 필터링, 인기 태그 조회
- 즐겨찾기 및 팔로우 기능

---

## ⚙️ 개발 및 테스트 환경

- Python 3.8+
- `pytest`
- `selenium`
- `webdriver-manager`
- `pytest-html`
- `pytest-xdist`
