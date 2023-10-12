# flask란

    - 파이썬 기반 웹서비스를 구현하는 패키지
        - 분석 기반 서비스, AI기반 서비스 등등
            - 차트가 동반, 데이터 표현 등등
            - 분석 파이썬 + 서비스(웹) 파이썬 -> 동일 언어
    - 종류
        - Django
            - 프레임웍기반, 대부분 프로젝트 구조가 자동으로 생성
            - 상대적으로 느리다.
            - 개발을 빠르게 구축할 수 있다. -> 국내에서 선호, 추세는 변경중
            - 스타일이 자바진영의 Spring과 유사
        - flask
            - 자유도가 높다. 처음부터 모든것을 직접 다 만든다.
            - 가볍고, 빠르게 구축이 가능함.
            - 미국쪽에서 선호함.
            - ex) 주피터 노트북,
            - 스타일이 JS진영의 node.js 와 유사하다
        - fastAPI
            - 모델 서빙쪽 등 추세를 넓혀가는 중
            - 가장 빠름

# 설치

    - 가상환경구축
        - 한대의 머신에서 여러개의 프롲게트 혹은 서비스 가동시 특정 패키지들의 버전이 충돌됨을 방지
            -> 격리시킨다. 샌드박스
        - 가상환경 생성 (현재 프로젝트 위치에서 수행)
            - python -m venv was
        -활성화
            - 윈도우 기준 활성화 파일 위치
                - cmd 에서  cd  ./was/Scripts
                - activate
                - (was) 프롬프트(경로) 로 바뀜
                    - (was) > pip list
    - 필요한 패키지 설치 -> 특정버전 (개발시) 기록 -> requirements.txt
        - 명령어로 생성하기
            - pip freeze > requirements.txt
        - 필요한 것만 카피해서 로컬 requirements.txt 수정

        - (was)> pip install -r requirements.txt
            - txt 경로는 상황에 맞추어서 조정
        - pip install flask
        - pip list

    -0- 요약
        - C:\Users\USER\Desktop\projects>
        - C:\Users\USER\Desktop\projects> python -m venv was
        - C:\Users\USER\Desktop\projects> cd was/Scripts
        - C:\Users\USER\Desktop\projects\was\Scripts> activate
        - C:\Users\USER\Desktop\projects\was\Scripts> ../..
        - (was) C:\Users\USER\Desktop\projects> pip install -r ./flask/requirements.txt
        - (was) C:\Users\USER\Desktop\projects> pip list
    이것을 간단히 하려면 Docker를 배워서 하면 된다.

# 최초코드
    - f1.py 참고
    - template.py 파일을 기본형으로 사용한다.

# 웹서비스 (3-tier)

    - 프런트(혹은 클라이언트 사이드)
        - HTML5 : 콘텐츠 , 뼈대 => 데이터가 존재
            - 데이터
        - css3 : 레이아웃, 디자인, 애니메이션, 반응형
            - css selector, xpath,
            - bootstrap, 이미완성된 디자인 모듈 활용
                - https://adminlte.io/
        - javascript : 인터렉션담당, 이벤트, 통신, 동적구성
            - javascript > es next(2015) > typescript => SPA
                - react, angular, vue
            - 클라이언트 -> 서버로 데이터를 보내는 방법
                - form 전송 -> 로그인등등, 화면 껌벅
                - ajax 통신 -> 백그라운드 통신
                - 웹소켓 -> 백그라운드 통신, 쌍방향통신, 푸시 -> 챗봇 베이스
    - 백엔드(혹은 서버 사이드)
        - flask
            - 같은포지션 : django, fastapi, springboot, nodejs, ...
    - 데이터베이스
        - RDBMS
            - Mysql, Maria, Oracle,
        - No SQL
            - MongoDB, redis ..

# 프로젝트 구조

    /
    L basic.py : flask를 익히기위한 예제
        L f1.py
        L f2.py
        L template.py
    L app.py    : 서비스 엔트리 포인트()
    L static  : 정적 데이터가 위치하는 것, 라우팅 필요없음(바로인식이 가능)
              : *.js *.css, *.이미지파일(png, jpeg... )
    L templates : html 위치,
        L index.html
    L requirements.txt : 해당 프로젝트에서 사용하는 라이브러리
    L readme.MD : 설명파일
