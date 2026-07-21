import { useNavigate } from "react-router-dom";
import { useState } from "react";
import {
  AppBar,
  Toolbar,
  InputBase,
  IconButton,
  Badge,
  Avatar,
  Menu,
  MenuItem,
  Box,
} from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import NotificationsIcon from "@mui/icons-material/NotificationsOutlined";
import { useAuth } from "@/context/AuthContext";
import { DRAWER_WIDTH } from "./Sidebar";

export default function Topbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const [query, setQuery] = useState("");

  function handleSearchSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (query.trim()) navigate(`/search?q=${encodeURIComponent(query.trim())}`);
  }

  const initials = user ? `${user.first_name[0] ?? ""}${user.last_name[0] ?? ""}` : "";

  return (
    <AppBar
      position="fixed"
      elevation={0}
      sx={{
        width: `calc(100% - ${DRAWER_WIDTH}px)`,
        ml: `${DRAWER_WIDTH}px`,
        backgroundColor: "rgba(255,255,255,0.6)",
        backdropFilter: "blur(16px)",
        borderBottom: "1px solid rgba(255,255,255,0.4)",
        color: "text.primary",
      }}
    >
      <Toolbar sx={{ gap: 2 }}>
        <Box
          component="form"
          onSubmit={handleSearchSubmit}
          className="glass-panel"
          sx={{
            display: "flex",
            alignItems: "center",
            px: 2,
            py: 0.5,
            flexGrow: 1,
            maxWidth: 480,
          }}
        >
          <SearchIcon fontSize="small" sx={{ mr: 1, color: "text.secondary" }} />
          <InputBase
            placeholder="Search datasets, projects, annotation tasks…"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            fullWidth
            sx={{ fontSize: 14 }}
          />
        </Box>

        <Box sx={{ flexGrow: 1 }} />

        <IconButton onClick={() => navigate("/notifications")}>
          <Badge color="error" variant="dot">
            <NotificationsIcon />
          </Badge>
        </IconButton>

        <IconButton onClick={(e) => setAnchorEl(e.currentTarget)}>
          <Avatar sx={{ width: 32, height: 32, bgcolor: "#4285F4", fontSize: 14 }}>
            {initials || "U"}
          </Avatar>
        </IconButton>
        <Menu anchorEl={anchorEl} open={Boolean(anchorEl)} onClose={() => setAnchorEl(null)}>
          <MenuItem disabled>{user?.email}</MenuItem>
          <MenuItem
            onClick={() => {
              logout();
              navigate("/login");
            }}
          >
            Sign out
          </MenuItem>
        </Menu>
      </Toolbar>
    </AppBar>
  );
}
