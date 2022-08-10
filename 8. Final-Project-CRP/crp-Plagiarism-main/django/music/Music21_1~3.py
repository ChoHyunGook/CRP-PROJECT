import music21

# Music21 User Guide 1 ~ 3 레퍼런스 정리

#   midi 파일 불러오는 법
# music21.converter.parse(datapath) 로 music21 객체 생성

datapath = './midi/Canon.mid'
midi = music21.converter.parse(datapath)

#   midi 파일의 키 알아내기

print(midi.analyze('key'))
# Canon의 경우 D 메이저

#   note (음표) 객체 만들기

f = music21.note.Note("F5")
# F5 즉 5옥타브의 파 음을 만들었다. 따라서 f.name은 F(파)를 octave는 5옥타브를 보여준다.
print(f)
print(f.name)
print(f.octave)

print(f.pitch)
# pitch의 경우 해당음의 피치를 나타낸다. (위의 경우 합쳐져서 F5 )

# f.pitch.pitchClassString은 옥타브를 int가 아닌 string으로 반환한다.
# 따라서 f.octave == 5 는 True 지만 , f.pitch.pitchClassString == 5 는 False다.

# 플랫과 샾의 경우 다음과 같이 만들 수 있다. (플랫 - / 샾 # )
b = music21.note.Note("F#2")
print(b.name)

# accidental은 해당 pitch의 올림 , 내림 즉 샤프 , 플랫을 리턴한다.
print(b.pitch.accidental)
k = b.pitch.accidental

# accidnetal 객체의 alter을 통해서 int 형태로 올림과 내림을 구분할 수 있는 듯 하다.
print(k.alter)

#   음 높낮이 변경
# M숫자 (마이너스 숫자 ) 와 P숫자 (플러스 숫자 ) 로 음을 높이고 내리고 할 수 있다.
# inplace 옵션을 = True로 하면 해당 객체에 바로 적용된다.
d = b.transpose("M3")
print(d)

d = music21.note.Note("D")

b.transpose("P4", inPlace=True)  # 바로 바뀜
d.transpose("dd6", inPlace=True)

# 레퍼런스에서 D음을 dd6(?)으로 내려서 alter가 -3.0 이고 triple flat인 음표를 만든다.
# 검색해보니 트리플 플랫이 존재하는 건 알겠는데 dd6은 무슨 뜻인지 잘 모르겠다.
print(d.pitch.accidental.alter)
print(d.pitch.accidental.name)

#   피치 (음높이) 생성
p1 = music21.pitch.Pitch('b-4')
print(p1)  # B-4 음높이 생성

# 피치와 관련된 메소드들
print(p1.octave)  # 피치의 옥타브 위의 경우 4
print(p1.pitchClass)  # 피치의 class
print(p1.name)  # 피치 이름 위의 경우 b
print(p1.accidental.alter)  # 피치의 플랫이나 샤프 위의 경우 플랫 (-) 이므로 -1.0
print(p1.nameWithOctave)  # 피치의 이름과 옥타브 모두 함께
print(p1.midi)  # midi는 C4를 60으로 기준잡아 그 음이 하나 올라갈때마다 1씩 즉 피아노음은 0 ~ 127 사이일 것이다.
# 위의 경우 midi는 70 / C4 = 60 에서 10만큼 위에 있으므로

# 이처럼 해당 특성들은 모두 변경가능하다.
p1.name = 'd#'
p1.octave = 3
print(p1.nameWithOctave)

# 음표에서 살펴보았던 transpose도 역시 가능 M과 P로 마이너스 플러스 높낮이
p2 = p1.transpose('M7')
print(p2)

#   Note와 Pitch의 관계

# 다음과 같이 C샾 음을 만들었다고 하자.
csharp = music21.note.Note('C#4')
print(csharp.name)

print(csharp.pitch.name)
print(csharp.octave)
print(csharp.pitch.octave)

# 음표안에 pitch가 있고 그 pitch의 이름을 볼 수 있다.
# 그 피치의 옥타브를 보던 , 그 음의 옥타브를 보던 같은 것을 위의 코드를 통해 알 수 있다.
# 그렇다면 왜 pitch가 필요한가 하면 pitch는 note에서 불가능한 다른 메소드들이 있다.

# 예를 들어 피치를 스페인어로 보여주는 csharp.pitch.spanish는 가능하지만
# csharp.spanish 는 가능하지 않다. spanish 메소드는 pitch에 있기 떄문이다.

# 또한 피치의 Unicode도 볼 수 있다.
print(csharp.pitch.unicodeName)

# 관련된 다른 메소드들 - (어떤 매소드인지는 모르겠음 )
print(csharp.pitch.getEnharmonic())
print(csharp.pitch.getLowerEnharmonic())

#   지속시간 Duration

# 음악에는 지속시간 즉 Duration 개념이 쓰인다.
# 예를 들어 음을 얼마나 지속할 것인지 등등이다.
# 그래서 Duration 객체는 보통 다른 객체들에 붙어서 사용된다.

