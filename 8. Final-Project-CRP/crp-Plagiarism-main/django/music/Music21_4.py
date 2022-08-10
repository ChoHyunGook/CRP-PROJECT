import music21

#Music21 User Guide 4 레퍼런스 정리

#   다수의 오브젝트를 리스트로 처리

note1 = music21.note.Note("C4")
note2 = music21.note.Note("F#4")

note1.duration.type = 'half'
print(note1.duration.quarterLength)

#음표의 옥타브 없이 음 자체만을 알려면 step 속성을 확인한다.
print(note1.step)
print(note2.step)

#악보는 음의 시퀀스로 구성될텐데 , 리스트를 활용해서 표현하고 음을 다룰 수도 있다.
noteList = [note1, note2]
print(noteList)

#객체로 표현되는 것이 보기 그렇다면 당연하게도 다음과 같이도 가능하다.
for thisNote in noteList:
    print(thisNote.step)

#파이썬에서 리스트 즉 시퀀스 자료형을 활용하는 것과 같이 note 하나하나도 모두 가능하다.
#다음 B플랫 음을 만들고 리스트 안에 넣을 수도 있다.
note3 = music21.note.Note("B-2")
noteList.append(note3)

print(len(noteList))
for thisNote in noteList:
    print(thisNote.step)

#달라진 것을 확인 할 수 있다.

#리스트에서 사용되는 기본적인 메소드들과 함께도 사용된다.
print(noteList[0])
print(noteList.index(note2))
print(noteList[-1])


#   스트림 ( Stream ) 오브젝트
#스트림 객체와 그 서브클래스 Score , Part , Measure은 Note, Chord, Clef, TimeSignature objects 와 같은
#music21의 기본 컨테이너다.
#이 컨테이너는 파이썬의 리스트 처럼 작동한다.

#스트림에 저장되는 객체는 시간간격이 지정된다.
#4분음표수를 나타내는 offset 오프셋 으로 표현된다.
#예를 들어 , 4분의 4박자에서 2분음표가 2개 있다면 처음 음표의 오프셋은 0.0 두번째는 2.0이 될 것이다.

#또한 스트림은 다른 스트림을 저장할 수도 있으며 , 다양한 중첩 구조 , 순서 구조 및 시간 구조를 사용가능하다.
#이런식으로 저장된 스트림에도 오프셋은 존재한다.

#보통 스트림의 서브클래스에는 Score , Part , Measure가 있다.
#이 서브클래스를 스트림에 넣는 다고 생각하는 것이 좋다.
#우리가 만약 2분음표 2개를 넣고 싶다면 스트림에 넣는 방식으로 하게 될 것이다.

#Music21의 또다른 특징은 바로 Music21의 객체를 다른 Stream에 저장 가능하다는 것이다.
#즉 참조 할 수 있다는 것을 이야기 한다.
#즉 어느 스트림에서 어느 부분을 가져왔다면 새로운 스트림을 만든 것이 아닌 참조 했다는 것이다.
#그래서 변경 내용은 원본 스트림에도 영향을 미치게 된다.


#   기본 스트림 만들기
#기본적으로 스트림에는 music21 객체들이 들어가게 된다.
#만약 다른 객체를 넣고 싶다면 다른 방식을 사용해여야 한다. ( ElementWrapper )

#스트림은 개별적인 요소들을 순서대로 보관한다는 점에서 파이썬의 리스트와 비슷하다.
#하지만 넣을 수 있는 요소들이 music21 객체들에 한정되어있다는 점이 다르다.

#다음과 같이 stream을 하나 만들 수 있다.
stream1 = music21.stream.Stream()

#스트림에 노트를 넣는 방식은 다음과 같다.
#리스트와 비슷하게 append함수를 통해 note를 넣어줄 수 있다.
stream1.append(note1)
stream1.append(note2)
stream1.append(note3)

#스트림에 음을 그럼 이렇게 일일이 넣어야 하느냐 하면 아니다.
#아래 코드처럼 repeatAppend( 넣고싶은 음 , 횟수 ) 를 통해 여러번의 음표를 넣는 작업을 수행할 수 있다.
#이 repeatAppend 메소드를 통해 추가된 음들은 모두 고유한 객체다.
#즉 파이썬의 copy.deepcopy를 생각하면 된다. ( 깊은 복사 )

stream2 = music21.stream.Stream()
n3 = music21.note.Note('D#5')
stream2.repeatAppend(n3, 4)
#stream2.show("midi")
#위의 show() 메소드를 확인하면 실제로 D#5음이 4번 나는 것을 확인 할 수 있다.

#다음과 같이 해당 스트림안에 객체가 몇개 있는지도 확인 가능하다.
print(len(stream1))

