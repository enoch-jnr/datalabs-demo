import { useNavigate } from "react-router-dom";
import { Box, Button, Container, Grid, Typography, Stack } from "@mui/material";
import DatasetIcon from "@mui/icons-material/StorageOutlined";
import LabelIcon from "@mui/icons-material/LabelOutlined";
import ScienceIcon from "@mui/icons-material/ScienceOutlined";
import GlassCard from "@/components/common/GlassCard";

const highlights = [
  {
    icon: <DatasetIcon sx={{ fontSize: 32, color: "#4285F4" }} />,
    title: "Dataset Management",
    body: "Upload, version, and benchmark datasets — GitHub-style versioning for data.",
  },
  {
    icon: <LabelIcon sx={{ fontSize: 32, color: "#34A853" }} />,
    title: "Annotation Workspace",
    body: "Image, audio, and text labeling with task assignment and review workflows.",
  },
  {
    icon: <ScienceIcon sx={{ fontSize: 32, color: "#FBBC05" }} />,
    title: "Experiment Tracking",
    body: "Log runs, metrics, and artifacts as you move from data to trained models.",
  },
];

export default function LandingPage() {
  const navigate = useNavigate();

  return (
    <Box
      sx={{
        minHeight: "100vh",
        background: "linear-gradient(135deg, #eef4ff 0%, #f5f7fb 50%, #fff9ec 100%)",
      }}
    >
      <Container maxWidth="lg" sx={{ pt: 4, pb: 10 }}>
        <Stack direction="row" justifyContent="space-between" alignItems="center" sx={{ mb: 10 }}>
          <Typography variant="h5" className="font-display" sx={{ fontWeight: 700, color: "#4285F4" }}>
            DataLabs
          </Typography>
          <Stack direction="row" spacing={2}>
            <Button color="inherit" onClick={() => navigate("/login")}>
              Log in
            </Button>
            <Button variant="contained" onClick={() => navigate("/signup")}>
              Get started
            </Button>
          </Stack>
        </Stack>

        <Grid container spacing={6} alignItems="center" sx={{ mb: 12 }}>
          <Grid item xs={12} md={7}>
            <Typography variant="h2" sx={{ mb: 3, lineHeight: 1.15 }}>
              One platform for datasets, annotation, and ML experiments.
            </Typography>
            <Typography variant="h6" color="text.secondary" sx={{ mb: 4, fontWeight: 400 }}>
              DataLabs combines Kaggle-style datasets, Scale AI-style annotation, and GitHub-style
              versioning — built for teams collecting and labeling real-world data.
            </Typography>
            <Stack direction="row" spacing={2}>
              <Button size="large" variant="contained" onClick={() => navigate("/signup")}>
                Get Started
              </Button>
              <Button size="large" variant="outlined" onClick={() => navigate("/login")}>
                Log in
              </Button>
            </Stack>
          </Grid>
          <Grid item xs={12} md={5}>
            <GlassCard sx={{ p: 4 }}>
              <Typography variant="overline" color="text.secondary">
                Demo instance
              </Typography>
              <Typography variant="body2" sx={{ mt: 1 }}>
                This is a demo deployment of DataLabs — sign up with any email to explore projects,
                datasets, and the annotation workspace.
              </Typography>
            </GlassCard>
          </Grid>
        </Grid>

        <Grid container spacing={3}>
          {highlights.map((item) => (
            <Grid item xs={12} md={4} key={item.title}>
              <GlassCard sx={{ p: 3, height: "100%" }}>
                <Box sx={{ mb: 2 }}>{item.icon}</Box>
                <Typography variant="h6" sx={{ mb: 1 }}>
                  {item.title}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {item.body}
                </Typography>
              </GlassCard>
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
}
