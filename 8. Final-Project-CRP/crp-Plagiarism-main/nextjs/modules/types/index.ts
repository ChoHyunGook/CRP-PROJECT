export interface Article {
  nickname?: string;
  articleId?: number;
  title?: string;
  content?: string;
  picture?: FileList | string | any;
  writtenDate?: string;
  open?: string;
  comment?: string;
  qna?: string;
  pictureName?: string;
  size?: number;
  writeData? : string;
  id? : number;
}
export interface User {
  userId?: number;
  password?: string;
}
export interface ArticleState {
  data: Article;
  status: "successed" | "loading" | "failed";
  error: null;
}
export interface UserState {
  data: User;
  status: "successed" | "loading" | "failed";
  error: null;
}

export interface UploadFileResponse {
  success: boolean;
  message: string;
}
export interface ValidatorResponse {
  isValid: boolean;
  errorMessage: string;
}

export interface musicData {
  data? : musicData[]
  userId : number;
  title : string;
  content : string;
}

export const fileTypes = ["jpg", "png"];
