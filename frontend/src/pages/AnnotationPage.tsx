import { useEffect, useState, FormEvent } from "react";
import {
  Box,
  Typography,
  Button,
  TextField,
  MenuItem,
  Grid,
  Chip,
  Tabs,
  Tab,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import GlassCard from "@/components/common/GlassCard";
import { listWorkspaces } from "@/api/workspaces";
import { listProjects } from "@/api/projects";
import { listAnnotationTasks, createAnnotationTask } from "@/api/annotations";
import { Project, AnnotationTask } from "@/api/types";

const ANNOTATION_TYPES = [
  { value: "IMAGE_CLASSIFICATION", label: "Image — Classification" },
  { value: "OBJECT_DETECTION", label: "Image — Object Detection" },
  { value: "SEGMENTATION", label: "Image — Segmentation" },
  { value: "TEXT_CLASSIFICATION", label: "Text — Classification" },
  { value: "NAMED_ENTITY_RECOGNITION", label: "Text — NER" },
  { value: "AUDIO_TRANSCRIPTION", label: "Audio — Transcription" },
  { value: "SPEAKER_LABELING", label: "Audio — Speaker Labeling" },
];

const MODALITY_TABS = ["ALL", "IMAGE", "TEXT", "AUDIO"];

function modalityOf(annotationType: string): string {
  if (annotationType.startsWith("IMAGE") || annotationType === "OBJECT_DETECTION" || annotationType === "SEGMENTATION") return "IMAGE";
  if (annotationType.startsWith("TEXT") || annotationType === "NAMED_ENTITY_RECOGNITION") return "TEXT";
  if (annotationType.startsWith("AUDIO") || annotationType === "SPEAKER_LABELING") return "AUDIO";
  return "ALL";
}

export default function AnnotationPage() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [activeProject, setActiveProject] = useState("");
  const [tasks, setTasks] = useState<AnnotationTask[]>([]);
  const [tab, setTab] = useState("ALL");

  const [name, setName] = useState("");
  const [annotationType, setAnnotationType] = useState(ANNOTATION_TYPES[0].value);

  useEffect(() => {
    (async () => {
      const ws = await listWorkspaces();
      const allProjects = (await Promise.all(ws.map((w) => listProjects(w.id)))).flat();
      setProjects(allProjects);
      if (allProjects.length > 0) setActiveProject(allProjects[0].id);
    })();
  }, []);

  useEffect(() => {
    if (activeProject) listAnnotationTasks(activeProject).then(setTasks);
  }, [activeProject]);

  async function handleCreate(e: FormEvent) {
    e.preventDefault();
    if (!activeProject) return;
    await createAnnotationTask({ project_id: activeProject, name, annotation_type: annotationType });
    setName("");
    listAnnotationTasks(activeProject).then(setTasks);
  }

  const visibleTasks = tasks.filter((t) => tab === "ALL" || modalityOf(t.annotation_type) === tab);

  return (
    <Box>
      <Typography variant="h4" sx={{ mb: 3 }}>
        Annotation
      </Typography>

      <GlassCard sx={{ p: 3, mb: 3 }}>
        <Box component="form" onSubmit={handleCreate} sx={{ display: "flex", gap: 2, flexWrap: "wrap", alignItems: "center" }}>
          <TextField select label="Project" size="small" value={activeProject} onChange={(e) => setActiveProject(e.target.value)} sx={{ minWidth: 200 }}>
            {projects.map((p) => (
              <MenuItem key={p.id} value={p.id}>
                {p.name}
              </MenuItem>
            ))}
          </TextField>
          <TextField label="Task name" size="small" value={name} onChange={(e) => setName(e.target.value)} required />
          <TextField
            select
            label="Annotation type"
            size="small"
            value={annotationType}
            onChange={(e) => setAnnotationType(e.target.value)}
            sx={{ minWidth: 240 }}
          >
            {ANNOTATION_TYPES.map((t) => (
              <MenuItem key={t.value} value={t.value}>
                {t.label}
              </MenuItem>
            ))}
          </TextField>
          <Button type="submit" variant="contained" startIcon={<AddIcon />} disabled={!activeProject}>
            New task
          </Button>
        </Box>
      </GlassCard>

      <Tabs value={tab} onChange={(_, v) => setTab(v)} sx={{ mb: 2 }}>
        {MODALITY_TABS.map((m) => (
          <Tab key={m} value={m} label={m === "ALL" ? "All" : m.charAt(0) + m.slice(1).toLowerCase()} />
        ))}
      </Tabs>

      <Grid container spacing={2}>
        {visibleTasks.map((task) => (
          <Grid item xs={12} md={4} key={task.id}>
            <GlassCard sx={{ p: 3 }}>
              <Typography variant="subtitle1" sx={{ fontWeight: 600, mb: 0.5 }}>
                {task.name}
              </Typography>
              <Typography variant="caption" color="text.secondary">
                {task.annotation_type.replace(/_/g, " ")}
              </Typography>
              <Box sx={{ mt: 1.5, display: "flex", gap: 1 }}>
                <Chip size="small" label={task.status} color={task.status === "APPROVED" ? "success" : "default"} />
                <Chip size="small" variant="outlined" label={modalityOf(task.annotation_type)} />
              </Box>
            </GlassCard>
          </Grid>
        ))}
        {visibleTasks.length === 0 && (
          <Grid item xs={12}>
            <Typography color="text.secondary">No annotation tasks yet for this filter.</Typography>
          </Grid>
        )}
      </Grid>
    </Box>
  );
}
