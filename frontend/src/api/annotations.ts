import { apiClient } from "./client";
import { AnnotationTask } from "./types";

export async function listAnnotationTasks(projectId: string): Promise<AnnotationTask[]> {
  const { data } = await apiClient.get<AnnotationTask[]>("/annotations/tasks", {
    params: { project_id: projectId },
  });
  return data;
}

export async function createAnnotationTask(payload: {
  project_id: string;
  dataset_id?: string;
  name: string;
  annotation_type: string;
  instructions?: string;
}): Promise<AnnotationTask> {
  const { data } = await apiClient.post<AnnotationTask>("/annotations/tasks", payload);
  return data;
}
