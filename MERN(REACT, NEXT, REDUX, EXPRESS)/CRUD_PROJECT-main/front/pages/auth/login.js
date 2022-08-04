import React, {useState} from 'react';
import {connect, useDispatch} from 'react-redux';
import {loginRequest} from '@/modules/auth/login';
import {Login} from '@/components';
import {useRouter} from "next/router"
import { round } from 'lodash';
import { useSelector } from 'react-redux';
import {Profile} from '@/components'
const LoginPage = ({}) => {
    const [user, setUser] = useState({userid: '', password: ''})
    const dispatch = useDispatch()
    const router = useRouter()
    const onChange = e => {
        e.preventDefault()
        const {name, value} = e.target;
        setUser({
            ...user,
            [name]: value
        })
    }
    const {isLoggined, loginUser} = useSelector(state => state.login)
    const onSubmit = e => {
        e.preventDefault()
        console.log(`로그인 정보 ${JSON.stringify(user)}`)
        console.log(history)
        dispatch(loginRequest(user))
        console.log(' 모듈에 저장된 로그인값: '+JSON.stringify(loginUser))
        //router.push('/user/profile') 이동시 데이터소실
    }
    return (isLoggined ? // 조건부 렌더링
      <Profile loginUser={loginUser}/> // frame
    :<Login onChange={onChange} onSubmit={onSubmit}/>);
};
const mapStateToProps = state => ({loginUser: state.login.loginUser})
const loginActions = {loginRequest}
export default connect(mapStateToProps, loginActions)(LoginPage);