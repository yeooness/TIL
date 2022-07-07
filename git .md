# 💻 Git 

> 분산형 버전 관리 시스템



## 기본 명령어

### init

- `git init`으로 저장소 생성

  - (Master) 확인하기


### add

- `git add 파일명`

  커밋할 파일들을 staged 상태로 변경

- `git add .`

  모든 변경 내용 추가 

### restore

- `gid restore 파일명`

  파일의 내용을 마지막 커밋상태로 되돌림

### commit 

- `git commit -m '<커밋메시지>'`

  커밋 (버전 기록)

### status

- `git status`

  untracked, unmodified, modified, staged 상태 확인

### log

- `git log`

  현재 저장소에 기록된 커밋을 조회

- 다양한 옵션을 통해 로그를 조회할 수 있음

  - `git log -1` : 가장 최근 1개를 보여줘
  - `git log --oneline` : 한 줄로 보여줘
  - `git log -2 --oneline` : 최근 2개를 한 줄로 보여줘

  
