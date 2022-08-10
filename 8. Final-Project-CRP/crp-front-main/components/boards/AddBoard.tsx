import { Article } from '@/modules/types'
import React from 'react'

type Props = {
  
  onChange : (e: React.FormEvent<HTMLInputElement> | any ) => void
  onSubmit : (e: React.FormEvent<HTMLFormElement> ) => void
}

const AddBoard: React.FC<Props> = ({onChange, onSubmit}) => {
  const date = new Date();
  const parseDate = date.toDateString()

  return (
    <div>
    <div className='container'>
      <div className="col-md-3 text-center m-auto"><br/><br/>
        <h3>나만의 게시글</h3> <br/>
    </div>

      <div className="col-md-3 text-center m-auto">
          <h6>이미지도 업로드하고 게시글도 작성해보세요</h6><br/>
      </div>
      
      <div>
        <h2> 게시글 등록하기</h2><br/>
        <p>{parseDate}</p><br/>
      </div>
        </div>
        
    <form onSubmit={onSubmit}>
        <div className='container'>
        <div className="input-group mb-3">
          <span className="input-group-text" id="inputGroup-sizing-default">
            <h5>제목 입력</h5>
            </span>
          <input onChange={onChange} type="hidden" name='userId'/>
          <input onChange = {onChange} name = "title" type="text" className="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"/>
        </div><br/>
          <div className="input-group mb-3">
            <h3>
              <input onChange = {onChange} name = "picture" type="file" className="form-control" id="inputGroupFile02" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"/>
            </h3>
            
          </div>
          <br/>
          
          
          <div className="input-group">
              <span className="input-group-text">
              <h5>
                게시글 작성란
              </h5>
              </span>
              <textarea name = "content" onChange = {onChange} className="form-control p-5" aria-label="With textarea"></textarea>
            </div>
            <br/>  
            <button  className="w-100 btn btn-lg btn-outline-secondary " type="submit">
              UPLOAD
            </button>          
          </div>
          </form>
          </div>
    
  )
}

export default AddBoard