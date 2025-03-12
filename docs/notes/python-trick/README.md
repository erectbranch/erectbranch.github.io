<div width="100%" height="100%" align="center">
  
<h1 align="center">
  <p align="center">슬기로운 파이썬 트릭</p>
  <a href="https://ebook.insightbook.co.kr/book/72">
    <img width="50%" src="https://raw.githubusercontent.com/erectbranch/Python_Trick/master/cover.jpg" />
  </a>
</h1>
  
<b>댄 베이더 저 · 전석환 역</b></br>
인사이트 · 2019년 01월 29일 출시</b> 

</div>

## :bulb: 목표

- **파이썬 코드 작성법을 공부한다.**

  > 파이썬 코드 예제를 보며 파이썬 코드 작성법을 공부한다.

</br>

## 🚩 정리한 문서 목록

 - [클래스, 클래스 메서드](notes/python-trick/ch04.md)

   > is vs ==, \_\_str\_\_ vs \_\_repr\_\_, copy.deepcopy

   > 사용자 예외 클래스, 추상 클래스(ABC), namedtuple, instance method vs classmethod vs staticmethod

 - [반복문, 이터레이션](notes/python-trick/ch06.md)

   > range(), 불필요한 index 제거하기, enumerate()

   > 딕셔너리 순회, 중첩 딕셔너리 순회, 중첩 딕셔너리 클래스화

- [타이핑, 정적 타입 검사](notes/python-trick/ch09.md)

   > mypy, typing.Union, typing.Optional, typing.List/Tuple/Dict, typing.Callable

   > typing.Generator, typing.Iterator, typing.TypeVar

   > 전방 참조 방지(annotations)

</br>

## :mag: 목차

### 1장 소개

    1.1 파이썬 트릭이란?
    1.2 이 책이 독자에게 알려 주는 것
    1.3 이 책을 읽는 방법

### 2장 파이썬 코드를 정돈하기 위한 패턴

    2.1 assert 문으로 방어하기
    2.2 보기 좋은 쉼표 배치
    2.3 콘텍스트 매니저와 with 문
    2.4 밑줄 문자와 던더
    2.5 문자열 형식화에 관한 충격적인 진실
    2.6 “파이썬의 선” 이스터 에그

### 3장 효과적인 함수

    3.1 파이썬 함수는 일급 객체다
    3.2 람다는 단일 표현식 함수다
    3.3 데코레이터의 힘
    3.4 *args와 **kwargs를 재미있게 활용하기
    3.5 함수 인자 풀기
    3.6 반환할 것이 없는 경우

### 4장 클래스와 객체 지향 프로그래밍

    4.1 객체 비교: ‘is’ 대 ‘==’
    4.2 문자열 변환(모든 클래스는 __repr__이 필요하다)
    4.3 자신만의 예외 클래스 정의하기
    4.4 재미있고 이득이 되는 객체 복제하기
    4.5 추상화 클래스는 상속을 확인한다
    4.6 네임드튜플은 어디에 적합한가
    4.7 클래스 변수 대 인스턴스 변수의 함정
    4.8 인스턴스 메서드, 클래스 메서드, 정적 메서드의 신비를 풀다

### 5장 파이썬의 일반 데이터 구조

    5.1 딕셔너리, 맵, 해시 테이블
    5.2 배열 데이터 구조
    5.3 레코드, 구조체, 데이터 전송 객체
    5.4 세트와 멀티세트
    5.5 스택(LIFO)
    5.6 큐(FIFO)
    5.7 우선순위 큐

### 6장 반복과 이터레이션

    6.1 파이썬다운 반복문 작성하기
    6.2 내포식 이해하기
    6.3 리스트 분할 트릭과 스시 연산자
    6.4 아름다운 이터레이터
    6.5 제너레이터는 단순화된 이터레이터다
    6.6 제너레이터 표현식
    6.7 이터레이터 체인

### 7장 딕셔너리 트릭

    7.1 딕셔너리 기본값
    7.2 재미있고 효과도 좋은 딕셔너리 정렬
    7.3 딕셔너리로 switch/case 문 모방하기
    7.4 딕셔너리 표현식의 특이점
    7.5 딕셔너리를 병합하는 많은 방법
    7.6 보기 좋은 딕셔너리 출력

### 8장 파이썬다운 생산성 향상 기법

    8.1 파이썬 모듈과 객체 탐색
    8.2 virtualenv로 프로젝트 의존성 격리하기
    8.3 바이트코드 내부 엿보기
