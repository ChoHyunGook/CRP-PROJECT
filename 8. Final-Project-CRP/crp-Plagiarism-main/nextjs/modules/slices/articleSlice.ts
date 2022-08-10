import { Article, ArticleState } from "@/modules/types";
import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { ArticleService } from "../services/ArticleService";

const articleService = new ArticleService();
const ArticleSlice = createSlice(articleService.createArticleSlice());

export const {
  writeArticle,
  writeArticleSuccess,
  writeArticleFailure,
  fetchArticles,
  fetchArticleSuccess,
  removeArticle,
  fetchMyArticle,
  writeComment,
} = ArticleSlice.actions;
const { reducer, actions } = ArticleSlice;
export const ArticleActions = actions;
export default reducer;
