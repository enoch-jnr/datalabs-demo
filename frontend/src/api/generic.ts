import { apiClient } from "./client";

/**
 * Thin client for the scaffolded modules (enterprises, teams,
 * experiments, model registry, training, deployments, pipelines,
 * inference, registry, monitoring, plugins, analytics, audit,
 * storage, billing, marketplace) — all backed by the backend's
 * GenericCRUDRouter, so one client function covers all of them.
 */
export async function listGeneric<T>(path: string): Promise<T[]> {
  const { data } = await apiClient.get<T[]>(path);
  return data;
}

export async function createGeneric<T>(path: string, payload: Record<string, unknown>): Promise<T> {
  const { data } = await apiClient.post<T>(path, payload);
  return data;
}

export async function deleteGeneric(path: string, id: string): Promise<void> {
  await apiClient.delete(`${path}${id}`);
}
