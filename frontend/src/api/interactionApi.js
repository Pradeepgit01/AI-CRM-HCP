import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/interactions";

export const logInteractionApi = async (payload) => {
  const response = await axios.post(`${API_URL}/log`, payload);
  return response.data;
};
