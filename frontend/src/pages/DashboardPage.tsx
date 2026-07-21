import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Box, Grid, Typography, Button, Chip } from "@mui/material";
import FolderIcon from "@mui/icons-material/FolderOutlined";
import DatasetIcon from "@mui/icons-material/StorageOutlined";
import LabelIcon from "@mui/icons-material/LabelOutlined";
import GlassCard from "@/components/common/GlassCard";
import { useAuth } from "@/context/AuthContext";
import { listWorkspaces, createWorkspace } from "@/api/workspaces";
import { listProjects } from "@/api/projects";
import { Workspace, Project } from "@/api/types";

function StatCard({ icon, label, value, color }: { icon: React.ReactNode; label: string; value: number | string; color: string }) {
  return (
    <GlassCard sx={{ p: 3, display: "flex", alignItems: "center", gap: 2 }}>
      <Box sx={{ p: 1.5, borderRadius: 3, backgroundColor: `${color}22`, color, display: "flex" }}>{icon}</Box>
      <Box>
        <Typography variant="h5" sx={{ fontWeight: 700 }}>
          {value}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {label}
        </Typography>
      </Box>
    </GlassCard>
  );
}

export default function DashboardPage() {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [workspaces, setWorkspaces] = useState<Workspace[]>([]);
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    (async () => {
      let ws = await listWorkspaces();
      if (ws.length === 0) {
        // give first-time users a personal workspace so the rest of the
        // app (projects, datasets) has somewhere to attach to
        const created = await createWorkspace({ name: "Personal Workspace", slug: "personal" });
        ws = [created];
      }
      setWorkspaces(ws);

      const allProjects = (
        await Promise.all(ws.map((w) => listProjects(w.id)))
      ).flat();
      setProjects(allProjects);
      setLoading(false);
    })();
  }, []);

  return (
    <Box>
      <Typography variant="h4" sx={{ mb: 0.5 }}>
        Welcome back, {user?.first_name}
      </Typography>
      <Typography variant="body2" color="text.secondary" sx={{ mb: 4 }}>
        Here&apos;s what&apos;s happening across your workspaces.
      </Typography>

      <Grid container spacing={3} sx={{ mb: 4 }}>
        <Grid item xs={12} sm={4}>
          <StatCard icon={<FolderIcon />} label="Projects" value={loading ? "…" : projects.length} color="#4285F4" />
        </Grid>
        <Grid item xs={12} sm={4}>
          <StatCard icon={<DatasetIcon />} label="Workspaces" value={loading ? "…" : workspaces.length} color="#34A853" />
        </Grid>
        <Grid item xs={12} sm={4}>
          <StatCard icon={<LabelIcon />} label="Annotation tasks" value="—" color="#FBBC05" />
        </Grid>
      </Grid>

      <GlassCard sx={{ p: 3 }}>
        <Box sx={{ display: "flex", justifyContent: "space-between", alignItems: "center", mb: 2 }}>
          <Typography variant="h6">Your projects</Typography>
          <Button variant="contained" size="small" onClick={() => navigate("/projects")}>
            Manage projects
          </Button>
        </Box>
        {projects.length === 0 && !loading && (
          <Typography variant="body2" color="text.secondary">
            No projects yet — head to Projects to create your first one.
          </Typography>
        )}
        <Grid container spacing={2}>
          {projects.map((project) => (
            <Grid item xs={12} md={4} key={project.id}>
              <GlassCard sx={{ p: 2 }}>
                <Typography variant="subtitle1" sx={{ fontWeight: 600 }}>
                  {project.name}
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  {project.code}
                </Typography>
                <Box sx={{ mt: 1 }}>
                  <Chip size="small" label={project.status} />
                </Box>
              </GlassCard>
            </Grid>
          ))}
        </Grid>
      </GlassCard>
    </Box>
  );
}
