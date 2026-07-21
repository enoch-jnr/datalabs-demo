import { apiClient } from "./client";
import { AppNotification } from "./types";

export async function listNotifications(unreadOnly = false): Promise<AppNotification[]> {
  const { data } = await apiClient.get<AppNotification[]>("/notifications/", {
    params: { unread_only: unreadOnly },
  });
  return data;
}

export async function markNotificationRead(id: string): Promise<AppNotification> {
  const { data } = await apiClient.post<AppNotification>(`/notifications/${id}/read`);
  return data;
}
