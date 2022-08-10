import React, {useState} from 'react';
import Plagiarism from '@/components/plagiarism/Plagiarism';
import { NextPage } from 'next';

const PlagiarismPage: NextPage = () =>{

    
    const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        
    }


    return <Plagiarism  onSubmit={onSubmit}/>
}
export default PlagiarismPage;