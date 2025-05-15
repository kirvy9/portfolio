@echo off
REM 명령어 실행 내용을 화면에 표시하지 않습니다. 배치 파일 실행 시 불필요한 명령어 출력을 숨깁니다.

chcp 65001 > nul
REM 콘솔 코드 페이지를 UTF-8(65001)로 설정합니다. 한글 등 다국어 문자가 깨지지 않도록 합니다.
REM '> nul'은 이 명령의 출력 메시지를 화면에 표시하지 않도록 합니다.

setlocal enabledelayedexpansion
REM 지역 변수 환경을 설정하고, 지연된 환경 변수 확장을 활성화합니다.
REM 이를 통해 같은 블록 내에서 변경된 변수 값을 !변수명! 형식으로 즉시 사용할 수 있습니다.
REM 일반적인 %변수명% 형식은 전체 블록이 실행되기 전에 확장되어 변경된 값을 바로 사용할 수 없습니다.

REM ============================================
REM JMeter 테스트 실행 스크립트
REM ============================================

REM 배치 파일 디렉토리를 기준으로 경로 설정
REM 현재 실행 중인 배치 파일이 위치한 디렉토리 경로를 SCRIPT_DIR 변수에 저장합니다.
set SCRIPT_DIR=%~dp0

REM JMeter 설치 경로 설정 (사용자 입력 또는 기존값 사용)
if exist "%SCRIPT_DIR%jmeter_path.txt" (
    REM 파일에서 JMeter 설치 경로를 읽어 JMETER_HOME 변수에 저장합니다.
    set /p JMETER_HOME=<"%SCRIPT_DIR%jmeter_path.txt"
) else (
    REM jmeter_path.txt 파일이 존재하지 않으면
    REM 중요: 아래 JMETER_HOME 경로는 예시이며, 실제 JMeter 설치 경로로 수정해야 합니다.
    REM 경로에 공백이 있다면 set "JMETER_HOME=경로 위드 스페이스" 처럼 변수명과 등호까지 포함해서 쌍따옴표로 묶으세요.
    set JMETER_HOME=C:\Users\user\Downloads\apache-jmeter-5.6.3
    REM 설정된 (또는 위에서 수정한) JMeter 경로를 jmeter_path.txt 파일에 저장하여 다음 실행 시 사용합니다.
    (echo %JMETER_HOME%)>"%SCRIPT_DIR%jmeter_path.txt"
    echo JMeter 경로가 저장되었습니다. 다음 실행 시에는 이 단계를 건너뜁니다.
    echo 저장된 경로: %JMETER_HOME% (파일: %SCRIPT_DIR%jmeter_path.txt)
)

REM 테스트 파일 및 결과 경로 설정 (상대 경로)
REM 실행할 JMeter 테스트 계획 파일(.jmx)의 경로를 설정합니다.
set TEST_PLAN=%SCRIPT_DIR%realworld.jmx
REM 테스트 결과 파일 및 보고서가 저장될 디렉토리 경로를 설정합니다.
set RESULTS_DIR=%SCRIPT_DIR%test-results

echo ============================================
echo JMeter 테스트 실행
echo ============================================
REM 설정된 JMeter 경로를 화면에 표시합니다.
echo JMeter 경로: %JMETER_HOME%
REM 설정된 테스트 계획 파일 경로를 화면에 표시합니다.
echo 테스트 파일: %TEST_PLAN%
REM 설정된 결과 저장 디렉토리 경로를 화면에 표시합니다.
echo 결과 디렉토리: %RESULTS_DIR%
echo ============================================
echo.

REM 테스트 파일 존재 확인
REM 테스트 계획 파일(.jmx)이 실제로 존재하는지 확인합니다.
if not exist "%TEST_PLAN%" (
    echo 오류: 테스트 파일이 존재하지 않습니다: %TEST_PLAN%
    REM 사용자가 키를 누를 때까지 대기합니다.
    pause
    REM 오류 코드 1과 함께 스크립트를 종료합니다.
    exit /b 1
)

REM 결과 디렉토리 생성
REM 결과 저장 디렉토리가 없으면 새로 생성합니다.
if not exist "%RESULTS_DIR%" mkdir "%RESULTS_DIR%"

