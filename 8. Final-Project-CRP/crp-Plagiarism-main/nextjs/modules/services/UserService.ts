import { Article, ArticleState, User, UserState } from "@/modules/types";
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

export class UserService {
  public createUserSlice() {
    const initialState: UserState = {
      data: {
        userId: 0,
        password: "",
      },
      status: "loading",
      error: null,
    };
    return {
      name: "userSlice",
      initialState,
      reducers: {
        join: (state: any, action: PayloadAction<User>) => {
          alert(`회원가입 액션 요청`);
          console.log(action);
          state.data = action.payload;
          state.status = "loading";
          console.log(`회원가입 성공 - 리듀서 ${JSON.stringify(state.data)}`);
        },
        joinSuccess: (state: any, action: PayloadAction) => {
          state.status = "successed";
        },
        joinFailure: (state: any, action: PayloadAction) => {
          alert(`회원가입 실패`);
          state.status = "failed";
        },
      },
    };
  }
}
