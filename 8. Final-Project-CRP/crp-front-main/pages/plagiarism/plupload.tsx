import React, { useEffect, useState } from 'react'
import Plupload from '@/components/plagiarism/Plupload'
import { NextPage } from 'next'
import axios from 'axios'
import {HOST_3000,HOST_8000} from "@/components/common/Path"

const headers = {
  "Content-Type": "multipart/form-data",
  Accept: "application/json",
  //Authorization: "JWT fefege...",
};

            // 현재 서버가 없는 상태 //


// const onSubmitFile = async (e: React.FormEvent<HTMLFormElement>) => {
//   e.preventDefault();
//   window.location.href = "/plagiarism/plagiarism";

// };




const PlUploadPage: NextPage = () => {
  
  

  
 
  

  return (
    <Plupload />
  )
}
export default PlUploadPage