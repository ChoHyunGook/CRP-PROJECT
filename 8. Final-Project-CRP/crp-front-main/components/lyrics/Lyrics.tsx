import React, { useState } from "react";

type Props = {
  onSubmit: (e: React.FormEvent<HTMLFormElement>) => void;
  onChange: (e: React.FormEvent<HTMLInputElement> | any) => void;
};
const Lyrics: React.FC<Props> = ({ onChange, onSubmit }) => {
  const onClick = (e: any) => {
    e.preventDefault();
    setClick(1);
  };

  const [click, setClick] = useState(0);
  return (
    <div className="col-md-3 text-center m-auto">
      <form onSubmit={onSubmit}>
        <br />
        <br />

        <div className="container">
          <h2>작사 키워드</h2>
          <br />
          <br />
          <select className="form-control">
            <option>가요</option>
            <option>동요</option>
          </select>{" "}
          <br />
          <br />
          <button
            onClick={onClick}
            type="button"
            className="btn btn-outline-dark"
          >
            작사하기
          </button>
          <br />
          <br />
          <br />
          {click === 1 ? (
            <div className="input-group">
              <h5>동요 노래 가사 :</h5>
              <br />
              <br />
              <h5>
                1.파란 하늘 파란 하늘 꿈이 드리운 푸른 언덕에 아기 염소 여럿이
                풀을 뜯고 놀아요 해처럼 밝은 얼굴로
              </h5>
              <br />
              <h5>2.학교 종이 땡땡땡 어서모이자 선생님이 우리를 기다리신다</h5>
              <br />
              <h5>
                3.산토끼 토끼야 어디를 가느냐 깡총깡총 뛰면서 어디를 가느냐
              </h5>
              <br />
              <h5>4.새신을 신고 뛰어보자 팔짝 머리가 하늘까지 닿겠네</h5>
              <br />
              <h5>
                5.곰 세 마리가 한 집에 있어 아빠곰 엄마곰 애기곰 아빠곰은 뚱뚱해
                엄마곰은 날씬해 애기곰은 너무 귀여워 으쓱으쓱 잘한다
              </h5>
              <br />
              <h5>6.얘들아 얘들아 이리와 나와 체조를 하자</h5>
              <br />
              <h5>7.원숭이 엉덩이는 빨개 사과처럼 빨가면 사과 사과는 맛있어</h5>
              <br />
              <h5>
                8.빨간풍선 파란풍선 노란풍선 속닥속닥 파란풍선은 어디에 떴을까
              </h5>
              <br />
              <h5>9.엄마손 아빠손 서로 잡고 빙글빙글 돌자</h5>
              <br />
              <h5>
                10.우리 모두 다같이 손뼉을 치면서 랄랄랄 라랄 라랄 라랄 랄랄랄
                라랄 라랄 라랄라
              </h5>
              <br />
              <h5>11.둥글둥글 둥게둥게 빙글빙글 돌아라 빙글빙글 돌아라</h5>
              <br />
              <h5>12.나비야나비야 잠자리야 잠자리야 날개가 돋치면 날자</h5>
              <br />
              <h5>
                13.산토끼 토끼야 어디를 가느냐 깡총깡총 뛰면서 어디를 가느냐
              </h5>
              <br />
              <h5>14.기린아 기린아 목이 길어 기린아 기린아 노래 불러보자</h5>
              <br />
              <h5>15.달을 보고 친구를 생각해 밤을 세워보자</h5>
              <br />
              <h5>16.달밤에 홀로 날으는 새처럼 훨~훨 날으는 새처럼</h5>
            </div>
          ) : null}
        </div>
      </form>
    </div>
  );
};

export default Lyrics;