REM 테스트 모드 선택
echo 테스트 모드를 선택하세요:
echo 1. 일반 부하 테스트 (Load Test) - 100명 사용자, 30초 램프업, 5회 반복
echo 2. 스트레스 테스트 (Stress Test) - 150명 사용자, 45초 램프업, 3회 반복
echo 3. 스파이크 부하 테스트 (Spike Test) - 200명 사용자, 5초 램프업, 1회 반복
echo 4. 모든 테스트 실행
REM 사용자로부터 실행할 테스트 모드를 입력받습니다.
set /p TEST_MODE="선택 (1-4): "

REM 각 테스트 모드 스레드 그룹 활성화 여부 변수 초기화 (기본값: 비활성화)
set LOAD_ENABLED=false
set STRESS_ENABLED=false
set SPIKE_ENABLED=false

REM 사용자가 '1' (일반 부하 테스트)을 선택한 경우
if "%TEST_MODE%"=="1" (
    echo 일반 부하 테스트 실행 중...
    REM 결과 파일(.jtl), JMeter 로그 파일, HTML 보고서 디렉토리 이름을 설정합니다.
    set RESULT_FILE=%RESULTS_DIR%\result_load_test.jtl
    set LOG_FILE=%RESULTS_DIR%\jmeter_load_test.log
    set REPORT_DIR=%RESULTS_DIR%\report_load_test
    REM 일반 부하 테스트 스레드 그룹을 활성화합니다.
    set LOAD_ENABLED=true
REM 사용자가 '2' (스트레스 테스트)를 선택한 경우
) else if "%TEST_MODE%"=="2" (
    echo 스트레스 테스트 실행 중...
    REM 결과 파일(.jtl), JMeter 로그 파일, HTML 보고서 디렉토리 이름을 설정합니다.
    set RESULT_FILE=%RESULTS_DIR%\result_stress_test.jtl
    set LOG_FILE=%RESULTS_DIR%\jmeter_stress_test.log
    set REPORT_DIR=%RESULTS_DIR%\report_stress_test
    REM 스트레스 테스트 스레드 그룹을 활성화합니다.
    set STRESS_ENABLED=true
REM 사용자가 '3' (스파이크 부하 테스트)를 선택한 경우
) else if "%TEST_MODE%"=="3" (
    echo 스파이크 부하 테스트 실행 중...
    REM 결과 파일(.jtl), JMeter 로그 파일, HTML 보고서 디렉토리 이름을 설정합니다.
    set RESULT_FILE=%RESULTS_DIR%\result_spike_test.jtl
    set LOG_FILE=%RESULTS_DIR%\jmeter_spike_test.log
    set REPORT_DIR=%RESULTS_DIR%\report_spike_test
    REM 스파이크 부하 테스트 스레드 그룹을 활성화합니다.
    set SPIKE_ENABLED=true
REM 사용자가 '4' (모든 테스트 실행)를 선택한 경우
) else if "%TEST_MODE%"=="4" (
    echo 모든 테스트 모드 실행 중...
    REM 모든 테스트용 결과 파일(.jtl), JMeter 로그 파일, HTML 보고서 디렉토리 이름을 설정합니다.
    set RESULT_FILE=%RESULTS_DIR%\result_all_tests.jtl
    set LOG_FILE=%RESULTS_DIR%\jmeter_all_tests.log
    set REPORT_DIR=%RESULTS_DIR%\report_all_tests
    REM 모든 테스트 스레드 그룹을 활성화합니다.
    set LOAD_ENABLED=true
    set STRESS_ENABLED=true
    set SPIKE_ENABLED=true
REM 사용자가 1-4 이외의 값을 입력한 경우
) else (
    echo 잘못된 선택입니다. 스크립트를 종료합니다.
    REM 사용자가 키를 누를 때까지 대기합니다.
    pause
    REM 오류 코드 1과 함께 스크립트를 종료합니다.
    exit /b 1
)

