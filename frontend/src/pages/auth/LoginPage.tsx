import { useState, FormEvent } from "react";
import { Link as RouterLink, useNavigate } from "react-router-dom";
import { Box, Button, Link, TextField, Typography, Alert } from "@mui/material";
import GlassCard from "@/components/common/GlassCard";
import { useAuth } from "@/context/AuthContext";

export default function LoginPage() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setSubmitting(true);
    setError(null);
    try {
      await login(email, password);
      navigate("/dashboard");
    } catch (err: any) {
      setError(err?.response?.data?.detail ?? "Login failed");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <Box
      sx={{
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        background: "linear-gradient(135deg, #eef4ff 0%, #f5f7fb 50%, #fff9ec 100%)",
      }}
    >
      <GlassCard sx={{ p: 5, width: 420 }}>
        <Typography variant="h4" sx={{ mb: 1 }}>
          Welcome back
        </Typography>
        <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
          Log in to your DataLabs workspace.
        </Typography>

        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        <Box component="form" onSubmit={handleSubmit}>
          <TextField
            label="Email"
            type="email"
            fullWidth
            required
            margin="normal"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <TextField
            label="Password"
            type="password"
            fullWidth
            required
            margin="normal"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button type="submit" fullWidth variant="contained" size="large" sx={{ mt: 3 }} disabled={submitting}>
            {submitting ? "Logging in…" : "Log in"}
          </Button>
        </Box>

        <Typography variant="body2" sx={{ mt: 3, textAlign: "center" }}>
          Don&apos;t have an account?{" "}
          <Link component={RouterLink} to="/signup">
            Sign up
          </Link>
        </Typography>
      </GlassCard>
    </Box>
  );
}
