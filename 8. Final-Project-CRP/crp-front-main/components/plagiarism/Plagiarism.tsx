import React, { useEffect, useState } from "react";

type Props = {
  onSubmit: (e: React.FormEvent<HTMLFormElement>) => void;
};
const Plagiarism: React.FC<Props> = ({ onSubmit }) => {
  const onClick = (e: any) => {
    e.preventDefault();
    setClick(1);
  };
  const [click, setClick] = useState(0);

  return (
    <div>
      <form onSubmit={onSubmit}>
        <div>
          <img
            src="https://ifh.cc/g/YB3kqq.jpg"
            style={{ width: 800 + "px" }}
            alt=" score"
          />{" "}
          &nbsp; &nbsp; &nbsp;
          <img
            src="https://ifh.cc/g/zNnyVv.jpg"
            style={{ width: 500 + "px" }}
            alt="score"
          />
        </div>
        <div className="col-md-3 text-center m-auto">
          <br />
          <br />
          <button onClick={onClick} type="button" className="btn btn-dark">
            표절판독하기
          </button>
          <br />
          <br />
          <br />
          <br />
          {click === 1 ? (
            <div className="input-group">
              <h5>검사 결과 : 표절 </h5> <br />
              <br />
              <div className="w-100 p-3">
                <h5>
                  하이라이트 된 부분의 마디가 학교종이 땡땡땡 악보와 유사합니다.
                </h5>
              </div>
            </div>
          ) : null}
        </div>
      </form>
    </div>
  );
};

export default Plagiarism;