# 다음은 half Duration을 만드는 과정이다.
# Duration 안에는  “whole”, “half”, “quarter”, “eighth”, “16th”, “32nd”, “64th”이 들어간다.
# 아마 음표의 길이인 온음표 / 2분음표 / 4분음표 / 8분음표 / 16분음표 / 32분음표 / 64분음표 로 이해하면 될 듯 싶다.
# Duration이 음표의 길이를 의미하는 것이 아닌 음표에 사용된 예시라고 생각하면 된다.
# 쉼표에 사용되면 그 쉼표의 길이가 될 것이다.

# 잘 사용되진 않지만 music21에는 “breve” (2 whole notes), “longa” (4 whole notes),
# and “maxima” (8 whole notes) and on the other side, “128th”, “256th”, etc. down to “2048th” notes 도 있다.
# 아마 온음표를 여러개 붙인 온음표 이상의 길이와 64분음표를 더 잘게 쪼갠 128 , 256 ... 도 있는 듯 하다.
halfDuration = music21.duration.Duration('half')

# string이 아닌 숫자로도 Duration을 만들 수 있다.
# 1.5는 1.5 쿼터 노트로 1.5 * 4분음표를 의미한다. 즉 4분음표 + 8분음표의 길이만큼을 만든다고 생각할 수 있다.
dottedQuarter = music21.duration.Duration(1.5)
print(dottedQuarter.quarterLength)

# 그래서 half의 경우도 확인해보면 2가 나온다. 왜냐면 4분음표 2개가 2분음표기 떄문이다.
print(halfDuration.quarterLength)

# 스트링으로 타입도 확인 가능하다.
print(halfDuration.type)  # half
print(dottedQuarter.type)  # quarter

# 타입은 Duration의 모든것을 알려주지 않는다.
# dot이라는 속성을 통해서 볼 수 있는 부분이 또 있다.
# dots, type, and quarterLength 속성이 있다.

# dots은 해당음표의 점의 개수를 알려준다.
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=musicing_hj&logNo=220738473324
# 음표에 대한 기본지식 레퍼런스
dottedQuarter.dots = 3
print(dottedQuarter.quarterLength)

# 예를 들어 1.5면 1 + 0.5로 구성되어 있다. 따라서 점이 하나 붙으면 1 + 0.5 + 0.25 가 된다.
# 점이 하나씩 붙는 다는 것은 1/2 하면서 더해준다고 생각하면 된다.


# quarterLength 속성으로는 Duration의 길이를 정할 수 있다.
# 0.25면 1이 4분음표니까 1/4 되어 16분 음표일 것이다.
dottedQuarter.quarterLength = 0.25
print(dottedQuarter.type)

#   Note와 Duration

# 앞에서 Duration은 Note와 함께 쓰일 수 있다고 했다.
# 그렇기에 Note안에는 Duration 속성이 있다.
# 악보를 천천히 생각해보면 음표의 나열로 이루어졌다고 생각할 수 있다.
# 그렇다면 그 음표 하나하나는 어떻게 이루어졌나? 생각해보면 높낮이 (pitch)와 음을 누르는 지속시간(음의길이 duration)으로 이루어져있다.
# 즉 note = ( pitch + duration ) 인 것이다.

# 디폴트 C4 노트인 n1을 만들었다.
n1 = music21.note.Note()
print(n1.pitch)

# 아래 코드를 통해서 볼 수 있듯이 디폴트 duration 속성값은 1.0 이다.
print(n1.duration)

# 우리는 다음과 같이 해당 음표의 pitch와 음표길이를 바꿀 수 있다.
n1.pitch.nameWithOctave = 'E-5'
n1.duration.quarterLength = 3.0

print(n1.duration.type)
print(n1.duration.dots)  # = 1 인데 왜그렇냐면 3.0 은 2.0 + 1.0 이라 2분음표에 점 하나 붙은걸로 표현되기 때문
print(n1.pitch.name)
print(n1.pitch.accidental)
print(n1.octave)

# 앞서 살펴본 다양한 pitch , duration에 관한 메소드들도 다음과 같이 다 사용이 가능하다.

# note 역시 pitch와 duration들이 하는 것들을 모두 할 수 있다.
print(n1.name)
print(n1.quarterLength)

# 음표에는 lyric 즉 자막 속성도 있다.
otherNote = music21.note.Note("F6")
otherNote.lyric = "I'm the Queen of the Night!"

# 다음과 같이 자막을 더할 수도 있다.
n1.addLyric(n1.nameWithOctave)
n1.addLyric(n1.pitch.pitchClassString)
n1.addLyric(f'QL: {n1.quarterLength}')

# show로 해당 음표를 보거나 실행하는 것도 가능하다.
# midi 옵션의 경우 실제 음을 midi 파일로 내준다.
# 디폴트는 .xml 기본프로그램이 실행되는데 musescore3를 설치한후 .xml 기본프로그램으로 설정해놓으면 악보상에도 해당음을 볼 수 있다.
music21.note.Note("C4").show("midi")
