import { createTheme } from "@mui/material/styles";

export const theme = createTheme({
  palette: {
    mode: "light",
    primary: { main: "#4285F4" },
    success: { main: "#34A853" },
    warning: { main: "#FBBC05" },
    error: { main: "#EA4335" },
    background: {
      default: "#F5F7FB",
      paper: "rgba(255, 255, 255, 0.75)",
    },
  },
  typography: {
    fontFamily: "'Inter', 'Roboto', sans-serif",
    h1: { fontFamily: "'Poppins', sans-serif", fontWeight: 700 },
    h2: { fontFamily: "'Poppins', sans-serif", fontWeight: 600 },
    h3: { fontFamily: "'Poppins', sans-serif", fontWeight: 600 },
    h4: { fontFamily: "'Poppins', sans-serif", fontWeight: 600 },
    h5: { fontFamily: "'Poppins', sans-serif", fontWeight: 600 },
    h6: { fontFamily: "'Poppins', sans-serif", fontWeight: 600 },
    button: { textTransform: "none", fontWeight: 600 },
  },
  shape: { borderRadius: 16 },
  components: {
    MuiPaper: {
      styleOverrides: {
        root: {
          backgroundImage: "none",
          backdropFilter: "blur(12px)",
          border: "1px solid rgba(255,255,255,0.4)",
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        root: { borderRadius: 12 },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          backdropFilter: "blur(12px)",
          backgroundColor: "rgba(255,255,255,0.75)",
          border: "1px solid rgba(255,255,255,0.5)",
        },
      },
    },
  },
});
