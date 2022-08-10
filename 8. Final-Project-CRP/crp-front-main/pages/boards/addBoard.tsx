import React, { useEffect, useState } from 'react'
import AddBoard from '@/components/boards/AddBoard'
import { useAppDispatch } from '@/hooks'
import { NextPage } from 'next'
import { writeArticle } from '@/modules/slices/articleSlice'

import { Article } from '@/modules/types'

const AddBoardPage: NextPage = () =>  {
  const date = new Date();
  const writtenDate = date.toDateString()
  const [write, setWrite] = useState<Article>({ title:'', content: '', open: "",
  picture: '', writtenDate: '', pictureName: ''
})
  const dispatch = useAppDispatch()
  


  const onChange = (e: React.FormEvent<HTMLInputElement>) => {
    e.preventDefault()
    const {name, value} = e.currentTarget
    setWrite({...write, [name]: value})
  }

  const onSubmit = (e:React.FormEvent<HTMLFormElement>) => {
    e.preventDefault() 
    dispatch(writeArticle(write))
  }

  return (
    <AddBoard onChange={onChange} onSubmit = {onSubmit}/>
  )
}
export default AddBoardPage