import { NavLink } from "react-router-dom";
import {
  Drawer,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Toolbar,
  Box,
  Typography,
  Divider,
} from "@mui/material";
import DashboardIcon from "@mui/icons-material/DashboardOutlined";
import FolderIcon from "@mui/icons-material/FolderOutlined";
import DatasetIcon from "@mui/icons-material/StorageOutlined";
import LabelIcon from "@mui/icons-material/LabelOutlined";
import BusinessIcon from "@mui/icons-material/ApartmentOutlined";
import GroupsIcon from "@mui/icons-material/GroupsOutlined";
import ScienceIcon from "@mui/icons-material/ScienceOutlined";
import ModelTrainingIcon from "@mui/icons-material/ModelTrainingOutlined";
import RocketLaunchIcon from "@mui/icons-material/RocketLaunchOutlined";
import CloudUploadIcon from "@mui/icons-material/CloudUploadOutlined";
import AccountTreeIcon from "@mui/icons-material/AccountTreeOutlined";
import MonitorHeartIcon from "@mui/icons-material/MonitorHeartOutlined";
import ExtensionIcon from "@mui/icons-material/ExtensionOutlined";
import InsightsIcon from "@mui/icons-material/InsightsOutlined";
import StorefrontIcon from "@mui/icons-material/StorefrontOutlined";
import SearchIcon from "@mui/icons-material/SearchOutlined";
import NotificationsIcon from "@mui/icons-material/NotificationsOutlined";

const DRAWER_WIDTH = 248;

const navGroups = [
  {
    label: "Workspace",
    items: [
      { to: "/dashboard", label: "Dashboard", icon: <DashboardIcon /> },
      { to: "/projects", label: "Projects", icon: <FolderIcon /> },
      { to: "/datasets", label: "Datasets", icon: <DatasetIcon /> },
      { to: "/annotations", label: "Annotation", icon: <LabelIcon /> },
      { to: "/search", label: "Search", icon: <SearchIcon /> },
      { to: "/notifications", label: "Notifications", icon: <NotificationsIcon /> },
    ],
  },
  {
    label: "Organization",
    items: [
      { to: "/enterprises", label: "Enterprises", icon: <BusinessIcon /> },
      { to: "/teams", label: "Teams", icon: <GroupsIcon /> },
    ],
  },
  {
    label: "ML Lifecycle",
    items: [
      { to: "/experiments", label: "Experiments", icon: <ScienceIcon /> },
      { to: "/model-registry", label: "Model Registry", icon: <ModelTrainingIcon /> },
      { to: "/training", label: "Training Jobs", icon: <CloudUploadIcon /> },
      { to: "/deployments", label: "Deployments", icon: <RocketLaunchIcon /> },
      { to: "/pipelines", label: "Pipelines", icon: <AccountTreeIcon /> },
      { to: "/monitoring", label: "Monitoring", icon: <MonitorHeartIcon /> },
    ],
  },
  {
    label: "Platform",
    items: [
      { to: "/analytics", label: "Analytics", icon: <InsightsIcon /> },
      { to: "/plugins", label: "Plugins", icon: <ExtensionIcon /> },
      { to: "/marketplace", label: "Marketplace", icon: <StorefrontIcon /> },
    ],
  },
];

export default function Sidebar() {
  return (
    <Drawer
      variant="permanent"
      sx={{
        width: DRAWER_WIDTH,
        flexShrink: 0,
        [`& .MuiDrawer-paper`]: {
          width: DRAWER_WIDTH,
          boxSizing: "border-box",
          backgroundColor: "rgba(255,255,255,0.6)",
          backdropFilter: "blur(16px)",
          borderRight: "1px solid rgba(255,255,255,0.4)",
        },
      }}
    >
      <Toolbar>
        <Typography variant="h6" className="font-display" sx={{ fontWeight: 700, color: "#4285F4" }}>
          DataLabs
        </Typography>
      </Toolbar>
      <Box sx={{ overflowY: "auto", px: 1 }}>
        {navGroups.map((group) => (
          <Box key={group.label} sx={{ mb: 1 }}>
            <Typography
              variant="caption"
              sx={{ px: 2, color: "text.secondary", fontWeight: 600, letterSpacing: 0.5 }}
            >
              {group.label.toUpperCase()}
            </Typography>
            <List dense>
              {group.items.map((item) => (
                <ListItemButton
                  key={item.to}
                  component={NavLink}
                  to={item.to}
                  sx={{
                    borderRadius: 2,
                    mx: 1,
                    mb: 0.5,
                    "&.active": {
                      backgroundColor: "rgba(66,133,244,0.12)",
                      color: "#4285F4",
                      "& .MuiListItemIcon-root": { color: "#4285F4" },
                    },
                  }}
                >
                  <ListItemIcon sx={{ minWidth: 36 }}>{item.icon}</ListItemIcon>
                  <ListItemText primaryTypographyProps={{ fontSize: 14 }} primary={item.label} />
                </ListItemButton>
              ))}
            </List>
            <Divider sx={{ mx: 2, opacity: 0.4 }} />
          </Box>
        ))}
      </Box>
    </Drawer>
  );
}

export { DRAWER_WIDTH };
