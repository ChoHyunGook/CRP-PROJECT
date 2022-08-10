from music21 import *

# Music21 User Guide 7 레퍼런스 정리

cMinor = chord.Chord(["C4", "G4", "E-5"])
# 다음과 같이 코드를 만들 수 있다.
# 코드는 여러 피치 오브젝트를 하나로 결합하여 만드는 객체이다.
# 가장 간단한 방법은 다음과 같이 코드 객체 안에 여러 피치 이름으로 이루어진 리스트를 전달하는 것이다.

# 코드와 노트는 모두 GeneralNote 의 서브클래스 이므로 다음과 같이 공유하는 부분이 존재한다.
cMinor.duration.type = 'half'
print(cMinor.quarterLength)

# 하지만 cMinor.pitch 는 불가능 하다.
# cMinor.pitches 는 가능하다.
print(cMinor.pitches)

# pitches는 tuple을 반환한다.

# 또한 해당 코드가 major인지 minor인지도 다음 메소드를 통해서 확인 가능하다.

print(cMinor.isMajorTriad())  # False
print(cMinor.isMinorTriad())  # True

# 코드가 인버전인지 아닌지도 확인 가능하다.
# 인버전 코드와 하이브리드 코드에 대한 내용
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=crom0720&logNo=70010072618

print(cMinor.inversion())  # 결과는 0

cMajor = chord.Chord(["E3", "C4", "G4"])
print(cMajor.inversion())  # 결과는 1

# root 즉 첫음도 확인 가능하다.
print(cMajor.root())

# bass 를 찾는다.
print(cMajor.bass())

# third 세번째 음이다.
print(cMajor.third)

# root , bass 등 코드와 관련된 레퍼런스
# https://spmusic.tistory.com/737

# 코드를 다음과 같이 만들고 해당 코드 안에 다른 음을 추가할 수도 있다.
# add 메소드를 사용한다.

dMaj = chord.Chord('D4 F#4')
dMaj.add('A5')
print(dMaj)

# 삭제도 가능하다.
dMaj.remove('D4')
print(dMaj)

# add 메소드에 피치와 note도 가능하다.
dMaj.add(pitch.Pitch('D3'))
dMaj.add(note.Note('F#5'))
print(dMaj)

# 다음과 같은 메소드로 closedpositon으로 코드를 바꿀 수도 있다.
cClosed = cMinor.closedPosition()
print(cClosed)

# inplace 옵션을 True로 두면 본래 객체에 변경된 코드가 저장된다.
cMajor.closedPosition(inPlace=True)

# semiclosedPostion도 있다.
c1 = chord.Chord(['C4', 'E5', 'C#6', 'E-7', 'G8', 'C9', 'E#9'])
c2 = c1.semiClosedPosition()
print(c2)

# common Name 속성도 있다.
elliottCarterChord = chord.Chord(['C4', 'D-4', 'E4', 'F#4'])
print(elliottCarterChord.commonName)

#   노트를 활용해 코드 만들기

d = note.Note('D4')
fSharp = note.Note('F#4')
a = note.Note('A5')
dMajor = chord.Chord([d, fSharp, a])

# dMajor.show()
# 위와 같은 방식으로 note를 활용해 코드를 만들 수 있다.

# 물론 아래와 같은 방식도 사용 가능하다.
e7 = chord.Chord("E4 G#4 B4 D5")
# e7.show()

# 또한 아래와 같은 방식으로도 표현 가능하다.
# 아래 코드의 - 는 플랫을 의미한다.

es = chord.Chord("E- G B-")
# es.show()

fMajor = chord.Chord("F A C")
# fMajor.show()

print(fMajor.inversion(), fMajor.inversionName())
print(fMajor.fullName)
print(fMajor.pitchedCommonName)

#   코드로 스트림 구성하기
stream1 = stream.Stream()
stream1.append(cMinor)
stream1.append(fMajor)
stream1.append(es)
stream1.show("text")

# 위와 같이 스트림 안에 코드를 넣는 방식으로 스트링을 구성할 수 있다.
# rest 즉 쉼표도 스트림 안에 넣어 스트림을 구성할 수 있다.
# 아래 코드를 살펴보자.

rest1 = note.Rest()
rest1.quarterLength = 0.5
noteASharp = note.Note('A#5')
noteASharp.quarterLength = 1.5

stream2 = stream.Stream()
stream2.append(cMinor)
stream2.append(rest1)
stream2.append(noteASharp)
stream2.show("text")
