import { useEffect, useState } from "react";
import { Box, Typography, List, ListItemButton, ListItemText, Chip, Tabs, Tab } from "@mui/material";
import GlassCard from "@/components/common/GlassCard";
import { listNotifications, markNotificationRead } from "@/api/notifications";
import { AppNotification } from "@/api/types";

export default function NotificationsPage() {
  const [notifications, setNotifications] = useState<AppNotification[]>([]);
  const [tab, setTab] = useState<"all" | "unread">("all");

  function refresh() {
    listNotifications(tab === "unread").then(setNotifications);
  }

  useEffect(refresh, [tab]);

  async function handleClick(n: AppNotification) {
    if (!n.is_read) {
      await markNotificationRead(n.id);
      refresh();
    }
  }

  return (
    <Box>
      <Typography variant="h4" sx={{ mb: 3 }}>
        Notifications
      </Typography>

      <Tabs value={tab} onChange={(_, v) => setTab(v)} sx={{ mb: 2 }}>
        <Tab value="all" label="All" />
        <Tab value="unread" label="Unread" />
      </Tabs>

      <GlassCard sx={{ p: 0 }}>
        <List>
          {notifications.map((n) => (
            <ListItemButton key={n.id} onClick={() => handleClick(n)} sx={{ opacity: n.is_read ? 0.6 : 1 }}>
              <ListItemText primary={n.title} secondary={n.body} />
              {!n.is_read && <Chip size="small" color="primary" label="new" />}
            </ListItemButton>
          ))}
          {notifications.length === 0 && (
            <Typography color="text.secondary" sx={{ p: 3 }}>
              You&apos;re all caught up.
            </Typography>
          )}
        </List>
      </GlassCard>
    </Box>
  );
}
