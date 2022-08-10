import { Article } from "@/modules/types";
import React, { useState } from "react";
import Image from "next/image";
import { musicData } from "@/modules/types";
export interface Props {
  datas: Article[];
  onDeleteClick: any;
}

const AllBoardList: React.FC<Props> = ({ datas, onDeleteClick }: Props) => {
  const [text, setText] = useState([
    {
      id: 1,
      title: "CRP",
      content: "Music is my life",
    },
    {
      id: 2,
      title: "CRP Team",
      content: "Enjoy your Life!",
    },
  ]);
  return (
    <div className="container">
      <br />
      <div>
        <h1 className="text-center"># CRP 게시판 #</h1>
      </div>
      <br />
      {text.map((data: any) => (
        <div className="row mb-2" key={data.id}>
          <div className="col-12">
            <div className="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
              <div className="col p-4 d-flex flex-column position-static">
                <input type="hidden" key={data.id} />
                <strong className="d-inline-block mb-2 text-primary">
                  {/* <h5>{data?.nickname}</h5> */}
                </strong>
                <input type="hidden" name="articleId" value={data.id} />
                <h3 className="mb-0">{data?.title}</h3>
                <div className="mb-1 text-muted">
                  {/* <h5> {article?.writtenDate} </h5> */}
                </div>
                <p key={data.content} className="card-text mb-auto">
                  {data?.content}
                </p>
              </div>
              <button
                onClick={() => onDeleteClick(data.id)}
                type="button"
                className="btn btn-outline-danger btn-sm m-3 col-3"
              >
                삭제
              </button>
              <div className="col-auto d-none d-lg-block">
                {/* <Image src={article?.picture} alt="board"/> */}
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default AllBoardList;
