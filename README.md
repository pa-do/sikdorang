# 식도랑

- 목적 : 음식점 기반 여행 기획 및  추천 플랫폼
- 개발 기간 : 20.08.31 ~ 20.10.08 (6주)
- [배포링크](http://j3d202.p.ssafy.io/)



## 목차

- [1. 팀 구성원 및 업무 분장](#팀-구성원-및-업무-분장)

- [2. 와이어 프레임](#와이어-프레임)

- [3. DB 모델링](#DB-모델링)

- [4. 식도랑 시퀀스](#식도랑-시퀀스)

- [5. 핵심 기능](#핵심-기능)

- [6. 느낀점](#느낀점)



## 팀 구성원 및 업무 분장

#### 정승희

 - 팀장 / QA / 프론트
     - 프로젝트 관리 전반 및 스케줄링
     - 지도 API 및 프론트
     - 이미지 처리 및 텍스트 추출 방문 알고리즘( OpenCV + Tesseract OCR )



#### 박인영

- 테크리더 / 프론트
  - 최종 코드리뷰 담당
  - 모바일 웹 최적화



#### 박도희

- 기획 / 초기 DB 구축 / 프론트엔드 엔지니어
  - 45만개 음식점, 유저, 리뷰 정보를 응용한 초기 DB 구축
  - 드래그-앤-드롭을 활용한 일정 추가 기능 구현
  - 사용자 여행 생성 후 동행구하기 기능(CRUD) 구현


#### 조규성

- 풀스택
  - 형태소 분석
  - 디버깅



#### 허성수

- 백엔드 / 배포
  - DB 모델링 설계 및 API 로직 작성
  - EC2, Jenkins, Nginx, uwsgi 를 통한 배포



## 와이어 프레임

- [식도랑_와이어프레임.pdf](README_img/식도랑_와이어프레임.pdf) 

- [식도랑_와이어프레임2.pdf](README_img/식도랑_와이어프레임2.pdf) 

- [식도랑 와이어프레임3.pdf](README_img/식도랑_와이어프레임3.pdf)



## DB 모델링

![ERD](README_img/ERD.PNG)





## 식도랑 시퀀스

- [식도랑_시퀀스.md](README_img/식도랑_시퀀스.md)





## 핵심 기능

> **사용자와 연결된 태그, 카테고리를 필터링하여 음식점, 카페, 숙박, 관광지와 같은 여행 일정 추천 알고리즘 제공**
>
> 다이닝코드 식당 데이터, 한국관광공사 API를 사용하여 약 5만건의 데이터를 필터링
>
> 이상형 월드컵을 통해 초기 데이터 확보 및 코사인 유사도 분석으로 콜드스타트 문제 해결
>
> 카카오 map API를 사용하여 사용자가 고르거나 식도랑에서 추천받은 지점 자동으로 연결 및 거리 분석
>
> 리뷰를 쓰면 형태소 분석을 통해 리뷰에 사용한 글자 기반으로 사용자 태그 업데이트 구현
>
> IAMPORT API를 사용하여 이니시스, 카카오, 네이버페이 등 다양한 결제 시스템 구축
>
> Pytesserect, Open CV를 통해 영수증, 결제내역 분석으로 자동 방문 인증 구현



#### 구현기능

휴대폰 인증을 통한 가이드 권한 획득

사용자 여행 생성 후 동행구하기 활성화 가능

가이드일 경우 투어 생성을 통해 결제시스템 사용 가능

GeoLocation API를 통해 현재 위치 획득



---



## 느낀점

**정승희**

- 팀장과 QA의 역할에 대해 이해도가 높아졌다.
* 팀의 목표와 팀원들의 기능 구현 진척사항을 체크하며 스케줄링을 하고 다시 계획을 조정하는 과정을 통해 전체적으로 프로젝트의 진행에 대해 넓은 시각으로 보게 되었다.
* Vue에 대한 전반적인 올바른 사용자 방법과 의도, vuex사용 store화, 바스크립트 비동기처리에 대해 많이 배운 기회였다.
* OpenCV와 Tesseract OCR을 사용하여 이미지를 처리하고 text detection으로 방문 알고리즘을 구현하며 전체적으로 이미지 처리와 조작에 대해 많이 배웠다.
*  데이터 처리와 분석을 다뤄봐서 좋았지만  처리,분석,시각화를 더 심도있게 다뤄보지 못해서 아쉽다.



**박도희**

- 주어진 데이터의 카테고리와 리뷰를 koNLPy의 Komoran을 활용해 명사 단위로 나누고 이를 활용해 카테고리, 태그 사전을 만들고, 맛집 추천에 활용할 데이터만을 추려 피클(.pkl) 파일을 생성하는 과정까지의 과정이 작은 도전이었다. 하나씩 해나가는 과정에서 성취감뿐 아니라 재미도 느낄 수 있었다.
- draggable이라는 vue 오픈소스를 활용해 일정 생성의 드래그-앤-드롭을 구현했다. 크롬 개발자도구에서 모바일 크기의 화면으로 테스트할 때는 문제가 없었으나 배포 후 실제 모바일에서 화면을 확인했을 때, 손으로 하나의 일정 버튼을 누르게 되면 해당 일정 이후의 몇 개의 일정이 함께 사라지는 문제가 발생했다. 구글링을 통해 문제를 해결할 수 있었지만, 모바일 웹 기반의 프로젝트를 진행하면서 컴퓨터와 모바일에서의 차이를 고려하지 못하고 웹에서만 디버깅을 진행했었던 점이 아쉽다.
- Vue를 활용한 두 번째 프로젝트로, Vuex의 사용뿐 아니라 store 처리, 자바스크립트의 비동기처리에 대해 고민해볼 수 있었다. 프로젝트를 마무리할 때쯤 store에 같은 역할을 하는 변수를 팀원들이 각자 만들었다는 사실을 발견하고 수정 작업을 진행했는데, 이러한 일이 일어나지 않게 하기 위한 의사소통의 중요성을 깨달았다.



**박인영**

- PC 웹과 달리 모바일 웹은 화면이 작기때문에 사용자에게 필요한 기능을 깔끔하게 보여주는 것이 중요하다는 것을 느꼈다.
- 이 버튼이 메인 화면에 있어야할지, 마이페이지에 있어야할지 같은 UI/UX 측면의 고민을 많이 했다.
- 많은 양의 데이터를 다루기 때문에 데이터 시각화와 같이 사용자에게 직관적으로 데이터를 보여줄 수 있는 기능도 기대했는데,
- 이 외에 필요한 기능이 생각보다 많아서 다뤄보지 못한 점이 아쉬웠다.



**조규성**

- 디버깅에 엄청 익숙해졌다. 자바스크립트의 동작, 특히 비동기처리에대해 고민해볼 수 있었다.

- 뷰의 장점인 컴포넌트화, 데이터 중앙처리에 부족함이 많이 느껴져서 안타까웠다.

- 리뷰 형태소 분석 후에 유의미한 데이터로 저장하는 과정이 흥미로웠다.



**허성수**

- Rest-framework의 역할과 Django기반의 백 구성에 대해 많이 고민했고 배웠다

- Ubuntu 기반 Vue.js와 Django 배포에 대해 배웠고 프록시 설정법 또한 배운 기회가 되었다

- HTTPS를 구성할 때 SSL 인증 방식과 접근 권한, 데이터 폼 처리에 대해 고민해 볼 수 있었다.



---