#또한 text로도 show() 메소드를 사용할 수 있따.
stream1.show('text')


#   스트림에 접근하기
#스트림 안의 객체들에 접근하기 위해서는 파이썬의 리스트 처럼 접근 할 수 있다.
for thisNote in stream1:
    print(thisNote.step)

#또한 리스트에서 가능했던 다양한 방식들도 스트림에서도 가능하다.
print(stream1[0])
print(stream1[-1].nameWithOctave)

#스트림 에서도 리스트와 비슷한 index() 메소드를 사용 가능하다.
note3Index = stream1.index(note3)
print(note3Index)

#또한 리스트에서의 pop() 과 같이 스트림에서도 pop() 이 가능하다.
stream1.pop(note3Index)
stream1.show('text') #확인해보면 가장 마지막 음 ( note3 ) 가 빠져있음을 알 수 있다.

#다시 append 하는 것도 가능하다.
stream1.append(note3)


#   .getElementsByClass()를 통한 클래스 별 요소 분리하기
#우리는 요소들의 클래스 , 오프셋 레인지 , 특정 식별자 등을 기준으로 요소들을 수집할 수 있다.
#스트림에서도 요소들의 이러한 특징들을 기반으로 스트림 안에서 요소들을 수집할 수 있다.
#.getElementsByClass() 메소드는 지정된 클래스의 인스턴스 혹은 서브클래스인 요소의 스트림에 대해 반복한다.
#다음 예제를 통해서 살펴보자.

#.getElementsByClass() 메소드를 통해 note들을 loop를 통해 확인한다.
#다음과 같이 .getElementsByClass() 는 요소의 클래스를 기준으로 스트림1 안의 요소들을 긁어왔고
#해당되는 요소들을 for문을 통해서 보여주고 있다.
for thisNote in stream1.getElementsByClass(music21.note.Note):
    print(thisNote, thisNote.offset)

for thisNote in stream1.getElementsByClass('Note'):
    print(thisNote, thisNote.offset)

#Rest라는 객체도 있는데 , 현재 이 안에는 Rest라는 객체가 없으니까 위와 같을 것이다.
#중요한 포인트는 이처럼 특정 클래스 기준으로 요소들을 긁어올 때 이러한 방식도 가능하다는 것이다.
for thisNote in stream1.getElementsByClass(['Note', 'Rest']):
    print(thisNote, thisNote.offset)

#리스트스럽게 이런 방식도 가능하다.
for thisNote in stream1.notes:
    print(thisNote)

#.notesAndRests는 .getElementsByClass(['Note', 'Chord', 'Rest']) 와 동일하다.
for thisNote in stream1.notesAndRests:
    print(thisNote)

#pitch는 조금 다른 점이 있긴하다.
#pitch는 note를 호출하면서 시작되지만 , 스트림 안에 있는 모든 Note나 Chord ( 코드 ) 에서의 pitch를 리턴한다.
listOut = stream1.pitches
print(listOut)

#.getElementsByClass() 의 결과는 스트림은 아니지만 .show() 메소드를 사용할 수 있다.
sOut = stream1.getElementsByClass(music21.note.Note)
sOut.show('text')

#만약 확실하게 하고 싶다면 뒤에 .stream()을 통해서 구현해도 된다.
sOut = stream1.getElementsByClass(music21.note.Note).stream()
sOut.show('text')


#   .getElementsByOffset()를 통한 offset으로 요소 긁어내기
#.getElementsByOffset()은 단일 오프셋이나 2개의 오프셋 사이의 범위에 대해 모든 요소의 스트림을 리턴한다.

#다음과 같은 경우 3 이므로 3 오프셋을 갖는 스트림이 리턴된다.
sOut = stream1.getElementsByOffset(3)
print(len(sOut))

#확인 한 결과 , 실제로 음 하나있는 스트림이 딸려 나온다.
print(sOut[0])

#위의 .getElementsByClass()에서 한 것과 마찬가지로 결과물을 stream으로 가져오고 싶다면 뒤에 .stream을 추가하면 된다.
sOut = stream1.getElementsByOffset(2, 3).stream()
sOut.show('text')



#   더 다양한 stream의 특징들
#지금까지 살펴본 stream은 리스트와 매우 흡사하다.
#하지만 고유하게 stream이 할 수 있는 일이 있기에 stream이 사용될 것이다.
#예를 들어 stream 고유의 메소드를 통해 해당 스트림의 음높이의 범위 ( 가장 낮은 음 ~ 가장 높은 음 ) 을 알 수도 있다.

#다음과 같은 방식으로 가능하다.
print(stream1.analyze('ambitus'))

#이처럼 stream은 다양하고 고유한 분석을 위한 메소드들을 많이 가지고 있다.

