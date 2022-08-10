import React, { useState, SyntheticEvent } from "react";
import style from "@/styles/Table.module.css";
import Link from "next/link";

type Props = {
  // 현재 서버가 없는 상태 //
  //onSubmit: (e: React.FormEvent<HTMLFormElement>) => void;
};

const LyUpload: React.FC<Props> = ({}: Props) => {
  return (
    <div>
      <form>
        <div className="col-md-3 text-center m-auto w-75 p-3">
          <h4 className={style.h4}>
            {" "}
            <br />
            인공지능을 사용하여 작사를 경험해보세요
          </h4>
        </div>
        <div className="col-md-3 text-center m-auto w-75 p-3">
          <Link href="/lyrics/lyrics">
            <button
              className="btn btn-outline-dark "
              type="submit"
              id="inputGroupFileAddon04"
            >
              <h5>작사하기</h5>
            </button>
          </Link>
        </div>
      </form>
    </div>
  );
};
export default LyUpload;
