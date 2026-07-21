import { useEffect, useState, FormEvent } from "react";
import { useSearchParams } from "react-router-dom";
import {
  Box,
  Typography,
  Button,
  TextField,
  MenuItem,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import GlassCard from "@/components/common/GlassCard";
import { listWorkspaces } from "@/api/workspaces";
import { listProjects } from "@/api/projects";
import { listDatasets, createDataset } from "@/api/datasets";
import { Project, Dataset } from "@/api/types";

export default function DatasetsPage() {
  const [searchParams] = useSearchParams();
  const [projects, setProjects] = useState<Project[]>([]);
  const [activeProject, setActiveProject] = useState(searchParams.get("project_id") ?? "");
  const [datasets, setDatasets] = useState<Dataset[]>([]);
  const [name, setName] = useState("");
  const [code, setCode] = useState("");

  useEffect(() => {
    (async () => {
      const ws = await listWorkspaces();
      const allProjects = (await Promise.all(ws.map((w) => listProjects(w.id)))).flat();
      setProjects(allProjects);
      if (!activeProject && allProjects.length > 0) setActiveProject(allProjects[0].id);
    })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    if (activeProject) listDatasets(activeProject).then(setDatasets);
  }, [activeProject]);

  async function handleCreate(e: FormEvent) {
    e.preventDefault();
    if (!activeProject) return;
    await createDataset({ project_id: activeProject, name, code });
    setName("");
    setCode("");
    listDatasets(activeProject).then(setDatasets);
  }

  return (
    <Box>
      <Typography variant="h4" sx={{ mb: 3 }}>
        Dataset Management
      </Typography>

      <GlassCard sx={{ p: 3, mb: 3 }}>
        <Box component="form" onSubmit={handleCreate} sx={{ display: "flex", gap: 2, flexWrap: "wrap", alignItems: "center" }}>
          <TextField select label="Project" size="small" value={activeProject} onChange={(e) => setActiveProject(e.target.value)} sx={{ minWidth: 220 }}>
            {projects.map((p) => (
              <MenuItem key={p.id} value={p.id}>
                {p.name}
              </MenuItem>
            ))}
          </TextField>
          <TextField label="Dataset name" size="small" value={name} onChange={(e) => setName(e.target.value)} required />
          <TextField label="Code" size="small" value={code} onChange={(e) => setCode(e.target.value)} required />
          <Button type="submit" variant="contained" startIcon={<AddIcon />} disabled={!activeProject}>
            New dataset
          </Button>
        </Box>
      </GlassCard>

      <GlassCard sx={{ p: 0 }}>
        <TableContainer>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell sx={{ fontWeight: 600 }}>Name</TableCell>
                <TableCell sx={{ fontWeight: 600 }}>Code</TableCell>
                <TableCell sx={{ fontWeight: 600 }}>Status</TableCell>
                <TableCell sx={{ fontWeight: 600 }}>Visibility</TableCell>
                <TableCell sx={{ fontWeight: 600 }}>Total assets</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {datasets.map((d) => (
                <TableRow key={d.id} hover>
                  <TableCell>{d.name}</TableCell>
                  <TableCell>{d.code}</TableCell>
                  <TableCell>
                    <Chip size="small" label={d.status} />
                  </TableCell>
                  <TableCell>{d.visibility}</TableCell>
                  <TableCell>{d.total_assets}</TableCell>
                </TableRow>
              ))}
              {datasets.length === 0 && (
                <TableRow>
                  <TableCell colSpan={5} align="center" sx={{ py: 4, color: "text.secondary" }}>
                    No datasets in this project yet.
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </TableContainer>
      </GlassCard>
    </Box>
  );
}
