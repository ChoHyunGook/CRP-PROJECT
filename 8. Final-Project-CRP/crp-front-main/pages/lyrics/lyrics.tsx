import React, {useState} from 'react';
import { NextPage } from 'next';
import Lyrics from '@/components/lyrics/Lyrics';

const LyricsPage: NextPage = () =>{
    const onChange =(e: React.FormEvent<HTMLInputElement> ) => {
        e.preventDefault()
         
    }
    const onSubmit = (e: React.FormEvent<HTMLFormElement> ) => {
        e.preventDefault() 

    }

    return <Lyrics onChange={onChange} onSubmit={onSubmit}/>
}
export default LyricsPage;