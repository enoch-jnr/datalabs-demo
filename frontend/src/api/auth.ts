import { apiClient } from "./client";
import { User } from "./types";

export interface TokenPair {
  access_token: string;
  refresh_token: string;
  token_type: string;
}

export async function registerUser(payload: {
  email: string;
  password: string;
  first_name: string;
  last_name: string;
  username?: string;
}): Promise<User> {
  const { data } = await apiClient.post<User>("/auth/register", payload);
  return data;
}

export async function loginUser(email: string, password: string): Promise<TokenPair> {
  const { data } = await apiClient.post<TokenPair>("/auth/login", { email, password });
  return data;
}

export async function fetchMe(): Promise<User> {
  const { data } = await apiClient.get<User>("/auth/me");
  return data;
}
