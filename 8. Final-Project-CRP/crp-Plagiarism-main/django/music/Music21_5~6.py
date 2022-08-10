from music21 import *

#Music21 User Guide 5,6 레퍼런스 정리

#   2차원 , 3차원 리스트
#User Guide 5는 2차원 , 3차원 리스트에 대해 설명한다.
#아마 스트림과 리스트를 비교하려는 듯 하다.

note1 = note.Note("C4")
note1.duration.type = 'half'
note2 = note.Note("F#4")
note3 = note.Note("B-2")

stream1 = stream.Stream()
stream1.id = 'some notes'
stream1.append(note1)
stream1.append(note2)
stream1.append(note3)

biggerStream = stream.Stream()
note2 = note.Note("D#5")
biggerStream.insert(0, note2)
biggerStream.append(stream1)

#다음과 같은 스트림들이 있을 때 , 내부 요소를 알고 싶다면 .show() 밖엔 없었다.
biggerStream.show('text')

#스트림은 music21의 객체를 계층적 , 시간적으로 분리하고 구조화하고 배치할 수 있다.
#스트림 또는 스트림 하위 클래스를 다른 스트림에 배치 할 수 있는 것이다.

#이러한 스트림 객체의 배열은 악보를 표현하는 가장 일반적인 방식이다.
#music21에는 music21.corpus 모듈이 있다.
#이 모듈을 통해서 다양한 함수를 사용 가능하고 다양한 정보들을 얻어낼 수 있다.

#corpus.parse는 악보를 스트림으로 만들어준다.
sBach = corpus.parse('bach/bwv57.8')
print(sBach)

#corpus.parse를 통해 스코어를 확인 가능하다.
#스코어는 a Metadata object, a StaffGroup object, and four Part objects 로 구성된다.

print(len(sBach[3]))
print(len(sBach[3][1]))

#스코어가 리스트의 형태로 나올텐데 그럼 어떤게 어떤건지 어떻게 아냐는 것이다.
#그래서 이런 기억과 순서에 의존하는 필터링은 좋지 않다.
#앞서 배운 getElementsByClass() 메소드를 통해 요소를 기준으로 필터링 하자.

print(len(sBach.getElementsByClass(stream.Part)))
print(len(sBach.getElementsByClass(stream.Part)[0].getElementsByClass(stream.Measure)))
print(len(sBach.getElementsByClass(stream.Part)[0].getElementsByClass(
        stream.Measure)[1].getElementsByClass(note.Note)))
print(len(sBach.getElementsByClass('Part')))

alto = sBach.parts[1]  # parts count from zero, so soprano is 0 and alto is 1
#part는 소프라노 , 알토 같은 부분을 이야기 한다.
#즉 파트가 나눠진 악보 예를 들어 여럿이서 부른다면 소프라노 파트 , 알토 파트 여럿이서 노래를 부를 것이다.
#이런 부분에 대해서 있는 속성이 part 다.

excerpt = alto.measures(1, 4) #마디를 의미한다.
#excerpt.show("midi")
excerpt.show("text")
#파디를 1 ~ 4 부분 띄어내어서 살퍄본다.

measure2 = alto.measure(2)  # measure not measure_s_
measure2.show("text")
#띄어낸 부분에서 2번째 것이다.
#차이를 보면 단일 마디는 measure , 범위 마디는 measures 다.

measureStack = sBach.measures(2, 3)
measureStack.show("text")


#   스트림 에서의 재귀
#스트림은 스트림 안에 스트림이 들어 갈 수 있다.
#스트림의 각 하위의 레이어에 도달하기 위해 모든 요소들을 recurse() 라는 메소드가 방문한다.

s = stream.Score(id='mainScore')
p0 = stream.Part(id='part0')
p1 = stream.Part(id='part1')

m01 = stream.Measure(number=1)
m01.append(note.Note('C', type="whole"))
m02 = stream.Measure(number=2)
m02.append(note.Note('D', type="whole"))
p0.append([m01, m02])

m11 = stream.Measure(number=1)
m11.append(note.Note('E', type="whole"))
m12 = stream.Measure(number=2)
m12.append(note.Note('F', type="whole"))
p1.append([m11, m12])

s.insert(0, p0)
s.insert(0, p1)
s.show('text')

#결과
#{0.0} <music21.stream.Part part0>
#     {0.0} <music21.stream.Measure 1 offset=0.0>
#         {0.0} <music21.note.Note C>
#     {4.0} <music21.stream.Measure 2 offset=4.0>
#         {0.0} <music21.note.Note D>
# {0.0} <music21.stream.Part part1>
#     {0.0} <music21.stream.Measure 1 offset=0.0>
#         {0.0} <music21.note.Note E>
#     {4.0} <music21.stream.Measure 2 offset=4.0>
#         {0.0} <music21.note.Note F>

recurseScore = s.recurse()
print(recurseScore)
#print 해보니 iterator 쪽이다. for문을 활용해서 뜯어보자.

for el in s.recurse():
    print(el.offset, el, el.activeSite)

#recurse의 결과는 리스트를 호출 하는 것처럼 사용해야 한다.


#   스트림 평탄화
#스트림을 평탄화 한다는 것은 중첩된 스트림을 평탄화 한다고 생각하면 된다.
#.flatten() 메소드의 결과를 확인해보자.

for el in s.flatten():
    print(el.offset, el, el.activeSite)

#결과
# 0.0 <music21.note.Note C> <music21.stream.Score mainScore_flat>
# 0.0 <music21.note.Note E> <music21.stream.Score mainScore_flat>
# 4.0 <music21.note.Note D> <music21.stream.Score mainScore_flat>
# 4.0 <music21.note.Note F> <music21.stream.Score mainScore_flat>


#중첩된 스트림의 구조를 평탄화하면 플랫 속성이 액세스된 스트림의 컨텍스트에서
#적절한 위치를 반영하여 스트림의 각 요소에 대해 새로운 시프트 오프셋이 설정된다.
#이와는 별도로, 노트 오프셋은 편집되지 않았음을 인식하는 것이 중요하다.

