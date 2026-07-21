import { apiClient } from "./client";
import { Dataset } from "./types";

export async function listDatasets(projectId: string): Promise<Dataset[]> {
  const { data } = await apiClient.get<Dataset[]>("/datasets/", {
    params: { project_id: projectId },
  });
  return data;
}

export async function createDataset(payload: {
  project_id: string;
  name: string;
  code: string;
  description?: string;
}): Promise<Dataset> {
  const { data } = await apiClient.post<Dataset>("/datasets/", payload);
  return data;
}