REM JMeter 실행 파일 확인
REM Windows용 JMeter 실행 파일 경로를 설정합니다.
set JMETER_EXE=%JMETER_HOME%\bin\jmeter.bat
REM jmeter.bat 파일이 존재하지 않으면
if not exist "%JMETER_EXE%" (
    REM Linux/macOS용 JMeter 실행 파일 경로를 설정해봅니다. (이 스크립트는 .bat이므로 주로 Windows용)
    set JMETER_EXE=%JMETER_HOME%\bin\jmeter
    REM jmeter (확장자 없음) 파일도 존재하지 않으면
    if not exist "%JMETER_EXE%" (
        echo 오류: JMeter 실행 파일을 찾을 수 없습니다: %JMETER_EXE%
        echo JMeter 설치 경로를 확인하세요: %JMETER_HOME%
        echo jmeter_path.txt 파일을 삭제하고 스크립트를 다시 실행하면 경로를 재설정할 수 있습니다.
        REM 사용자가 키를 누를 때까지 대기합니다.
        pause
        REM 오류 코드 1과 함께 스크립트를 종료합니다.
        exit /b 1
    )
)

REM JMeter 실행 명령 생성
REM JMeter 실행 명령어의 기본 부분을 구성합니다.
REM -n: non-GUI 모드로 JMeter 실행
REM -t "%TEST_PLAN%": 사용할 테스트 계획 파일 지정
REM -l "%RESULT_FILE%": 결과 데이터를 저장할 JTL 파일 지정
REM -j "%LOG_FILE%": JMeter 실행 로그를 저장할 파일 지정
REM -e: 테스트 종료 후 HTML 대시보드 보고서 생성
REM -o "%REPORT_DIR%": 생성된 HTML 보고서를 저장할 디렉토리 지정
set JMETER_CMD="%JMETER_EXE%" -n -t "%TEST_PLAN%" -l "%RESULT_FILE%" -j "%LOG_FILE%" -e -o "%REPORT_DIR%"

REM 스레드 그룹 활성화/비활성화 매개변수 추가
REM JMeter 속성(-J)을 사용하여 JMX 파일 내의 사용자 정의 변수(스레드 그룹 활성화 여부)를 전달합니다.
set JMETER_CMD=%JMETER_CMD% -JloadTestEnabled=%LOAD_ENABLED% -JstressTestEnabled=%STRESS_ENABLED% -JspikeTestEnabled=%SPIKE_ENABLED%

echo JMeter 테스트 실행 중... 잠시 기다려주세요.
REM 실제로 실행될 전체 JMeter 명령어를 화면에 표시합니다.
echo %JMETER_CMD%
echo.

REM JMeter 실행
REM 구성된 JMeter 명령어를 실행합니다.
%JMETER_CMD%

REM 실행 결과 확인
REM 이전 명령어(JMeter 실행)의 종료 코드가 0이면 (성공)
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ============================================
    echo 테스트가 성공적으로 완료되었습니다!
    echo ============================================
    REM 결과 파일, 로그 파일, 보고서 디렉토리 경로를 화면에 표시합니다.
    echo 결과 파일: %RESULT_FILE%
    echo 로그 파일: %LOG_FILE%
    echo HTML 보고서: %REPORT_DIR%
REM 종료 코드가 0이 아니면 (오류 발생)
) else (
    echo.
    echo ============================================
    echo 테스트 실행 중 오류가 발생했습니다.
    REM 로그 파일을 확인하도록 안내합니다.
    echo 로그 파일을 확인하세요: %LOG_FILE%
    echo ============================================
)

REM HTML 보고서 열기
echo.
REM 사용자에게 HTML 보고서를 열지 여부를 묻습니다.
set /p VIEW_REPORT="HTML 보고서를 지금 열어보시겠습니까? (Y/N): "
REM 사용자가 'Y' 또는 'y'를 입력하면 (대소문자 구분 안 함)
if /i "%VIEW_REPORT%"=="Y" (
    REM 보고서 파일이 실제로 생성되었는지 확인
    if exist "%REPORT_DIR%\index.html" (
        REM 생성된 HTML 보고서의 메인 파일(index.html)을 기본 웹 브라우저로 실행합니다.
        start "" "%REPORT_DIR%\index.html"
    ) else (
        echo HTML 보고서 파일(%REPORT_DIR%\index.html)을 찾을 수 없습니다. JMeter 실행 중 오류가 있었을 수 있습니다.
    )
)

echo.
echo 스크립트를 종료합니다.
REM 사용자가 아무 키나 누를 때까지 대기한 후 스크립트를 완전히 종료합니다.
pause