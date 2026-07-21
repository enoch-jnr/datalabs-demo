import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { Box, Typography, TextField, InputAdornment, List, ListItemButton, ListItemText, Chip } from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import GlassCard from "@/components/common/GlassCard";
import { globalSearch } from "@/api/search";
import { SearchResultItem } from "@/api/types";

export default function SearchPage() {
  const [searchParams, setSearchParams] = useSearchParams();
  const [query, setQuery] = useState(searchParams.get("q") ?? "");
  const [results, setResults] = useState<SearchResultItem[]>([]);

  useEffect(() => {
    const q = searchParams.get("q");
    if (q) {
      setQuery(q);
      globalSearch(q).then(setResults);
    }
  }, [searchParams]);

  function handleChange(value: string) {
    setQuery(value);
    if (value.trim()) {
      setSearchParams({ q: value.trim() });
    } else {
      setResults([]);
    }
  }

  return (
    <Box>
      <Typography variant="h4" sx={{ mb: 3 }}>
        Search
      </Typography>

      <TextField
        fullWidth
        placeholder="Search projects, datasets, annotation tasks…"
        value={query}
        onChange={(e) => handleChange(e.target.value)}
        InputProps={{ startAdornment: <InputAdornment position="start"><SearchIcon /></InputAdornment> }}
        sx={{ mb: 3 }}
      />

      <GlassCard sx={{ p: 0 }}>
        <List>
          {results.map((r) => (
            <ListItemButton key={`${r.type}-${r.id}`}>
              <ListItemText primary={r.title} secondary={r.subtitle} />
              <Chip size="small" label={r.type.replace(/_/g, " ")} />
            </ListItemButton>
          ))}
          {results.length === 0 && (
            <Typography color="text.secondary" sx={{ p: 3 }}>
              {query ? "No results." : "Start typing to search across your workspace."}
            </Typography>
          )}
        </List>
      </GlassCard>
    </Box>
  );
}
