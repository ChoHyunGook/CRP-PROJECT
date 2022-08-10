import { all, fork } from 'redux-saga/effects';

import {
  watchWriteArticle,
  watchFetchMyArticleSaga,
  
  watchWriteComment,
  watchRemoveArticle
} from './articleSaga'


// rootSaga를 만들어줘서 store에 추가해주 어야 합니다.
export default function* rootSaga() {
  yield all([
    fork(watchWriteArticle),
    fork(watchFetchMyArticleSaga),
    
    fork(watchRemoveArticle),
    fork(watchWriteComment)
  ]);
}