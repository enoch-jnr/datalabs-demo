import { apiClient } from "./client";
import { Workspace } from "./types";

export async function listWorkspaces(): Promise<Workspace[]> {
  const { data } = await apiClient.get<Workspace[]>("/workspaces/");
  return data;
}

export async function createWorkspace(payload: {
  name: string;
  slug: string;
  description?: string;
}): Promise<Workspace> {
  const { data } = await apiClient.post<Workspace>("/workspaces/", payload);
  return data;
}
