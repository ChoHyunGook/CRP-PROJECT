import React, {useEffect, useState } from 'react'
import AllBoardList from '@/components/boards/AllBoardList'
import { NextPage } from 'next'

import { Article, musicData } from '@/modules/types'
import { ArticleController } from '@/modules/controllers/ArticleController'
import { useAppDispatch } from '@/hooks'
import { removeArticle } from '@/modules/slices/articleSlice'

const headers = {
  "Content-Type" : "application/json",
  Authorization: "JWT fefege...",

}

const AllBoardListPage: NextPage = () => {
  


  const [ data, setData ] = useState<Array<Article>>([])
  
  const dispatch = useAppDispatch()

  useEffect (() => {
    const articleController = new ArticleController();
    articleController.readList().then(response => {
      setData(response)
    })
} ,[])

  const onDeleteClick = (articleNo : any) => {
    dispatch(removeArticle({id: articleNo}))
    window.location.href = ('/boards/allBoardList')

  }

  
  return (
    <AllBoardList onDeleteClick={onDeleteClick} datas = {data} />
  )
}

export default AllBoardListPage