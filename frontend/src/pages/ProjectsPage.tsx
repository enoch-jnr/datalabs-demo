import { useEffect, useState, FormEvent } from "react";
import { useNavigate } from "react-router-dom";
import { Box, Typography, Button, TextField, Grid, Chip, MenuItem } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import GlassCard from "@/components/common/GlassCard";
import { listWorkspaces, createWorkspace } from "@/api/workspaces";
import { listProjects, createProject } from "@/api/projects";
import { Workspace, Project } from "@/api/types";

export default function ProjectsPage() {
  const navigate = useNavigate();
  const [workspaces, setWorkspaces] = useState<Workspace[]>([]);
  const [activeWorkspace, setActiveWorkspace] = useState<string>("");
  const [projects, setProjects] = useState<Project[]>([]);
  const [name, setName] = useState("");
  const [code, setCode] = useState("");

  async function loadWorkspaces() {
    let ws = await listWorkspaces();
    if (ws.length === 0) {
      ws = [await createWorkspace({ name: "Personal Workspace", slug: "personal" })];
    }
    setWorkspaces(ws);
    setActiveWorkspace(ws[0].id);
  }

  useEffect(() => {
    loadWorkspaces();
  }, []);

  useEffect(() => {
    if (activeWorkspace) listProjects(activeWorkspace).then(setProjects);
  }, [activeWorkspace]);

  async function handleCreate(e: FormEvent) {
    e.preventDefault();
    if (!activeWorkspace) return;
    await createProject({ workspace_id: activeWorkspace, name, code });
    setName("");
    setCode("");
    listProjects(activeWorkspace).then(setProjects);
  }

  return (
    <Box>
      <Typography variant="h4" sx={{ mb: 3 }}>
        Projects
      </Typography>

      <GlassCard sx={{ p: 3, mb: 3 }}>
        <Box component="form" onSubmit={handleCreate} sx={{ display: "flex", gap: 2, flexWrap: "wrap", alignItems: "center" }}>
          <TextField select label="Workspace" size="small" value={activeWorkspace} onChange={(e) => setActiveWorkspace(e.target.value)} sx={{ minWidth: 200 }}>
            {workspaces.map((w) => (
              <MenuItem key={w.id} value={w.id}>
                {w.name}
              </MenuItem>
            ))}
          </TextField>
          <TextField label="Project name" size="small" value={name} onChange={(e) => setName(e.target.value)} required />
          <TextField label="Code" size="small" value={code} onChange={(e) => setCode(e.target.value)} required />
          <Button type="submit" variant="contained" startIcon={<AddIcon />}>
            New project
          </Button>
        </Box>
      </GlassCard>

      <Grid container spacing={2}>
        {projects.map((project) => (
          <Grid item xs={12} md={4} key={project.id}>
            <GlassCard
              sx={{ p: 3, cursor: "pointer" }}
              onClick={() => navigate(`/datasets?project_id=${project.id}`)}
            >
              <Typography variant="h6">{project.name}</Typography>
              <Typography variant="caption" color="text.secondary">
                {project.code}
              </Typography>
              <Box sx={{ mt: 1, display: "flex", gap: 1 }}>
                <Chip size="small" label={project.status} />
                <Chip size="small" variant="outlined" label={project.visibility} />
              </Box>
            </GlassCard>
          </Grid>
        ))}
        {projects.length === 0 && (
          <Grid item xs={12}>
            <Typography color="text.secondary">No projects in this workspace yet.</Typography>
          </Grid>
        )}
      </Grid>
    </Box>
  );
}
