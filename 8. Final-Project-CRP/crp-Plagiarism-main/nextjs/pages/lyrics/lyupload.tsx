import React, { useEffect, useState } from "react";
import Lyupload from "@/components/lyrics/Lyupload";
import { NextPage } from "next";
import axios from "axios";
import { HOST_3000, HOST_8000 } from "@/components/common/Path";

const headers = {
  "Content-Type": "multipart/form-data",
  Accept: "application/json",
  //Authorization: "JWT fefege...",
};

          // 현재 서버가 없는 상태 //

// const onSubmitFile = async (e: React.FormEvent<HTMLFormElement>) => {
//   e.preventDefault();
//   window.location.href = "/lyrics/lyrics";
  
// };

const LyUploadPage: NextPage = () => {
  return <Lyupload  />;
};
export default LyUploadPage;
