import { User, UserState } from "@/modules/types";
import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { UserService } from "../services/UserService";

const userService = new UserService();
const UserSlice = createSlice(userService.createUserSlice());

export const {
  join,
  joinSuccess,
  joinFailure,
  
} = UserSlice.actions;
const { reducer, actions } = UserSlice;
export const UserActions = actions;
export default reducer;
