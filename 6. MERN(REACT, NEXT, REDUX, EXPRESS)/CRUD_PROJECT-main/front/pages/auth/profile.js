import React, {useState} from 'react';
import {Profile} from '@/components';
import {useSelector} from 'react-redux'; 

const ProfilePage = () => {
    const {loginUser} = useSelector(state => state.login)
    return (<Profile loginUser={loginUser}/>);
};

export default ProfilePage