#note의 오프셋도 확인 가능하다.
print(note1.offset)
print(note2.offset)
print(note3.offset)

#음과 오프셋도 함께 볼 수 있다.
#스트림1 안에는 note객체들이 들어있을 것이고 그걸 thisNote에 넣어서 그 객체의 offset과 name을 함께 본 것이다.
for thisNote in stream1:
    print(thisNote.offset, thisNote.name)

#note2.offset 보다 note2.getOffsetBySite(stream1) 이 좁 더 안전한 방식인데 이는 나중에 알아보도록 하자.

#스트림에서 .lowestOffset 속성은 모든 요소에 대해 offset의 최소값을 반환한다.
print(stream1.lowestOffset)

#   디폴트 박자 ( 4/4박 등등 )
#음을 넣을 떄 왜 디폴트로 4/4박으로 설정되어있나 생각해 볼 수 있다.
#defaults.meterNumerator를 통해 분자 , defaults.meterDenominator를 통해 분모를 확인 가능하다.

print(music21.defaults.meterNumerator) # 4
print(music21.defaults.meterDenominator) # quarter = 4

#스트림을 식별하게 위해서는 .id로 식별 가능하다.
#id는 16진수 형태이다.

stream1.id = 'some_notes'
print(stream1)
#출력 해보니 <music21.stream.Stream some_notes> 로 내가 붙인 아이디가 뒤쪽에 붙여서 나온다.

#잊지 말아야할 속성이 있는데 바로 duration 이다.
#앞서 우리는 music21 객체들의 속성으로 duration이 존재한다는 것을 배웠다.

#따라서 stream도 duration 속성이 존재한다.
#다음과 같은 방식으로 확인 가능하다.
print(stream1.duration)

print(stream1.duration.type)
print(stream1.duration.quarterLength)

#여기서 헷갈리기 쉬운점은 len(stream) != stream.duration 이라는 점이다.
#즉 len(stream)은 stream안의 객체의 개수일 뿐 , 그 개수가 duration 즉 stream의 지속 시간을 의미하지는 않는다.
#굳이 duration과 비슷한 개념을 찾자면 스트림 안의 최신 요소가 종료되는 시간인 .highestTime 일 것이다.
#스트림의 가장 앞쪽의 offset + .quarterLength = .highestTime 이기 떄문이다.

print(stream1.highestTime)



#   스트림 안의 스트림

#앞서 스트림 안에 스트림을 넣을 수도 있다고 하였다.
biggerStream = music21.stream.Stream()
note2 = music21.note.Note("D#5")
biggerStream.insert(0, note2)

#스트림을 하나 만들고 그 안에 다른 스트림을 하나 넣어보자.
biggerStream.append(stream1)

#그리고 한번 구조가 어떻게 생겼는지 확인 해보자.
biggerStream.show('text')

#다음과 같이 나오는 것을 확인 할 수 있다.
#{0.0} <music21.note.Note D#>
#{1.0} <music21.stream.Stream some_notes>
#    {0.0} <music21.note.Note C>
#    {2.0} <music21.note.Note F#>
#    {3.0} <music21.note.Note B->

#여기서 주의할 점은 오프셋 부분이다.
#스트림 안의 스트림의 오프셋이 다음과 같은 것을 볼 수 있다.
#즉 외부 오프셋에 영향을 받는 것이 아닌 , 내부 오프셋으로 작동이 되고 있다는 것이다.
#그렇다면 통합적인 오프셋은 어떻게 읽어야 할까 생각하면 바로 내부 스트림 자체의 오프셋을 고려해야 한다는 것이다.
#음이 4개 존재하고 3개는 내부 오프셋 (0 , 2 , 3 ) 이다.
#내부 스트림의 오프셋이 1.0 이므로 뒤쪽에 1씩 더해져 다음과 같이 된다.
#0 , 1 , 3 , 4 로 통합적인 오프셋이라고 생각할 수 있는 것이다.

#그래서 안의 객체도 다음과 같이 판단한다.
print(note1 in stream1) # True
print(note1 in biggerStream) # False

#즉 note1 객체는 stream1에 있는 거고 biggerStream에는 다른 노트 1개와 stream1이 있는 것이므로 False다.
#즉 안에 스트림을 포함하고 있다고 하더라도 그 객체가 안에 있다는 뜻이 아니라는 것이다.


#Music21에서 악보는 스트림 안의 스트림 안의 스트림 구조로 만들어진다.
#예를 들어 바이올린 스트림과 비올라 스트림을 함께 다루기 위해 한 스트림 안에 넣을 수도 있고 ,
#다채로운 악보 구성을 위해 다양한 스트림을 구성하고 합치고 변형할 수 있다.