import { apiClient } from "./client";
import { Project } from "./types";

export async function listProjects(workspaceId: string): Promise<Project[]> {
  const { data } = await apiClient.get<Project[]>("/projects/", {
    params: { workspace_id: workspaceId },
  });
  return data;
}

export async function createProject(payload: {
  workspace_id: string;
  name: string;
  code: string;
  description?: string;
}): Promise<Project> {
  const { data } = await apiClient.post<Project>("/projects/", payload);
  return data;
}
