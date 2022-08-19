# wanted_pre_onboarding


## Introduction
원티드 프리온보딩 백엔드 코스 4차 선발 과제 레포입니다.


</br>

## 구현 완료한 요구 사항
- 채용 공고 등록
- 채용 공고 수정
- 채용 공고 삭제
- 채용 공고 목록 조회
- 채용 공고 검색
- 채용 공고 상세 조회


</br>

## DB Modeling

<img width="869" alt="image" src="https://user-images.githubusercontent.com/65996045/185530653-acce9b8e-bc0f-4bd0-9987-74794342516d.png">

</br>

## Technologies
- Python
- Django
- MySQL
- Git, Github


</br>

## Features

</br>

**Posting**
1. 채용 공고 등록 및 수정
  - View Class: PostingView
  - http method: POST
  - 채용 공고 등록 및 수정 API
  - update_or_create ORM으로 등록 및 수정 동시 구현
  - unit test 구현 완료
  
<br>
  
2. 채용 공고 삭제
  - View Class: PostingView
  - http method: DELETE
  - 채용 공고 삭제 API
  - unit test 구현 완료

<br>
  
3. 채용 공고 상세 조회
  - View Class: PostingView
  - http method: GET
  - 채용 공고 상세 조회 API
  - 채용 공고를 올린 회사의 다른 채용 공고들의 ID도 반환
  - unit test 구현 완료

<br>
  
4. 채용 공고 검색
  - View Class: PostingSearchView
  - http method: GET
  - 회사 이름으로 채용 공고 검색 API
  - unit test 구현 완료

<br>
  
5. 채용 공고 목록 조회 
  - View Class: PostingListView
  - http method: GET
  - 회사 ID를 받아 해당 회사의 모든 채용 공고 보여주는 API
  - unit test 구현 완료

</br>


