## wanted-pre-onboarding-backend

**프리온보딩 백엔드 인턴십 선발과제**

> 언어 및 프레임워크 : Python 3.10 & Django 5.0, DRF 3.15 \
RDBMS : sqlite3


### 개요
기업의 채용을 위한 웹 서비스의 API를 구현하였습니다. \
회사는 채용 공고를 생성하고, 사용자는 공고에 지원할 수 있습니다.

**목차**
1. [주요 기능](#주요-기능)
2. [ERD](#ERD)
3. [프로젝트 구조](#프로젝트-구조)
4. [개발 워크플로우 및 코드 품질 관리](개발-워크플로우-및-코드-품질-관리)

<br>

## 주요 기능
- 채용공고 등록
- 채용공고 수정
- 채용공고 삭제
- 채용공고 리스트 조회 및 검색
- 채용공고 상세 조회
- 채용공고 지원

<br>

### 기능 개발 문서화

<img width="1287" alt="API swagger" src="https://github.com/user-attachments/assets/4fc8cc35-40d4-422b-a53e-9a933684468f">

- [[Issues 1] 개발 환경 설정](https://github.com/Jihyun-Choi/wanted-pre-onboarding-backend/issues/1) \
	& [[PR 1] 개발 환경 설정](https://github.com/Jihyun-Choi/wanted-pre-onboarding-backend/pull/7)
- [[Issues 2]: User, Company 구현](https://github.com/Jihyun-Choi/wanted-pre-onboarding-backend/issues/2) \
	& [[PR 2] Feat: User, Company 기능 구현](https://github.com/Jihyun-Choi/wanted-pre-onboarding-backend/pull/8)
- [[Issues 3] 채용공고 기능 요구사항 구현](https://github.com/Jihyun-Choi/wanted-pre-onboarding-backend/issues/3) \
	& [[PR 3] Feat: 채용공고 기능 요구사항 API 구현](https://github.com/Jihyun-Choi/wanted-pre-onboarding-backend/pull/9)
- [[Issues 4] 채용공고 기능 선택사항 구현](https://github.com/Jihyun-Choi/wanted-pre-onboarding-backend/issues/4) \
	& [[PR 4] Feat: 채용공고 기능 선택사항 API 구현](https://github.com/Jihyun-Choi/wanted-pre-onboarding-backend/pull/10)
- [[Issues 5] 채용공고 지원 기능 선택사항 구현](https://github.com/Jihyun-Choi/wanted-pre-onboarding-backend/issues/5) \
	& [[PR 5] Feat: 채용공고 지원 기능 선택사항 API 구현](https://github.com/Jihyun-Choi/wanted-pre-onboarding-backend/pull/11)


<br>

## ERD
<img width="1386" alt="erd_image" src="https://github.com/user-attachments/assets/6451185a-f70b-4fb4-a86d-36a67c478fff">

<br>

## 프로젝트 구조

```bash
wanted-pre-onboarding-backend/
├── config/
├── user/
├── company/
├── recruitment
│   ├── admin.py
│   ├── models.py
│   │   ├── job_application.py
│   │   └── job_posting.py
│   ├── serializers.py
│   │   ├── job_application_serializer.py
│   │   ├── job_posting_create_serializer.py
│   │   ├── job_posting_detail_serializer.py
│   │   ├── job_posting_serializer.py
│   │   └── job_posting_update_serializer.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│       ├── job_application_create_api_view.py
│       └── job_posting_view_set.py
├── manage.py
├── Pipfile
├── Pipfile.lock
├── .flake8
├── .env
└── .gitignore

```

<br>

## 개발 워크플로우 및 코드 품질 관리

### 개발 프로세스

1. **Issues 생성**
   : 구현할 기능을 Issues에 작성합니다.

2. **브랜치 생성**
	: Issue에 맞춰 feature 브랜치를 생성합니다.

3. **기능 개발**
	: feature 브랜치에서 기능을 구현합니다.

4. **Pull Request 생성**
	: 개발이 완료되면 PR을 작성하여 변경 사항을 검토합니다.

5. **코드 리뷰 및 병합**
	: 리뷰 완료 후 main 브랜치에 병합합니다. \
	해당 프로젝트는 개인 개발 프로젝트로, self-review를 진행하였습니다.

### git branch 전략
- **Main branch** \
	배포 가능한 안정적이고 검증된 코드만 포함합니다.
	기능 개발이 완료된 코드가 병합됩니다.
- **Feature branch**  (`feat/{기능명}`): \
	새로운 기능 개발은 모두 feature 브랜치에서 진행합니다. \
	브랜치 이름은 feat/으로 시작하며, 개발 중인 기능을 명확히 알 수 있도록 작성합니다.

### git commit 컨벤션
- [feat]: 새로운 기능 추가
- [fix]: 코드 수정, 코드 포맷 변경
- [docs]: 문서 작성

### 코드 스타일 및 품질 관리
Black과 Flake8을 사용하여 코드 스타일의 일관성을 유지하고, 코드 품질을 관리하였습니다.
- Black
	자동 코드 포맷팅을 통해 일관된 코드 스타일 유지
- Flake8
	PEP 8 스타일 가이드를 준수하며, 코드 내 잠재적 오류와 스타일 위반을 사전에 방지
