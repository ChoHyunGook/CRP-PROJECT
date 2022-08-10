import style from "@/styles/BoardList.module.css";
import axios from "axios";
import { useEffect, useState } from "react";

const Table =({columns,colspan,data})=>{
    return(
        <table className={style.table}>
        <thead>
        <tr className={style.tr}>
        {columns.map((column)=>(
            <th key ={column} className={style.td}>{column}</th>
        ))}
        </tr>
        </thead>
        <tbody>
        { data.length == 0 ?<tr className={style.tr}>
                            <td colSpan={colspan} className={style.td}>데이터가없습니다</td>
                            </tr>
        :data.map((board)=>(
            <tr className={style.tr} key ={board.passengerId}>
            <td className={style.td}>{board.passengerId}</td>
            <td className={style.td}>{board.name}</td>
            <td className={style.td}>{board.teamId}</td>
            <td className={style.td}>{board.subject}</td>
            </tr>
        ))}
        
        </tbody>
        </table>
    )
}

export default function List(){
    const columns =["passengerId","name","teamId","subject"]
    const [data,setData]=useState([])
    useEffect(()=>{
        axios.get('http://localhost:5000/api/article/getArticles').then(res=>{
            setData(res.data.articles)
        }).catch(err=>{})
    },[])
    return (<>
        <h1>게시판 목록</h1><br/><br/>
        <div className={style.td}>
        <Table columns={columns} colspan={4} data = {data}/>
        </div><br/><br/>
    <button onClick={ () => {history.back('/'); } } >뒤로가기</button>
    </>)
}