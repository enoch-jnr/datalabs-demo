import { useEffect, useState, FormEvent } from "react";
import {
  Box,
  Typography,
  Button,
  TextField,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
  IconButton,
  Stack,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import DeleteOutlineIcon from "@mui/icons-material/DeleteOutline";
import GlassCard from "./GlassCard";
import { createGeneric, deleteGeneric, listGeneric } from "@/api/generic";

interface FieldConfig {
  name: string;
  label: string;
  type?: "text" | "number";
  defaultValue?: string;
}

interface GenericModulePageProps {
  title: string;
  description: string;
  apiPath: string; // e.g. "/enterprises/"
  columns: { key: string; label: string }[];
  createFields: FieldConfig[];
}

export default function GenericModulePage({
  title,
  description,
  apiPath,
  columns,
  createFields,
}: GenericModulePageProps) {
  const [items, setItems] = useState<Record<string, any>[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [formValues, setFormValues] = useState<Record<string, string>>(
    Object.fromEntries(createFields.map((f) => [f.name, f.defaultValue ?? ""]))
  );

  async function refresh() {
    setLoading(true);
    try {
      const data = await listGeneric<Record<string, any>>(apiPath);
      setItems(data);
      setError(null);
    } catch (err: any) {
      setError(err?.response?.data?.detail ?? "Failed to load data. Is the backend running?");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    refresh();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [apiPath]);

  async function handleCreate(e: FormEvent) {
    e.preventDefault();
    const payload: Record<string, unknown> = {};
    for (const field of createFields) {
      payload[field.name] = field.type === "number" ? Number(formValues[field.name]) : formValues[field.name];
    }
    await createGeneric(apiPath, payload);
    setFormValues(Object.fromEntries(createFields.map((f) => [f.name, f.defaultValue ?? ""])));
    refresh();
  }

  async function handleDelete(id: string) {
    await deleteGeneric(apiPath, id);
    refresh();
  }

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        {title}
      </Typography>
      <Typography variant="body2" color="text.secondary" sx={{ mb: 3, maxWidth: 640 }}>
        {description}
      </Typography>

      <GlassCard sx={{ p: 3, mb: 3 }}>
        <Typography variant="subtitle1" sx={{ mb: 2, fontWeight: 600 }}>
          Create new
        </Typography>
        <Box component="form" onSubmit={handleCreate}>
          <Stack direction="row" spacing={2} flexWrap="wrap" useFlexGap sx={{ mb: 2 }}>
            {createFields.map((field) => (
              <TextField
                key={field.name}
                label={field.label}
                size="small"
                type={field.type ?? "text"}
                value={formValues[field.name]}
                onChange={(e) => setFormValues((prev) => ({ ...prev, [field.name]: e.target.value }))}
                sx={{ minWidth: 220 }}
              />
            ))}
          </Stack>
          <Button type="submit" variant="contained" startIcon={<AddIcon />}>
            Create
          </Button>
        </Box>
      </GlassCard>

      <GlassCard sx={{ p: 0 }}>
        {error && (
          <Typography color="error" sx={{ p: 3 }}>
            {error}
          </Typography>
        )}
        {!error && (
          <TableContainer>
            <Table size="small">
              <TableHead>
                <TableRow>
                  {columns.map((col) => (
                    <TableCell key={col.key} sx={{ fontWeight: 600 }}>
                      {col.label}
                    </TableCell>
                  ))}
                  <TableCell align="right">Actions</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {items.map((item) => (
                  <TableRow key={item.id} hover>
                    {columns.map((col) => (
                      <TableCell key={col.key}>
                        {typeof item[col.key] === "boolean" ? (
                          <Chip
                            size="small"
                            label={item[col.key] ? "true" : "false"}
                            color={item[col.key] ? "success" : "default"}
                          />
                        ) : (
                          String(item[col.key] ?? "—")
                        )}
                      </TableCell>
                    ))}
                    <TableCell align="right">
                      <IconButton size="small" onClick={() => handleDelete(item.id)}>
                        <DeleteOutlineIcon fontSize="small" />
                      </IconButton>
                    </TableCell>
                  </TableRow>
                ))}
                {!loading && items.length === 0 && (
                  <TableRow>
                    <TableCell colSpan={columns.length + 1} align="center" sx={{ py: 4, color: "text.secondary" }}>
                      Nothing here yet — create the first one above.
                    </TableCell>
                  </TableRow>
                )}
              </TableBody>
            </Table>
          </TableContainer>
        )}
      </GlassCard>
    </Box>
  );
}
