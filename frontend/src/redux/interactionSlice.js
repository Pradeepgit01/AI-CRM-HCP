import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { logInteractionApi } from "../api/interactionApi";

export const logInteraction = createAsyncThunk(
  "interaction/log",
  async (payload) => {
    return await logInteractionApi(payload);
  }
);

const interactionSlice = createSlice({
  name: "interaction",
  initialState: {
    result: null,
    loading: false,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(logInteraction.pending, (state) => {
        state.loading = true;
      })
      .addCase(logInteraction.fulfilled, (state, action) => {
        state.loading = false;
        state.result = action.payload.data;
      });
  },
});

export default interactionSlice.reducer;
