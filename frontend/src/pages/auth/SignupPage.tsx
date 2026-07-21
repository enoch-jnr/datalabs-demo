import { useState, FormEvent } from "react";
import { Link as RouterLink, useNavigate } from "react-router-dom";
import { Box, Button, Grid, Link, TextField, Typography, Alert } from "@mui/material";
import GlassCard from "@/components/common/GlassCard";
import { useAuth } from "@/context/AuthContext";

export default function SignupPage() {
  const { signup } = useAuth();
  const navigate = useNavigate();
  const [form, setForm] = useState({ first_name: "", last_name: "", email: "", password: "" });
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);

  function update(field: keyof typeof form, value: string) {
    setForm((prev) => ({ ...prev, [field]: value }));
  }

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setSubmitting(true);
    setError(null);
    try {
      await signup(form);
      navigate("/dashboard");
    } catch (err: any) {
      setError(err?.response?.data?.detail ?? "Sign up failed");
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
      <GlassCard sx={{ p: 5, width: 460 }}>
        <Typography variant="h4" sx={{ mb: 1 }}>
          Create your account
        </Typography>
        <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
          Start collecting, annotating, and versioning data.
        </Typography>

        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        <Box component="form" onSubmit={handleSubmit}>
          <Grid container spacing={2}>
            <Grid item xs={6}>
              <TextField
                label="First name"
                fullWidth
                required
                value={form.first_name}
                onChange={(e) => update("first_name", e.target.value)}
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                label="Last name"
                fullWidth
                required
                value={form.last_name}
                onChange={(e) => update("last_name", e.target.value)}
              />
            </Grid>
          </Grid>
          <TextField
            label="Email"
            type="email"
            fullWidth
            required
            margin="normal"
            value={form.email}
            onChange={(e) => update("email", e.target.value)}
          />
          <TextField
            label="Password"
            type="password"
            fullWidth
            required
            margin="normal"
            helperText="At least 8 characters"
            value={form.password}
            onChange={(e) => update("password", e.target.value)}
          />
          <Button type="submit" fullWidth variant="contained" size="large" sx={{ mt: 3 }} disabled={submitting}>
            {submitting ? "Creating account…" : "Sign up"}
          </Button>
        </Box>

        <Typography variant="body2" sx={{ mt: 3, textAlign: "center" }}>
          Already have an account?{" "}
          <Link component={RouterLink} to="/login">
            Log in
          </Link>
        </Typography>
      </GlassCard>
    </Box>
  );
}
