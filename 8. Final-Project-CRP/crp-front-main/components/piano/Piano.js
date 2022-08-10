import './Piano.module.css';
import css from "styled-jsx/css"

import { Button } from 'react-bootstrap';
import React, {useEffect, useState} from 'react';
import axios from 'axios';

import {
  playC4,
  playDb4,
  playD4,
  playEb4,
  playE4,
  playF4,
  playGb4,
  playG4,
  playAb4,
  playA4,
  playBb4,
  playB4,
  playC5,
  playDb5,
  playD5,
  playEb5,
  playE5,
  playF5,
  playGb5,
  playG5,
  playAb5,
  playA5,
  playBb5,
  playB5,
  playC6,
  PlayNote
} from "./Tone.js"

import {HOST_3000} from "../common/Path"

const headers = {
  "Content-Type": "application/json"
}

//window.addEventListener("keydown",PlayNote);
function Piano(){

  const [saveNote, setSaveNote] = useState()

   const tonePianoApi = async(saveNote) => {
     try {
      console.log(`API 진입`)
       const response = await axios.post(`${HOST_3000}`, saveNote, {headers})
     } catch (err) {
      return err;
    }
   }
  
  useEffect(() => {
    window.addEventListener('keydown', PlayNote)
  }, [])

  const clickC4 =(e)=>{
      e.preventDefault()
      
      playC4()
      
  }

  const clickDb4 =(e)=>{
    e.preventDefault()
    
     playDb4()
    

}

    const clickD4 =(e)=>{
    e.preventDefault()
    
    playD4()
    
  }

  const clickEb4 =(e)=>{
    e.preventDefault()
    
    playEb4()
    
  }

  const clickE4 =(e)=>{
    e.preventDefault()
    
    playE4()
    
  }

  const clickF4 =(e)=>{
    e.preventDefault()
    
    playF4()
    
  }

  const clickGb4 =(e)=>{
    e.preventDefault()
    
    playGb4()
    
  }

  const clickG4 =(e)=>{
    e.preventDefault()
    
    playG4()
    
  }

  const clickAb4 =(e)=>{
    e.preventDefault()
    
    playAb4()
    
  }

  const clickA4 =(e)=>{
    e.preventDefault()
    
    playA4()
    
  }

  const clickBb4 =(e)=>{
    e.preventDefault()
    
    playBb4()
    
  }

  const clickB4 =(e)=>{
    e.preventDefault()
    
    playB4()
    
  }

  const clickC5 =(e)=>{
    e.preventDefault()
    
    playC5()
    
  }

  const clickDb5 =(e)=>{
    e.preventDefault()
    
    playDb5()
    
  }

  const clickD5 =(e)=>{
    e.preventDefault()
    
    playD5()
    
  }

  const clickEb5 =(e)=>{
    e.preventDefault()
    
    playEb5()
   
  }

  const clickE5 =(e)=>{
    e.preventDefault()
    
    playE5()
   
  }

  const clickF5 =(e)=>{
    e.preventDefault()
    
   playF5()
    
  }

  const clickGb5 =(e)=>{
    e.preventDefault()
    
    playGb5()
    
  }

  const clickG5 =(e)=>{
    e.preventDefault()
    
   playG5()
    
  }

  const clickAb5 =(e)=>{
    e.preventDefault()
    
    playAb5()
    
  }

  const clickA5 =(e)=>{
    e.preventDefault()
    
   playA5()
    
  }

  const clickBb5 =(e)=>{
    e.preventDefault()
    
    playBb5()
    
  }

  const clickB5 =(e)=>{
    e.preventDefault()
    
    playB5()
    
  }

  const clickC6 =(e)=>{
    e.preventDefault()
    
    playC6()
    
  }

  const clickStart = (e) => {
    e.preventDefault()
    localStorage.clear()
  }

  const clickEnd =(e)=>{
    e.preventDefault()
    const finalNote = localStorage.getItem('note')
    const arr = finalNote.split(',')
    const arr2 = arr.slice(1)

    tonePianoApi()
    console.log({item : arr2})
    setSaveNote({item : finalNote})
    //axios.post(`${SERVER}`, saveNote, {headers})
    
    localStorage.setItem('note', null)
  }

    return(
    <div className='pianoPage'>
    
    <div className="col-md-3 text-center m-auto">
    <h1>Enjoy Playing Piano!</h1> </div>

    <br/> <br/> <br/> <br/> 

    <div className='row'>
    <div className= "col text-center">
    <Button type = "button" className="btn btn-light" onClick={clickStart}>녹음시작</Button> <br/><br/> 
    </div>

    <div className= "col text-center">
    <Button type = "button" className="btn btn-dark" onClick={clickEnd}>녹음 끝</Button><br/><br/>
    </div>
    </div>

    <div className='piano'>
    <div className='white-key' name= 'note1' onClick={clickC4}>A</div>
    <div className='black-key' name= 'note2' onClick={clickDb4}>W</div>
    <div className='white-key' name= 'note3' onClick={clickD4}>S</div>
    <div className='black-key' name= 'note4' onClick={clickEb4}>E</div>
    <div className='white-key' name= 'note5' onClick={clickE4}>D</div>
    <div className='white-key' name= 'note6' onClick={clickF4}>F</div>
    <div className='black-key' name= 'note7' onClick={clickGb4}>T</div>
    <div className='white-key' name= 'note8' onClick={clickG4}>G</div>
    <div className='black-key' name= 'note9' onClick={clickAb4}>Y</div>
    <div className='white-key' name= 'note10' onClick={clickA4}>H</div>
    <div className='black-key' name= 'note11' onClick={clickBb4}>U</div>
    <div className='white-key' name= 'note12' onClick={clickB4}>J</div>

    <div className='white-key' name= 'note13' onClick={clickC5}>K</div>
    <div className='black-key' name= 'note14' onClick={clickDb5}>O</div>
    <div className='white-key' name= 'note15' onClick={clickD5}>L</div>
    <div className='black-key' name= 'note16' onClick={clickEb5}>P</div>
    <div className='white-key' name= 'note17' onClick={clickE5}>Z</div>
    <div className='white-key' name= 'note18' onClick={clickF5}>X</div>
    <div className='black-key' name= 'note19' onClick={clickGb5}>C</div>
    <div className='white-key' name= 'note20' onClick={clickG5}>V</div>
    <div className='black-key' name= 'note21' onClick={clickAb5}>B</div>
    <div className='white-key' name= 'note22' onClick={clickA5}>N</div>
    <div className='black-key' name= 'note23' onClick={clickBb5}>M</div>
    <div className='white-key' name= 'note24' onClick={clickB5}>R</div>
    <div className='white-key' name= 'note25' onClick={clickC6}>I</div>
    
    </div>
    <style jsx>
        {`.pianoPage{
    align-items: center;
    background-color: bisque;
  }
  
  /* h1{
    text-align: center;
  } */
  
  .piano {
    display: flex;
    justify-content: center;
    
  }
  
  .white-key {
    border: 1px solid #000000;
    width: 100px;
    height: 400px;
    background-color: white;
    color: red;
    text-align: center;
  }
  
  .black-key {
    background-color: black;
    width: 60px;
    height: 250px;
    margin-left: -30px;
    margin-right: -30px;
    z-index: 1;
    color: red;
    text-align: center;
  
  }
  
  `}
    </style>
    </div>
    

    )
}

export default Piano;