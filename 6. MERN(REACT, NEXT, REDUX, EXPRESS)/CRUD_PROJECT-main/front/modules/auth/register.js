import {createAction, handleActions} from 'redux-actions';
import {call, delay, put, takeLatest, select, throttle} from 'redux-saga/effects';
import {HYDRATE} from "next-redux-wrapper"
import axios from 'axios'

const SERVER = 'http://127.0.0.1:5000'
const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT fefege..."
}

export const initialState = {
    isRegistered: false // 리액트 // 전역으로 사용하는 상태값
}

// type
const REGISTER_REQUEST = 'auth/REGISTER_REQUEST'; // 사용자 요청 -> export
const REGISTER_SUCCESS = 'auth/REGISTER_SUCCESS';
const REGISTER_FAILURE = 'auth/REGISTER_FAILURE';
const UNREGISTER_REQUEST = 'auth/UNREGISTER_REQUEST';
const UNREGISTER_SUCCESS = 'auth/UNREGISTER_SUCCESS';
const UNREGISTER_FAILURE = 'auth/UNREGISTER_FAILURE';

export const registerRequest = createAction(REGISTER_REQUEST, data => data) // 액션 -> type : REGISTER_REQUEST, payload : data
export const unregisterRequest = createAction(UNREGISTER_REQUEST, data => data)

export function* registerSaga() { // rootSaga로 넘어감
    yield takeLatest(REGISTER_REQUEST, signup);
    yield takeLatest(UNREGISTER_REQUEST, membershipWithdrawal);
}

function* signup(action) {
    try {
        console.log("*** 여기가 핵심 *** " + JSON.stringify(action))
        const response = yield call(registerAPI, action.payload) // 함수의 동기적 호출
        console.log("회원가입 서버 다녀옴 " + JSON.stringify(response.data))
        yield put({type: REGISTER_SUCCESS, payload: response.data}) // 액션 함수(dispatch)로 진행
        yield put(window.location.href="/auth/login") // 리덕스 자극 -> 리액트에게 전달
    } catch (error) {
        yield put({type: REGISTER_FAILURE, payload: error.message})
    }
}

const registerAPI = payload => axios.post(
    `${SERVER}/user/join`,
    payload,
    {headers}
)

function* membershipWithdrawal(){
    try {
        console.log("*** 회원탈퇴 ***")
    } catch (error) {
        
    }
}

const register = handleActions({ // pages의 registerActions
    [HYDRATE] : (state, action) => ({ // 동적 키 할당
        ...state, ...action.payload
    })
}, initialState)

/** handleActions 사용하기 전 학습용 백업
const auth = (state = initialState, action) => { // 리듀서
    switch (action.type) {
        case HYDRATE:
            console.log(' ### HYDRATE Issue 발생 ### ')
            return {
                ...state,
                ...action.payload
            }
        case REGISTER_SUCCESS:
            console.log(' ### 회원가입 성공 ### ' + action.payload)
            return {
                ...state,
                user: action.payload
            }
        case REGISTER_FAILURE:
            console.log(' ### 회원가입 실패 ### ' + action.payload)
            return {
                ...state,
                user: action.payload
            }
        default:
            return state;
    }
}
*/

export default register