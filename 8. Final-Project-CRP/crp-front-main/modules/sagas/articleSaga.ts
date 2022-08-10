import { ArticleController } from "@/modules/controllers/ArticleController";
import { call, put, takeEvery, takeLatest } from "redux-saga/effects";
import { ArticleActions } from "../slices/articleSlice";
import { Article } from "../types";

//get Saga
function* writeArticleSaga(action: { payload: Article }) {
  const { writeArticleSuccess, writeArticleFailure } = ArticleActions;
  const param = action.payload;
  const articleController = new ArticleController();
  try {
    yield call(articleController.writeArticle, param);
    yield put(writeArticleSuccess());
  } catch (error) {
    yield put(writeArticleFailure());
  }
}

function* fetchMyArticleSaga(action: { payload: any }) {
  const { fetchMyArticleSuccess, fetchMyArticleFailure } = ArticleActions;
  try {
    const response: Article = yield call(action.payload);
    yield put(fetchMyArticleSuccess(response));
  } catch (error) {
    yield put(fetchMyArticleFailure());
  }
}

function* removeArticleSaga(action: { payload: Article }) {
  const articleController = new ArticleController();
  try {
    yield call(articleController.removeArticle, action.payload.id);
  } catch (error) {}
}

function* wrtieCommentSaga(action: { payload: Article }) {
  const articleController = new ArticleController();
  try {
    yield call(articleController.writeComment, action.payload);
  } catch (error) {}
}
// main saga
export function* watchWriteArticle() {
  yield takeLatest(ArticleActions.writeArticle, writeArticleSaga);
}

export function* watchFetchMyArticleSaga() {
  yield takeEvery(ArticleActions.fetchMyArticle, fetchMyArticleSaga);
}
export function* watchRemoveArticle() {
  yield takeLatest(ArticleActions.removeArticle, removeArticleSaga);
}
export function* watchWriteComment() {
  yield takeLatest(ArticleActions.writeComment, wrtieCommentSaga);
}
